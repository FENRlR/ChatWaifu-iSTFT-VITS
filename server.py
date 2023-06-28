from scipy.io.wavfile import write
from text import text_to_sequence
from models import SynthesizerTrn
import utils
import commons
import sys
import re
from pydub import AudioSegment
import torch
import logging
import requests
import json
import os
import openai
import socket
import datetime
from text.symbols import symbols


class SocketServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.client, self.addr = self.socket.accept()

    def receive(self):
        total_data = b""
        while True:
            data = self.client.recv(1024)
            total_data += data
            if len(data) < 1024:
                break
        return total_data.decode()

    def send(self, data):
        self.client.send(data.encode())

    def stop(self):
        self.socket.close()

class vits():
    def __init__(self, model, config):
        logging.getLogger('numba').setLevel(logging.WARNING)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        hps_ms = utils.get_hparams_from_file(config)
        self.n_symbols = len(hps_ms.symbols) if 'symbols' in hps_ms.keys() else 0

        self.net_g_ms = SynthesizerTrn(
            len(symbols),
            hps_ms.data.filter_length // 2 + 1,
            hps_ms.train.segment_size // hps_ms.data.hop_length,
            **hps_ms.model).to(self.device)
        _ = self.net_g_ms.eval()
        self.hps_ms = hps_ms
        _ = utils.load_checkpoint(model, self.net_g_ms,None)


    def get_text(self, text):
        text_norm = text_to_sequence(text, self.hps_ms.data.text_cleaners)
        if self.hps_ms.data.add_blank:
            text_norm = commons.intersperse(text_norm, 0)
        text_norm = torch.LongTensor(text_norm)
        return text_norm
    
    
    def get_label_value(self, text, label, default, warning_name='value'):
        value = re.search(rf'\[{label}=(.+?)\]', text)
        if value:
            try:
                text = re.sub(rf'\[{label}=(.+?)\]', '', text, 1)
                value = float(value.group(1))
            except:
                print(f'Invalid {warning_name}!')
                sys.exit(1)
        else:
            value = default
        return value, text


    def get_label(self, text, label):
        if f'[{label}]' in text:
            return True, text.replace(f'[{label}]', '')
        else:
            return False, text


    def generateSound(self, inputString):
        fltstr = re.sub(r"[\[\]\(\)\{\}]", "", inputString)
        stn_tst = self.get_text(fltstr)

        with torch.no_grad():
            x_tst = stn_tst.cuda().unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cuda()
            audio = self.net_g_ms.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=1)[0][
                0, 0].data.cpu().float().numpy()
        out_path = "./output.wav"
        write(out_path, self.hps_ms.data.sampling_rate, audio)
        print('Successfully saved!')
        # torch.cuda.empty_cache()
        return out_path





get_dir = lambda x: os.path.split(os.path.realpath(x))[0]

def download_file(url, save_dir):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(os.path.join(save_dir, local_filename), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    return local_filename

class openai_session():
    def __init__(self, api_key, tts_service):
        self.api_key = api_key
        openai.api_key = api_key
        self.language = tts_service
        self.messages = []
        self.model = "gpt-3.5-turbo"
        self.currunt_log = f"userfile/log/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
        if not os.path.exists("userfile/log"):
            os.makedirs("userfile/log")

    def save(self):
        with open(self.currunt_log, 'w', encoding='utf-8') as f:
            data = json.dumps(self.messages, ensure_ascii=False, indent=4)
            f.write(data)

    def set_role(self, role):
        prefix = ""
        if self.language == 0:
            prefix = "From now on, you will assume the following roles to conduct the conversation: \n"
        elif self.language == 1:
            prefix = "이제부터 당신은 다음과 같은 역할을 맡아 대화를 진행합니다: \n"
        elif self.language == 2:
            prefix = "これからあなたは次の役割を果たして会話を続けます。: \n"

        self.messages.append({"role": "system", "content": prefix + role})

    def set_greeting(self, greeting):
        self.messages.append({"role": "assistant", "content": greeting})
    
    def send_message(self, message):
        answer = ""
        try:
            self.messages.append({"role": "user", "content": message})
            res = openai.ChatCompletion.create(
                model=self.model,
                messages=self.messages if len(self.messages) <= 30 else [self.messages[0]] + self.messages[-9:],
            )
            answer = res['choices'][0]['message']['content']
            self.messages.append({"role": "assistant", "content": answer})
            self.save()
        except Exception as e:
            if self.language == 0:
                answer = "Excuse me, could you repeat what you just said?"
            elif self.language == 1:
                answer = "앗.. 뭐라고 하셨었죠? 다시 한번 말씀해 주실 수 있나요?"
            elif self.language == 2:
                answer = "あっ、何て言ってましたっけ？ もう一度おっしゃっていただけますか？"

            print("ERROR Occurred: " + str(e))

        return answer
    


def main():
    #"""
    server = SocketServer("127.0.0.1", 9000)
    print("Waiting connection from client...")
    server.start()

    print("Connected.")

    tts_service = int(server.receive()) # language selection
    lang = ["eng", "kor", "jp"]

    model_path = f"./userfile/tts/{lang[tts_service]}/model.pth"
    config_path = f"./userfile/tts/{lang[tts_service]}/config.json"

    if not os.path.isfile(model_path):
        os.makedirs(get_dir(model_path), exist_ok=True)
        print("ERROR : model.pth not found.")

    if not os.path.isfile(config_path):
        os.makedirs(get_dir(config_path), exist_ok=True)
        print("ERROR : config.json not found.")

    tts = vits(model_path, config_path)
    config = json.load(open(config_path, 'r'))


    print("Input API KEY to the client")
    print("You can get API KEY from : https://platform.openai.com/account/api-keys")

    session_token = server.receive()

    if(session_token):
        print(f"API KEY: ...{session_token[-8:]}")
        oai = openai_session(session_token, tts_service)

        setting = server.receive()
        oai.set_role(setting)
        print("Background concept: "+ setting)

        greeting = server.receive()
        oai.set_greeting(greeting)
        print("Greeting: "+ greeting)

        while True:
            question = server.receive()
            print("Question Received: " + question)

            answer = oai.send_message(question)
            print("ChatGPT:", answer)

            tts_audio_path = tts.generateSound(answer)

            # convert wav to ogg
            src = tts_audio_path
            dst = "./ChatWithGPT/game/audio/test.ogg"
            sound = getattr(AudioSegment, f'from_{src.split(".")[-1]}')(src)
            sound.export(dst, format="ogg")

            # send response to UI
            server.send(answer)

            # finish playing audio
            print(server.receive())



    #"""






if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)
    except ConnectionResetError:
        print("Connection lost.")
        sys.exit(0)