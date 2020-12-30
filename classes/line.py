from yaml import YAMLObject, load


def load_settings():
    return load(open("config.yml", 'r').read())


class Line(YAMLObject):
    def __init__(self, minimum, maximum, effect, modify, base, pa, ra):
        self.minimum = minimum
        self.maximum = maximum
        self.effect = effect
        self.modify = modify
        self.base = base
        self.pa = pa
        self.ra = ra


class Area(YAMLObject):
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def get_center(self):
        return [(self.max_x + self.min_x) / 2, (self.max_y + self.min_y) / 2]
