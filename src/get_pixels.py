"""
Module to create a pixel matrix from an image
"""

import numpy as np
from skimage.io import imread
from image import image_matrix

def get_pixel_matrix(path):
    """
    Helper Function to get a pixel matrix
    """
    # Returns nested lists
    data = imread(path)
    # Transforms to x, y, R, G, B
    h, w, c = data.shape
    y_coords, x_coords = np.meshgrid(np.arange(h), np.arange(w), indexing="ij")
    pixels = np.column_stack((x_coords.ravel(), y_coords.ravel(), data.reshape(-1, c)))
    pixels_list = pixels.tolist()
    return pixels_list

# if this file is ran by itself, run this
if __name__ == "__main__":
    test_image = "../data/Donor 3, Candin, 12hr, Slide 8, 5x_ch00.tif"
    test_matrix = image_matrix(test_image)
    print(str(test_matrix))
    print(type(test_matrix.data))
