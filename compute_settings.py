import yaml
from classes.line import *
import pyautogui


def get_pixel_color():
    img = pyautogui.screenshot()
    width, height = img.size
    while True:
        pos_brut = pyautogui.position()
        x, y = pos_brut.x, pos_brut.y
        if x <= 0 or x >= width or y <= 0 or y >= height:
            continue
        print(img.getpixel((x, y)))


def create_yml():
    obj = []
    with open(r"C:\Users\Bousq\Downloads\Feuille de calcul sans titre - Copie de Feuille 1 (4).csv", 'r') as f:
        content = f.read()
        content_lines = content.split('\n')
        tmp = []
        for lines in content_lines:
            tmp.append(lines.split(','))
        for i in range(0, len(tmp), 2):
            minimum = Area(int(tmp[i][0]), int(tmp[i+1][0]), int(tmp[i][1]), int(tmp[i+1][1]))
            maximum = Area(int(tmp[i][2]), int(tmp[i+1][2]), int(tmp[i][3]), int(tmp[i+1][3]))
            effect = Area(int(tmp[i][4]), int(tmp[i+1][4]), int(tmp[i][5]), int(tmp[i+1][5]))
            modify = Area(int(tmp[i][6]), int(tmp[i+1][6]), int(tmp[i][7]), int(tmp[i+1][7]))
            base = Area(int(tmp[i][8]), int(tmp[i+1][8]), int(tmp[i][9]), int(tmp[i+1][9]))
            pa = Area(int(tmp[i][10]), int(tmp[i+1][10]), int(tmp[i][11]), int(tmp[i+1][11]))
            ra = Area(int(tmp[i][12]), int(tmp[i+1][12]), int(tmp[i][13]), int(tmp[i+1][13]))
            obj.append(Line(minimum, maximum, effect, modify, base, pa, ra))
    result = {
        "button_fusion": Area(1840, 450, 2234, 503),
        "stats": obj
    }
    with open("config.yml", 'w') as y:
        y.write(yaml.dump(result))


#create_yml()
get_pixel_color()

"""
  max_x: '2234'
  max_y: '503'
  min_x: '1840'
  min_y: '450'
"""