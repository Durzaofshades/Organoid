
import math
from math import sqrt, acos, cos, sin, pow

def circle(x0,y0,radius, verbose = False) -> list:
    """
    Outputs a list of circular coordinates for a given radius
    """

    x1 = x0 - radius
    x2 = x0 + radius
    y1 = y0 - radius
    y2 = y0 + radius

    pixels = []

    in_circle = True

    if verbose:
        print(f"{x1} -> {x2}")
        print(f"{y1} -> {y2}")
    
    pi = math.pi

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            p = (i,j)
            
            distance = sqrt(pow(i,2) + pow(j,2))

            try: theta = acos(i / distance)
            except: theta = 0

            if j < 0: theta = theta + pi

            circle_x = cos(theta)
            circle_y = sin(theta)
    
            if verbose:
                text = ""
                text += f"({i},{j})\n"
                text += f"\tx = {i}\n"
                text += f"\ty = {j}\n"
                text += f"\tdistance = {distance:.2f}\n" 
                text += f"\tangle = {theta*12/pi:.2f}/12 radians\n"
                print(text)

            if distance <= radius:
                pixels.append(p)

    return pixels

if __name__ == "__main__":
    print(circle(0,0,1))
    print(circle(0,0,2))

            
