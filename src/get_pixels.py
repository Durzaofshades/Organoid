"""
Module to create a pixel matrix from an image
"""

import numpy as np
from skimage.io import imread

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

# quick test
def test():
    test_matrix = get_pixel_matrix("../data/Skin Organoids (tif)/5x/Donor 3, Candin, 12hr, Slide 8, 5x_ch00.tif")
    print(test_matrix)
    print(type(test_matrix))
