"""
Module to scan each axis for organoid borders
"""

from image import image_array

def scan(image, threshold) -> None:
    """
    given an image, and a r+g+b threshold, 
    return the outline of the image
    (outline is the leftmost and rightmost point that pass the threshold
    """

    height = image.height - 1
    width = image.width - 1

    color = (0,255,0,)
    r = color[0]
    g = color[1]
    b = color[2]
    
    for y in range(0, height, 1):
        for x in range(0, width):
            # Checking Left Side
            point = image.get_point(x,y)
            if sum(point[2:5]) > threshold:
                image.set_point(x,y,r,g,b)
                break
        for x in range(width, 0, -1):
            # Checking from Right Side
            point = image.get_point(x,y)
            if sum(point[2:5]) > threshold:
                image.set_point(x,y,r,g,b)
                break
    return None

if __name__ == "__main__":
    test_image = "../data/Skin Organoids (tif)/5x/Donor 3, Mock, 24hr, Slide 8, 5x_ch00.tif"
    test_path = "../data/test/"
    image = image_array(test_image)
    
    #outline = scan(image, 150)
    # image.save(f"{test_path}outline.png")
    image.show()
