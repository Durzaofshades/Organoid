#!/bin/python

import matplotlib.pyplot as plt
import numpy as np

from image import ImageArray

def color_type_graph(image_path, annotation_path):
    """
    given an image and an annotated image
    """

    image = ImageArray(image_path)
    annotation = ImageArray(annotation_path)

    nucleated = []

    cells = 0

    for y in range(annotation.height):
        for x in range(annotation.width):
            pixel = annotation.get_point(x,y)
            test = False
            if pixel[2:5] == [255,255,255]:
                test = True
                cells += 1

            nucleated.append(test)
    nucleated = np.array(nucleated, dtype = bool)
    data = list(image.data)
    data.append(nucleated)
    #image.data = np.array(data)

    data = np.array(data).T
    print(data)

    # x, y, r, g, b, n = image.data

    d1 = np.array([row for row in data if row[5] == False]).T
    d2 = np.array([row for row in data if row[5] == True]).T

    print(d1)

    s = 4

    plt.scatter(d1[2],d1[3], s=s)
    plt.scatter(d2[2],d2[3], s=s)
    plt.title("Nucleated Cells Red vs Green Values")
    plt.xlabel("R Values")
    plt.ylabel("G Values")
    plt.legend( ["Non-Nucleated Cells", "Nucleated Cell Annotations"], loc="lower right")
    plt.savefig("../data/test/Nucleated-RG.png")

    plt.close()

    plt.scatter(d1[2],d1[4], s=s)
    plt.scatter(d2[2],d2[4], s=s)
    plt.title("Nucleated Cells Red vs Blue Values")
    plt.xlabel("R Values")
    plt.ylabel("B Values")
    plt.legend( ["Non-Nucleated Cells", "Nucleated Cell Annotations"], loc="lower right")
    plt.savefig("../data/test/Nucleated-RB.png")

    plt.close()

    w1 = [1/len(d1[2])] * len(d1[2])
    w2 = [1/len(d2[2])] * len(d2[2])

    print(len(w1))
    print(len(d1[2]))

    plt.hist(
            x = [d1[2], d2[2]], 
            bins=64, 
            weights = [w1,w2],
            stacked=True, 
            density = True
            #color=['cyan', 'Purple']
            # edgecolor='black'
        )
    plt.title("Nucleated Cells Red Color Channel")
    plt.xlabel("Red Values")
    plt.legend( ["Non-Nucleated Cells", "Nucleated Cell Annotations"], 
               loc="upper left")
    plt.savefig("../data/test/Nucleated-R.png")

    plt.close()

    plt.hist(
            x = [d1[3], d2[3]], 
            bins=64, 
            weights = [w1,w2],
            stacked=True, 
            density = True
            #color=['cyan', 'Purple']
            # edgecolor='black'
        )
    plt.legend( ["Non-Nucleated Cells", "Nucleated Cell Annotations"], 
               loc="upper left")
    plt.title("Nucleated Cells Blue Channel")
    plt.xlabel("Blue Values")
    plt.savefig("../data/test/Nucleated-B.png")

    plt.close()

    plt.hist(
            x = [d1[4], d2[4]], 
            bins=64, 
            weights = [w1,w2],
            stacked=True, 
            density = True
            #color=['cyan', 'Purple']
            # edgecolor='black'
        )
    plt.legend( ["Non-Nucleated Cells", "Nucleated Cell Annotations"], 
               loc="upper left")
    plt.title("Nucleated Cells Green Channel")
    plt.xlabel("Green Values")
    plt.savefig("../data/test/Nucleated-G.png")

    plt.close()

    plt.hist(
            x = [image.data[2]], 
            bins=64, 
            stacked=True, 
            density = True
            # color=['cyan', 'Purple']
            # edgecolor='black'
        )
    plt.title("Organoid Red Color Channel")
    plt.xlabel("Red Values")
    plt.savefig("../data/test/Organoid-R.png")

if __name__ == "__main__":
    f1 = "../data/test/original.png"
    f2 = "../data/test/N-Cell.png"
    color_type_graph(f1,f2)
