################################################################################
## 초기화
################################################################################

## 이 파일에서 init offset 문을 사용하면 이 파일의 초기화 문이 다른 파일의 init
## 코드보다 먼저 실행됩니다.
init offset = -2

## gui.init의 호출은 스타일을 합리적인 기본값으로 재설정하고, 게임의 너비(width)
## 와 높이(height)를 설정합니다.
init python:
    gui.init(1920, 1080)



################################################################################
## GUI 설정 변수
################################################################################


## 색상 ##########################################################################
##
## 인터페이스에서 글자의 색상입니다.

## 강조 색상은 레이블(label)과 강조된 글자로 인터페이스 전체에서 사용됩니다.
define gui.accent_color = '#0099cc'

## 텍스트 버튼(text button)이 선택(selected)됐거나 커서를 올리지(hovered) 않았을
## 때 사용됩니다.
define gui.idle_color = '#888888'

## 작은(small) 색상은 같은 효과를 내기 위해 더 밝거나 어두워야 하는 작은 글자에
## 사용됩니다.
define gui.idle_small_color = '#aaaaaa'

## 버튼(button)과 막대(bar)에 커서를 올렸을 때(hovered) 사용됩니다.
define gui.hover_color = '#66c1e0'

## 텍스트 버튼(text button)에 선택됐지만(selected) 포커스되지(focused) 않았을 때
## 사용됩니다. 버튼(button)은 현재 화면이거나 설정값인 경우 선택됨(selected)이
## 됩니다.
define gui.selected_color = '#ffffff'

## 텍스트 버튼(text button)이 선택되지(selected) 않았을 때 사용됩니다.
define gui.insensitive_color = '#8888887f'

## 채워지지 않은 빈 막대(bar)에 사용됩니다. 이것은 바로 사용되지 않지만, 막대
## (bar) 이미지 파일이 재생성됐을 때 사용됩니다.
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## 대사(dialogue)와 선택지(menu choice)의 글자에서 사용됩니다.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## 글자와 글자 크기 ###################################################################

## 인-게임 글자에 사용됩니다.
define gui.text_font = "SourceHanSansLite.ttf"

## 캐릭터의 이름에 사용됩니다.
define gui.name_text_font = "SourceHanSansLite.ttf"

## 인터페이스에 사용됩니다.
define gui.interface_text_font = "SourceHanSansLite.ttf"

## 일반 대사의 글자 크기입니다.
define gui.text_size = 33

## 캐릭터 이름의 글자 크기입니다.
define gui.name_text_size = 45

## 게임의 유저 인터페이스에서 글자의 크기입니다.
define gui.interface_text_size = 33

## 게임의 유저 인터페이스에서 레이블(label)들의 글자 크기입니다.
define gui.label_text_size = 36

## 통지(notify) 화면의 글자 크기입니다.
define gui.notify_text_size = 24

## 게임의 타이틀(title) 글자의 크기입니다.
define gui.title_text_size = 75


## 메인과 게임 메뉴들 ##################################################################

## 이미지들은 메인(main)과 게임 메뉴(game menu)에 사용됩니다.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## 대사 ##########################################################################
##
## 이러한 변수들은 한 번에 한 줄의 대사가 어떻게 화면에 표시되는지 제어합니다.

## 대사를 포함하는 텍스트 박스의 높이입니다.
define gui.textbox_height = 278

## 화면에 텍스트박스를 세로로 배치합니다. 0.0은 최상단, 0.5는 중앙, 그리고 1.0은
## 최하단입니다.
define gui.textbox_yalign = 1.0


## 말하는 캐릭터의 이름을 텍스트 박스를 기준으로 배치합니다. 이것은 좌측이나 최
## 상단으로부터 전체 픽셀값의 숫자가 되거나, 0.5로 중앙이 될 수 있습니다.
define gui.name_xpos = 360
define gui.name_ypos = 0

## 캐릭터들의 이름을 수평으로 정렬합니다. 이것은 0.0으로 좌측 정렬, 0.5로 중앙,
## 그리고 1.0으로 우측 정렬될 수 있습니다.
define gui.name_xalign = 0.0

## 캐릭터들의 이름이 들어 있는 박스의 너비, 높이, 그리고 테두리입니다. 혹은 그것
## 을 None으로 자동 설정할 수 있습니다.
define gui.namebox_width = None
define gui.namebox_height = None

