"""
File: fire.py
Name:
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.2


def highlight_fires(filename):
    """
    :param filename: Requesting the image what we are going to process
    :returning the image are able to find fire and highlight that area to become red

    """
    filepath = 'images/'+filename

    gray_img = SimpleImage(filepath)
    for pixel in gray_img:
        avg = (pixel.green+pixel.red+pixel.blue)//3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.green = avg
            pixel.blue = avg
            pixel.red = avg
    return gray_img


def main():
    """
    Trying to distinguish which areas have fire. If the area has fire,
     I will highlight the red color in that area and the rest of the area turn gray
    """

    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
