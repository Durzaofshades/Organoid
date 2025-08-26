"""
Module to scan each axis for organoid borders
"""

from image import image_array

print("hello world")

def scan(image, threshold) -> image_array:
    """
    given an image, and a r+g+b threshold, 
    return the outline of the image
    """
    
    data = [[pixel[0], pixel[1], sum(pixel[2:5])] for pixel in image.data]

    return data

if __name__ == "__main__":

    test_image = "../data/Donor 3, Mock, 24hr, Slide 8, 5x_ch00.tif"
    image = image_array(test_image)
    outline = scan(image, 150)
