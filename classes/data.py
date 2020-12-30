import pytesseract
import pyautogui
from .utils import black_and_white
from .line import load_settings


def create_item_info(number_of_stats, number_of_damage_line):
    settings = load_settings()
    stats = settings["stats"]
    return ItemInfo(stats, number_of_stats, number_of_damage_line)


class ItemInfo:
    def __init__(self, settings, number_of_line_stats, number_of_line_damage):
        self.number_of_items = number_of_line_stats
        self.items = []
        for i in range(number_of_line_damage, number_of_line_stats + 1):
            self.items.append(LineInfo(settings[i]))

    def compute_info(self):
        img = pyautogui.screenshot()
        for item in self.items:
            item.compute(img)
            # print("#########\n{}\n".format(str(item)))

    def get_best_stat_to_fm(self):
        # TODO: Ajouter le système de poids
        best_stats = None
        for item in self.items:
            if not best_stats and item.has_rune:
                best_stats = item
                continue
            state_best = best_stats.get_state_info()
            state = item.get_state_info()
            if state["to_max"] > state_best["to_max"] and item.has_rune:
                print("#############\n{}\n{}\n".format(state_best, state))
                best_stats = item
        return best_stats


class LineInfo:
    def __init__(self, settings):
        self._minimum_area = Text(settings.minimum)
        self._maximum_area = Text(settings.maximum)
        self._effect_area = Text(settings.effect)
        self._modify_area = Text(settings.modify)
        self._rune_base_area = Rune(settings.base)
        self._rune_pa_area = Rune(settings.pa)
        self._rune_ra_area = Rune(settings.ra)
        self.minimum = None
        self.maximum = None
        self.effect = None
        self.modify = None
        self.rune_base = False
        self.rune_pa = False
        self.rune_ra = False

    @property
    def has_rune(self):
        return self.rune_base or self.rune_pa or self.rune_ra

    def compute(self, image):
        self.minimum = self._minimum_area.extract_data(image)
        self.maximum = self._maximum_area.extract_data(image)
        self.effect = self._effect_area.extract_data(image)
        if not self.effect and self.minimum and self.maximum:
            self.effect = 0
        self.modify = self._modify_area.extract_data(image)
        self.rune_base = self._rune_base_area.get_rune_info(image)
        self.rune_pa = self._rune_pa_area.get_rune_info(image)
        self.rune_ra = self._rune_ra_area.get_rune_info(image)

    def get_state_info(self):
        return {"to_min": self.minimum - self.effect,
                "to_max": self.maximum - self.effect
                }

    def apply_rune(self, use_pa, use_ra):
        if use_ra:
            self._rune_ra_area.click()
        elif use_pa:
            self._rune_pa_area.click()
        else:
            self._rune_base_area.click()

    def __str__(self):
        return "Minimum: {}\nMaximum: {}\nEffect: {}\nModify: {}\nRune base: {}\nRune pa: {}\nRune ra: {}".format(
            self.minimum, self.maximum, self.effect, self.modify, self.rune_base, self.rune_pa, self.rune_ra)


class Text:
    def __init__(self, area):
        self._area = (area.min_x, area.min_y, area.max_x, area.max_y)
        self.data = None

    def extract_data(self, image):
        crop = image.crop(self._area)
        baw = black_and_white(crop)
        val = pytesseract.image_to_string(baw, config='--oem 3 --psm 6 outputbase digits')
        try:
            return int(val)
        except:
            return None


class Rune:
    def __init__(self, area):
        self._area = (area.min_x, area.min_y, area.max_x, area.max_y)
        self._center = ((area.max_x + area.min_x)/2, (area.max_y + area.min_y)/2)

    def get_rune_info(self, image):
        crop = image.crop(self._area)
        x, y = int(crop.size[0]/2), int(crop.size[1]/2)
        pixels = []
        for i in range(x - 5, x + 5):
            for j in range(y - 5, y + 5):
                pixels.append(crop.getpixel((i, j)))
        total = (0, 0, 0)
        for pixel in pixels:
            r, g, b = total
            rr, gg, bb = pixel
            total = (r + rr, b + bb, g + gg)
        r, g, b = total
        r, g, b = r/len(pixels), g/len(pixels), b/len(pixels)
        return r > 40 and g > 40 and b > 40

    def click(self):
        pyautogui.click(self._center)
