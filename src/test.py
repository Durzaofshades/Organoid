#!/bin/python

"""
Module to test functions
"""

import sys
import numpy

from image import image_array

def test_get_point(image, x, y) -> bool:
    fail = False
    try:
        point = image.get_point(x,y)
    except IndexError:
        fail = True
        print(f"Index Error: Failure to get point at ({x}, {y})")
        return not fail

    if not noprint:
        print(point)

    if point[0] != x or point[1] != y:
        fail = True
        print(point)

    return not fail

def test_set_point(image) -> bool:
    """
    test set point function
    depends on the get point function
    """
    fail = False
    x = 100
    y = 200

    # Get original point
    p1 = image.get_point(x,y)
    image.set_point(x,y, 0, 255, 0)
    
    # Get new point
    p2 = image.get_point(x,y)
    if p2[2] != 0 or p2[3] != 255 or p2[4] != 0:
        fail = True
        print(p2)

    # Set it back to normal
    image.set_point(x,y, p1[2], p1[3], p1[4])

    return not fail

def test_image_axis(image, width, height) -> bool:
    x = image.width
    y = image.height
    if not noprint:
        print(f"Image (x,y) Dimensions are {x,y}")
    # Test image is 1280x960
    return (x,y) == (width, height)

def test_get_array(image) -> bool:
    fail = False

    datatype = type(image.data)

    if not noprint:
        print(str(image))
        print(datatype)

    for column in image.data:
        print(column.dtype)

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
    global noprint

    # if -noprint is passed in as an argument, don't print NORMAL prints
    # still print test failure error messages
    if "-noprint" in sys.argv:
        noprint = True
    else:
        noprint = False

    path = "../data/Skin Organoids (tif)/5x/Donor 3, Candin, 12hr, Slide 8, 5x_ch00.tif"
    image = image_array(path)

    get_point_first = test_get_point(image, 0, 0)
    get_point_middle = test_get_point(image, int(image.width/2), int(image.height/2))
    get_point_last = test_get_point(image, image.width-1, image.height-1)
    
    axis = test_image_axis(image, 1280, 960)
    set_point = test_set_point(image)
    array = test_get_array(image)
    row = test_get_row(image)
    
    success = all([
        axis, 
        get_point_first, 
        get_point_middle, 
        get_point_last, 
        set_point, 
        array, 
        row
        ])
    
    # TODO print each tests value
    print(f"Axis test status: {axis}")
    print(f"Get First Point test status: {get_point_first}")
    print(f"Get Middle Point test status: {get_point_middle}")
    print(f"Get Last Point test status: {get_point_last}")
    print(f"Set Point test status: {set_point}")
    print(f"Array test status: {array}")
    print(f"Row test status: {row}")

    # Print section
    print(f"Length = {len(image.data[0])}")
    
    out = open("test.csv", "w")
    sep = ",\t"
    for x in range(len(image.data[0])):
        text = ""
        text += str(image.data[0][x]) + sep
        text += str(image.data[1][x]) + sep
        text += str(image.data[2][x]) + sep
        text += str(image.data[3][x]) + sep
        text += str(image.data[4][x]) + "\n"
        out.write(text)


    if success:
        print("All Tests Passed")
        sys.exit(0)
    else:
        print("Tests Failed")
        sys.exit(1)
