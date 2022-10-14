"""
File: mirror_lake.py
Name:
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
creating the opposite picture and combine original picture
    """
    filepath = 'images/'+filename
    img = SimpleImage(filepath)
    b_img = SimpleImage.blank(img.width, img.height *2)

    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            #照片先貼到上方
            b_img_top= b_img.get_pixel(x, y)
            b_img_top.red = img_p.red
            b_img_top.green = img_p.green
            b_img_top.blue = img_p.blue

            b_img_bottom = b_img.get_pixel(x, b_img.height - 1 - y)
            b_img_bottom.red = img_p.red
            b_img_bottom.green = img_p.green
            b_img_bottom.blue = img_p.blue
    b_img.show()



def main():
    """
creating the opposite picture and combine original picture
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()

    reflected = reflect('mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
