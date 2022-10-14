"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
Average pixels in all corners of the original image
    """
    # Todo: create a new blank img that is as big as the original one

    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            new_img_pixel = new_img.get_pixel(x, y)
            if x == 0 and y == 0:
                # (0, 1), (1, 0), (1, 1)
                pixelA = img.get_pixel(0, 1)
                pixelB = img.get_pixel(1, 0)
                pixelC = img.get_pixel(1, 1)
                avg_red = (pixel.red + pixelA.red + pixelB.red + pixelC.red) // 4
                avg_blue = (pixel.blue + pixelA.blue + pixelB.blue + pixelC.blue) // 4
                avg_green = (pixel.green + pixelA.green + pixelB.green + pixelC.green) // 4
            # Get pixel at the top-right corner of the image.
            elif x == img.width - 1 and y == 0:
                pixelA = img.get_pixel(x - 1, y)
                pixelB = img.get_pixel(x - 1, y + 1)
                pixelC = img.get_pixel(x, y + 1)
                avg_red = (pixel.red + pixelA.red + pixelB.red + pixelC.red) // 4
                avg_blue = (pixel.blue + pixelA.blue + pixelB.blue + pixelC.blue) // 4
                avg_green = (pixel.green + pixelA.green + pixelB.green + pixelC.green) // 4
            # Get pixel at the bottom-left corner of the image
            elif x == 0 and y == img.height - 1:
                pixelA = img.get_pixel(x, y - 1)
                pixelB = img.get_pixel(x + 1, y - 1)
                pixelC = img.get_pixel(x + 1, y)
                avg_red = (pixel.red + pixelA.red + pixelB.red + pixelC.red) // 4
                avg_blue = (pixel.blue + pixelA.blue + pixelB.blue + pixelC.blue) // 4
                avg_green = (pixel.green + pixelA.green + pixelB.green + pixelC.green) // 4
            # Get pixel at the bottom-right corner of the image
            elif x == img.width - 1 and y == img.height - 1:
                pixelA = img.get_pixel(x, y - 1)
                pixelB = img.get_pixel(x - 1, y - 1)
                pixelC = img.get_pixel(x - 1, y)
                avg_red = (pixel.red + pixelA.red + pixelB.red + pixelC.red) // 4
                avg_blue = (pixel.blue + pixelA.blue + pixelB.blue + pixelC.blue) // 4
                avg_green = (pixel.green + pixelA.green + pixelB.green + pixelC.green) // 4
            # Get top edge's pixels (without two corners)
            elif y == 0:
                pixelA = img.get_pixel(x - 1, y)
                pixelB = img.get_pixel(x - 1, y + 1)
                pixelC = img.get_pixel(x, y + 1)
                pixelD = img.get_pixel(x + 1, y + 1)
                pixelE = img.get_pixel(x + 1, y)
                avg_red = (pixel.red + pixelA.red + pixelB.red + pixelC.red + pixelD.red + pixelE.red) // 6
                avg_blue = (pixel.blue + pixelA.blue + pixelB.blue + pixelC.blue + pixelD.blue + pixelE.blue) // 6
                avg_green = (pixel.green + pixelA.green + pixelB.green + pixelC.green + pixelD.green + pixelE.green) // 6
            # Get bottom edge's pixels (without two corners)
            elif y == img.height - 1:
                pixelA = img.get_pixel(x - 1, y)
                pixelB = img.get_pixel(x - 1, y - 1)
                pixelC = img.get_pixel(x, y - 1)
                pixelD = img.get_pixel(x + 1, y - 1)
                pixelE = img.get_pixel(x + 1, y)
                avg_red = (pixel.red + pixelA.red + pixelB.red + pixelC.red + pixelD.red + pixelE.red) // 6
                avg_blue = (pixel.blue + pixelA.blue + pixelB.blue + pixelC.blue + pixelD.blue + pixelE.blue) // 6
                avg_green = (pixel.green + pixelA.green + pixelB.green + pixelC.green + pixelD.green + pixelE.green) // 6
            # Get left edge's pixels (without two corners)
            elif x == 0:
                pixelA = img.get_pixel(x, y - 1)
                pixelB = img.get_pixel(x + 1, y - 1)
                pixelC = img.get_pixel(x + 1, y)
                pixelD = img.get_pixel(x + 1, y + 1)
                pixelE = img.get_pixel(x, y + 1)
                avg_red = (pixel.red + pixelA.red + pixelB.red + pixelC.red + pixelD.red + pixelE.red) // 6
                avg_blue = (pixel.blue + pixelA.blue + pixelB.blue + pixelC.blue + pixelD.blue + pixelE.blue) // 6
                avg_green = (pixel.green + pixelA.green + pixelB.green + pixelC.green + pixelD.green + pixelE.green) // 6
            # Get right edge's pixels (without two corners)
            elif x == img.width - 1:
                pixelA = img.get_pixel(x, y - 1)
                pixelB = img.get_pixel(x - 1, y - 1)
                pixelC = img.get_pixel(x - 1, y)
                pixelD = img.get_pixel(x - 1, y + 1)
                pixelE = img.get_pixel(x, y + 1)
                avg_red = (pixel.red + pixelA.red + pixelB.red + pixelC.red + pixelD.red + pixelE.red) // 6
                avg_blue = (pixel.blue + pixelA.blue + pixelB.blue + pixelC.blue + pixelD.blue + pixelE.blue) // 6
                avg_green = (pixel.green + pixelA.green + pixelB.green + pixelC.green + pixelD.green + pixelE.green) // 6
            else:
                pixelA = img.get_pixel(x - 1, y)
                pixelB = img.get_pixel(x + 1, y)
                pixelC = img.get_pixel(x - 1, y - 1)
                pixelD = img.get_pixel(x, y - 1)
                pixelE = img.get_pixel(x + 1, y - 1)
                pixelF = img.get_pixel(x - 1, y + 1)
                pixelG = img.get_pixel(x, y + 1)
                pixelH = img.get_pixel(x + 1, y + 1)
                avg_red = (pixel.red + pixelA.red + pixelB.red + pixelC.red + pixelD.red + pixelE.red + pixelF.red + pixelG.red + pixelH.red) // 9
                avg_blue = (pixel.blue + pixelA.blue + pixelB.blue + pixelC.blue + pixelD.blue + pixelE.blue + pixelF.blue + pixelG.blue + pixelH.blue) // 9
                avg_green = (pixel.green + pixelA.green + pixelB.green + pixelC.green + pixelD.green + pixelE.green + pixelF.green + pixelG.green + pixelH.green) // 9

            new_img_pixel.red = avg_red
            new_img_pixel.blue = avg_blue
            new_img_pixel.green = avg_green
    return new_img



def main():
    """
    Average pixels in all corners of the original image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
