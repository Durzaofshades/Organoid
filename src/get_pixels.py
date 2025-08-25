"""
Module to create a pixel matrix from an image
"""

import sys
import skimage

def get_pixel_matrix(path):
    """
    Helper Function to get a pixel matrix
    """

    data = skimage.io.imread(path)
    return data
