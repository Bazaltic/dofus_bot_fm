WHITE = [(52, 74, 27), (78, 39, 36)]
BLACK = [(82, 174, 63), (203, 104, 94), (107, 107, 107), (101, 143, 196)]


def black_and_white(image):
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = image.getpixel((i, j))
            mid = (r + g + b) / 3
            if (r, g, b) in WHITE:
                image.putpixel((i, j), (255, 255, 255))
            elif (r, g, b) in BLACK:
                image.putpixel((i, j), (0, 0, 0))
            else:
                image.putpixel((i, j), (0, 0, 0) if mid > 128 else (255, 255, 255))
    return image