## 캐릭터의 이름이 들어 있는 박스의 테두리를 좌측, 상단, 우측, 하단의 순서로 정
## 합니다.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## 만약 참(True)이면, 네임박스의 배경은 바둑판식으로 배열(tiled)될 것이고, 거짓
## (False)이면, 네임박스의 배경은 채워질(scaled) 것입니다.
define gui.namebox_tile = False


## 텍스트박스에서 대사의 위치입니다. These can be a whole number of pixels
## relative to the left or top side of the textbox, or 0.5 to center.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## 픽셀값에서 대사의 최대 너비입니다.
define gui.dialogue_width = 1116

## 대사 글자의 수평 정렬입니다. 이것은 0.0으로 좌측 정렬, 0.5로 중앙, 그리고 1.0
## 으로 우측 정렬이 될 수 있습니다.
define gui.dialogue_text_xalign = 0.0


## 버튼들 #########################################################################
##
## 이러한 변수들은 GUI/버튼에서 이미지 파일들과 함께 어떻게 버튼이 표시되는지 제
## 어합니다.

## 픽셀값에서 버튼의 너비와 높이입니다. 만약 None이면, 렌파이가 크기를 계산합니
## 다.
define gui.button_width = None
define gui.button_height = None

## 좌측, 상단, 우측, 하단의 순서에서 버튼의 테두리 값입니다.
define gui.button_borders = Borders(6, 6, 6, 6)

## 만약 참(True)이면, 배경 이미지는 바둑판식으로 배열(tiled)될 것입니다. 만약 거
## 짓(False)이면, 배경 이미지는 선으로 채워질(scaled) 것입니다.
define gui.button_tile = False

## 버튼에 사용된 글자의 폰트입니다.
define gui.button_text_font = gui.interface_text_font

## 버튼에 사용된 글자의 크기입니다.
define gui.button_text_size = gui.interface_text_size

## 다양한 상태의 버튼 글자의 색상입니다.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## 버튼 글자의 수평 정렬(0.0은 왼쪽，0.5은 가운데，1.0은 오른쪽)입니다.
define gui.button_text_xalign = 0.0


## 이러한 변수는 다른 종류의 버튼 설정을 덮어씌웁니다. 사용 가능한 버튼의 종류
## 와, 각각 무엇을 위해 사용하는지는 gui 문서를 확인해주세요.
##
## 이러한 사용자 지정은 기본 인터페이스에 사용됩니다:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## 당신은 또한 설정된 이름의 변수를 추가함으로써 당신만의 커스텀을 추가할 수 있
## 습니다. 예를 들어, 다음 행의 주석 표시를 제거하여 탐색(navigation) 버튼의 너
## 비를 설정할 수 있습니다.

# define gui.navigation_button_width = 250


## 선택 버튼들 ######################################################################
##
## 선택 버튼은 인-게임 메뉴에 사용됩니다.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


## 파일 슬롯 버튼 ####################################################################
##
## 파일 슬롯 버튼은 버튼의 특별한 종류입니다. 그것은 썸네일 이미지나 저장 슬롯의
## 콘텐츠를 설명하는 글자를 포함합니다. GUI/버튼에서 저장 슬롯은 버튼의 다른 종
## 류와 같은 이미지 파일을 사용합니다.

## 저장 슬롯 버튼입니다.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## 저장 슬롯에 사용되는 썸네일의 너비와 높이입니다.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## 저장 슬롯의 그리드(grid)에서 행(rows)과 열(columns)의 갯수입니다.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## 위치와 간격 ######################################################################
##
## 이러한 변수들은 다양한 사용자 인터페이스 요소들의 위치와 간격을 제어합니다.

## 화면의 왼쪽을 기준으로 하는 네비게이션 버튼의 왼쪽 위치입니다.
define gui.navigation_xpos = 60

## 스킵 표시기(skip indicator)의 수직 위치입니다.
define gui.skip_ypos = 15

## 통지(notify) 스크린의 수직 위치입니다.
define gui.notify_ypos = 68

## 선택지의 메뉴 선택 간의 간격입니다.
define gui.choice_spacing = 33

## 메인과 게임 메뉴에서 네비게이션 섹션의 버튼들 간의 간격입니다.
define gui.navigation_spacing = 6

## 환경 설정들 간의 간격을 제어합니다.
define gui.pref_spacing = 15

## 환경 설정 버튼들 사이의 간격을 제어합니다.
define gui.pref_button_spacing = 0

