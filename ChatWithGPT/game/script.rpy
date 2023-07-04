# Game scripts can be placed in this file.

# Declare the characters used by this game. The color parameter colors the character name.

define e = Character("Chatbot")
define y = Character("User")
define config.gl2 = True

image hiyori = Live2D("Resources/Hiyori", base=.6, loop = True, fade=True)


init python:
    import socket
    import time
    thinking = 0
    total_data = bytes()
    renpy.block_rollback()
    ip_port = ('127.0.0.1', 9000)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ip_port)


# The game starts here.

label start:
    $ renpy.block_rollback()
    show hiyori m01

    jump chooseTts

label chooseTts:
    $ renpy.block_rollback()
    menu TTSChoice:
        e"Select language"
        "Korean":
            python:
                client.send(("1").encode())
            jump getApiKey
        "Japanese":
            python:
                client.send(("2").encode())
            jump getApiKey


label getApiKey:
    $ renpy.block_rollback()
    python:
        token = renpy.input("Enter openAI API KEY")
        client.send(token.encode())

    jump chooseinput
    return

label chooseinput:
    $ renpy.block_rollback()
    menu inputchoice:
        e"Choose Input method"
        "Keyboard":
            python:
                client.send(("0").encode())
            jump uploadSetting
        "Voice recognition":
            python:
                client.send(("1").encode())
            jump uploadSettingV


label uploadSetting:
    $ renpy.block_rollback()
    python:
        token = renpy.input("Enter background explanation of the character")
        client.send(token.encode())
    jump uploadInit

label uploadInit:
    $ renpy.block_rollback()
    python:
        token = renpy.input("Enter the first line of the character (greeting)")
        client.send(token.encode())
    jump talk_keyboard

label talk_keyboard:
    $ renpy.block_rollback()
    show hiyori m02
    python:
        message = renpy.input("User：")
        client.send(message.encode())
        data = bytes()
    jump checkRes



label uploadSettingV:
    $ renpy.block_rollback()
    e "Give some background explanation of the character"
    python:
        message = "Input：" + client.recv(1024).decode() #renpy.input("User：")
    e "[message]"
    jump uploadInitV

label uploadInitV:
    $ renpy.block_rollback()
    e "Give the first line of the character (greeting)"
    python:
        message = "Input：" + client.recv(1024).decode() #renpy.input("User：")
    e "[message]"
    jump talk_voice

label talk_voice:
    $ renpy.block_rollback()
    show hiyori m02
    e "User："
    python:
        message = "User：" + client.recv(1024).decode() #renpy.input("User：")
        data = bytes()
    e "[message]"
    jump checkResV


label checkRes:
    $ renpy.block_rollback()
    if(thinking == 0):
        show hiyori m03
    e "..."

    python:
        client.setblocking(0)
        try:
                data = client.recv(1024)
                total_data += data
        except:
                data = bytes()
                client.setblocking(1)

    if(len(data) > 0 and len(data) < 1024):
        python:
            response = total_data.decode()
            total_data = bytes()
            thinking = 0
        jump answer
    else:
        $ renpy.block_rollback()
        e "......"
        $ thinking = 1
        jump checkRes




label answer:
    show hiyori talking
    voice "/audio/test.ogg"
    $ renpy.block_rollback()
    e "[response]"
    voice sustain

    $ client.send("Playback complete".encode())
    jump talk_keyboard



label checkResV:
    $ renpy.block_rollback()
    if(thinking == 0):
        show hiyori m03
    e "..."

    python:
        client.setblocking(0)
        try:
                data = client.recv(1024)
                total_data += data
        except:
                data = bytes()
                client.setblocking(1)

    if(len(data) > 0 and len(data) < 1024):
        python:
            response = total_data.decode()
            total_data = bytes()
            thinking = 0
        jump answerV
    else:
        $ renpy.block_rollback()
        e "......"
        $ thinking = 1
        jump checkResV


label answerV:
    show hiyori talking
    voice "/audio/test.ogg"
    $ renpy.block_rollback()
    e "[response]"
    voice sustain

    $ client.send("Playback complete".encode())
    jump talk_voice