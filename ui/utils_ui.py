from PyQt5.QtGui import QFont


def create_title_stylesheet():
    background_color = "background-color: #303030;"
    text_color = "color: white;"
    return background_color + text_color


def create_title_font():
    font = QFont()
    font.setBold(True)
    font.setPixelSize(15)
    font.setLetterSpacing(QFont.AbsoluteSpacing, 3)
    return font


def create_stylesheet_header():
    background_color = "background-color: #454545;"
    text_color = "color: white;"
    return background_color + text_color


def create_stylesheet_dark_0():
    background_color = "background-color: #606060;"
    text_color = "color: white;"
    return background_color + text_color


def create_stylesheet_dark_1():
    background_color = "background-color: #707070;"
    text_color = "color: white;"
    return background_color + text_color


def create_stylesheet_button():
    background_color = "background-color: #454545;"
    text_color = "color: white;"
    border_style = "border-style: outset;"
    border_width = "border-width: 2px;"
    border_color = "border-color: #0A0A0A"
    return background_color + text_color + border_style + border_width + border_color


TITLE_FONT = create_title_font()
TITLE_STYLESHEET = create_title_stylesheet()
STYLESHEET_HEADER = create_stylesheet_header()
STYLESHEET_DARK_0 = create_stylesheet_dark_0()
STYLESHEET_DARK_1 = create_stylesheet_dark_1()
STYLESHEET_BUTTON = create_stylesheet_button()