## 파일 페이지 버튼들 간의 간격입니다.
define gui.page_spacing = 0

## 파일 슬롯들 간의 간격입니다.
define gui.slot_spacing = 15

## 메인 메뉴 글자의 위치입니다.
define gui.main_menu_text_xalign = 1.0


## 프레임들 ########################################################################
##
## 이러한 변수들은 오버레이되거나 창이 없을 때 보여지는 사용자 인터페이스 구성
## 요소들을 포함하는 프레임을 제어합니다.

## Generic frames.
define gui.frame_borders = Borders(6, 6, 6, 6)

## 프레임은 확인(confirm) 화면의 일부로 사용됩니다.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## 프레임은 스킵(skip) 화면의 일부로 사용됩니다.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## 프레임은 통지(notify) 화면의 일부로 사용됩니다.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## 프레임 배경들은 바둑판식으로 배열해야 할까요?
define gui.frame_tile = False


## 막대, 스크롤바, 슬라이더 ##############################################################
##
## 이러한 설정은 막대와 스크롤바, 그리고 슬라이더의 보여지는 것과 크기를 제어합
## 니다.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## 수평 막대, 스크롤바, 슬라이더의 높이. 수직 막대, 스크롤바, 슬라이더의 너비.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## 막대 이미지가 바둑판식 배열돼야 하면 참(True)입니다. 선으로 채워져야 한다면
## 거짓(False)입니다.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## 수평 테두리입니다.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## 수직 테두리입니다.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## GUI에서 스크롤할 수 없는 스크롤 막대로 뭘 할 수 있나요? "hide"로 그것들을 숨
## 기고, None은 그것들을 보여줍니다.
define gui.unscrollable = "hide"


## 대사록 #########################################################################
##
## 대사록 화면은 사용자가 이미 확인한 다이얼로그를 표시합니다.

## 렌파이가 보관할 대사록의 블록 갯수입니다.
define config.history_length = 250

## 대사록 화면 항목의 높이를 지정하거나 None으로 하여 높이를 성능에 맡길 수 있습
## 니다.
define gui.history_height = 210

## 말하는 캐릭터의 이름을 나타내는 레이블의 위치, 너비, 그리고 정렬입니다.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## 대사 글자의 위치, 너비, 그리고 정렬입니다.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL-모드 ######################################################################
##
## NVL-모드 화면은 NVL-모드 캐릭터들에 의한 대화를 화면에 표시합니다.

## NVL-모드 배경 창에서 배경의 테두리입니다.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## 렌파이가 표시할 NVL-mode 항목의 최대 수입니다. 설정보다 많은 항목이 표시되면
## 가장 오래된 항목이 제거됩니다.
define gui.nvl_list_length = 6

## NVL-모드 항목의 높이입니다. 이것을 None으로 설정하면 항목들은 동적으로 높이를
## 조정합니다.
define gui.nvl_height = 173

## gui.nvl_height 값이 None일 때 NVL-모드 항목들, 그리고 NVL-모드 항목들과 NVL-
## 모드 메뉴간의 간의 간격입니다.
define gui.nvl_spacing = 15

## 말하는 캐릭터의 이름을 나타내는 레이블의 위치, 너비, 그리고 정렬입니다.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## 대사 글자의 위치, 너비, 그리고 정렬입니다.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## nvl_thought 글자의 위치, 너비, 정렬(nvl_narrator 캐릭터에 의해 표시되는 글자)
## 입니다.
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## NVL 메뉴 버튼의 위치입니다.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

## 현지화 #########################################################################

## 줄 바꿈이 허용되는 위치를 제어합니다. 기본값은 대부분의 언어에 적
## 합합니다. 사용 가능한 값 목록은 https://www.renpy.org/doc/html/
## style_properties.html#style-property-language 에서 찾을 수 있습니다.

define gui.language = "unicode"


################################################################################
## 모바일 기기
################################################################################

init python:

    ## 이것은 휴대전화와 태블릿에서 쉽게 터치할 수 있도록 빠른(Quick) 버튼들의
    ## 크기를 크게 합니다.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## 이것은 휴대전화에서 다양한 GUI 요소들의 크기와 간격을 쉽게 보일 수 있도록
    ## 변경합니다.
    @gui.variant
    def small():

        ## 글자 크기들.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## 텍스트박스의 위치를 조정합니다.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Change the size and spacing of various things.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## 파일 버튼 레이아웃.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-모드.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
