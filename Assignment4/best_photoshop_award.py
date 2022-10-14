"""
File: best_photoshop_award.py
Name:
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.1555
BLACK_THRESHOLD = 150


def main():
    """
    創作理念：想學好程式但每次作業想破頭都寫不出來，但安慰自己
    學習應該要有耐心的，所以有時候覺得自己很爛也是ok的
    """
    fig = SimpleImage('image_contest/me.jpeg')  # 1108 x 1478
    fig.show()
    bg = SimpleImage('image_contest/suck.jpeg')  # 700 x 411
    bg.make_as_big_as(fig)  # 1108 x 1478
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    """
 put back ground picture and me together.

     """
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            total = fig_pixel.red + fig_pixel.blue + fig_pixel.green
            avg = total // 3
            if fig_pixel.green > avg * THRESHOLD and total > BLACK_THRESHOLD:
                # green screen
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return fig


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
