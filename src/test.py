#!/bin/python

"""
Module to test functions
"""

import sys
import numpy

from image import image_array

def test_get_point(image) -> bool:
    x = 100
    y = 200
    point = image.get_point(x,y)
    fail = False
    print(point)
    if point[0] != x or point[1] != y:
        fail = True
        print(point)

    return not fail

def test_image_axis(image, width, height) -> bool:
    x = image.width
    y = image.height
    print(f"Image (x,y) Dimensions are {x,y}")
    # Test image is 1280x960
    return (x,y) == (width, height)

def test_get_array(image) -> bool:
    fail = False

    print(str(image))
    datatype = type(image.data)
    print(datatype)
    if datatype != numpy.ndarray:
        fail = True

    return not fail

def test_get_row(image) -> bool:
    fail = False

    row = image.get_row(0)
    x = row[0][0]
    y = row[0][1]
    if x != 0 or y != 0:
        fail = True
    return not fail

if __name__ == "__main__":
    path = "../data/Skin Organoids (tif)/5x/Donor 3, Candin, 12hr, Slide 8, 5x_ch00.tif"
    image = image_array(path)
    
    axis = test_image_axis(image, 1280, 960)
    point = test_get_point(image)
    array = test_get_array(image)
    row = test_get_row(image)
    
    success = all([axis, point, array, row])
    
    # TODO print each tests value
    print(f"Axis test status: {axis}")
    print(f"Point test status: {point}")
    print(f"Array test status: {array}")
    print(f"Row test status: {row}")

    if success:
        print("All Tests Passed")
        sys.exit(0)
    else:
        print("Tests Failed")
        sys.exit(1)
