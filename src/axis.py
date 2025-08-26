"""
Module to scan each axis for organoid borders
"""

import skimage.io
from get_pixels import get_pixel_matrix

print("hello world")

def scan(image, threshold):
    """
    given an image, and a r+g+b threshold, 
    return the outline of the image
    """
    
    for line in image




    return data

if __name__ == "__main__":

    test_image = "../data/Donor 3, Mock, 24hr, Slide 8, 5x_ch00.tif"

    image = get_pixel_matrix(test_image)

    width = image[-1][0] + 1
    height = image[-1][1] + 1

    x = 0
    y = 0
    data = [[] for y in range(height)]

    for pixel in image:
        x = pixel[0]
        y = pixel[1]
        data[y].append(pixel[2:5])
        # data.append(pixel[2:5])
    del image
