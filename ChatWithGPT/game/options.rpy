## 이 파일은 귀하의 게임 커스텀으로 변경될 수 있는 옵션을 포함합니다.
##
## 두 개의 '#' 표시로 시작되는 줄은 주석이며, 그것을 없애지 말아야 합니다. 한 개
## 의 '#' 표시로 시작되는 줄은 주석 처리된 코드로 필요한 경우 제거해도 됩니다.


## 기본 ##########################################################################

## 인간이 읽을 수 있는 게임의 이름. 기본 윈도우의 제목으로 사용되며, 인터페이스
## 와 오류 보고에서 보여집니다.
##
## 문자열을 _()로 둘러 쌓으면 씌우면 번역의 대상으로 표시됩니다.

define config.name = _("ChatWithGPT")


## 위에 주어진 제목이 주 메뉴 화면에 표시되는지 결정합니다. 제목을 숨기려면 이것
## 을 False로 설정하십시오.

define gui.show_name = True


## 게임의 버전입니다.

define config.version = "1.0"


## 게임의 about 스크린에 배치되는 텍스트입니다. 텍스트를 삼중 따옴표 사이에 배치
## 하고 단락 사이에 빈 줄을 남겨 둡니다.

define gui.about = _p("""
""")


## 배포판의 실행 파일과 디렉토리에 사용되는 게임의 약식 이름. 이것은 ASCII 전용
## 이어야 하며 공백, 콜론 또는 세미콜론을 포함해서는 안 됩니다.

define build.name = "ChatWithGPT"


## 음악과 음향 ######################################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 사용자가 음향 또는 음성 채널에서 테스트 사운드를 재생할 수 있게 하려면 아래
## 줄의 주석을 제거하고 이를 사용하여 재생할 샘플 사운드를 설정하십시오.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 플레이어가 주 메뉴에 있을 때 재생할 오디오 파일을 설정하려면 다음 줄의 주석
## 처리를 제거하십시오. 이 파일은 중지되거나 다른 파일이 재생 될 때까지 계속 재
## 생합니다.

# define config.main_menu_music = "main-menu-theme.ogg"


## 번역 ##########################################################################
##
## 이러한 변수는 특정 이벤트가 발생할 때 사용되는 전환을 설정합니다. 각 변수는
## 전환으로 설정해야 하며, 전환을 사용하지 말아야 한다는 것을 나타내려면 None으
## 로 설정해야 합니다.

## 게임 메뉴에 진입하거나 나갑니다.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## 게임 메뉴 화면 사이입니다.

define config.intra_transition = dissolve


## 게임이 로드된 후 사용되는 전환입니다.

define config.after_load_transition = None


## 게임 종료 후 주 메뉴에 진입할 때 사용됩니다.

define config.end_game_transition = None


## 게임을 시작할 때 사용되는 전환을 설정하는 변수가 없습니다. 대신, 초기 장면을
## 표시한 후 with 문을 사용하십시오.


## 창 관리 ########################################################################
##
## 이것은 대사 창이 표시됐을 때 제어합니다. 만약 "show"면, 그것은 상항 표시됩니
## 다. 만약 "hide"면, 그것은 대사가 주어질 때만 표시됩니다. 만약 "auto"면, 창은
## 장면(scene) 문 앞에 숨겨져 대화 상자가 표시되면 다시 표시됩니다.
##
## 게임이 시작된 후에는 "window show", "window hide", 그리고 "window auto" 문을
## 사용하여 변경할 수 있습니다.

define config.window = "auto"


## 대화 창을 표시하고 숨기는 데 사용되는 전환

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 환경설정 기본값 ####################################################################

## 기본 글자 속도를 제어합니다. 기본적으로, 0은 즉시이며 다른 숫자는 초당 입력
## 할 문자 수입니다.

default preferences.text_cps = 0


## 기본 auto-forward 지연 시간입니다. 숫자가 클수록 대기 시간이 길어지며, 0 ~ 30
## 이 유효한 범위가 됩니다.

default preferences.afm_time = 15


## 세이브 디렉토리 ####################################################################
##
## 렌파이는 이 게임에 대한 저장 파일을 플랫폼 별로 배치합니다. 세이브 파일들은
## 여기에 있습니다:
##
## 윈도우즈: %APPDATA\RenPy\<config.save_directory>
##
## 매킨토시: $HOME/Library/RenPy/<config.save_directory>
##
## 리눅스: $HOME/.renpy/<config.save_directory>
##
## 이것은 일반적으로 변경해서는 안 되며, 항상 표현형식이 아닌 정확한 문자열이어
## 야 합니다.

define config.save_directory = "ChatWithGPT-1680367288"


## Icon ########################################################################
##
## 작업 표시 줄 또는 독에 표시되는 아이콘.

define config.window_icon = "gui/window_icon.png"


## 빌드 구성 #######################################################################
##
## 이 섹션은 렌파이가 프로젝트를 배포 파일로 만드는 방법을 제어합니다.

init python:

    ## 다음 함수는 파일 패턴을 사용합니다. 파일 패턴은 대/소문자를 구분하지 않으
    ## 며, /의 유무와 관계없이 기본 디렉터리의 상대 경로와 일치합니다. 여러 패턴
    ## 이 일치하면 첫 번째 패턴이 사용됩니다.
    ##
    ## 패턴 있음:
    ##
    ## / 는 디렉토리 구분 기호입니다.
    ##
    ## * 는 디렉토리 구분자를 제외한 모든 문자와 일치합니다.
    ##
    ## ** 는 디렉토리 구분자를 포함해 모든 문자와 일치합니다.
    ##
    ## 예를 들어, "*.txt" 는 기본 디렉토리의 txt 파일들과 일치하고, "game/
    ## **.ogg" 는 게임 디렉토리 또는 그 서브 디렉토리의 ogg 파일들과 일치하며,
    ## "**.psd" 는 프로젝트에서 모든 곳의 psd 파일들과 일치합니다.

    ## 파일을 None으로 분류하여 배포판으로부터 제외하십시오.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 파일을 아카이브하려면 'archive'로 분류하십시오.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## 파일들의 매칭 문서 패턴은 맥앱(Mac App) 빌드에서 중복되므로 app 및 zip 파
    ## 일에 모두 나타납니다.

    build.documentation('*.html')
    build.documentation('*.txt')


## 확장 파일을 다운로드하고 인앱 구매를 수행하려면 Google Play 라이센스 키가 필
## 요합니다. Google Play 개발자 콘솔의 "서비스 및 API"페이지에서 확인할 수 있습
## 니다.

# define build.google_play_key = "..."


## itch.io 프로젝트와 연관된 사용자 이름과 프로젝트 이름이며 슬래시로 구분됩니
## 다.

# define build.itch_project = "renpytom/test-project"
