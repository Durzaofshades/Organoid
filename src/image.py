
global changed_image

import skimage
import numpy as np
import matplotlib.pyplot as pyplot

class image_array:
    """
    Class to hold a pixel matrix


    data[0] = x
    data[1] = y
    data[2] = r
    data[3] = g
    data[4] = b
    data[5] = nucleated
    """
    #
    #
    #
    #
    #
    #
    

    def __init__(self, path:str) -> None:
        global changed_image
        changed_image = False
        # Initialize variables
        self.data = []

        # Returns Nested Lists
        image = skimage.io.imread(path)

        # Transform to xy, rgb
        self.height = image.shape[0]
        self.width  = image.shape[1]
        color       = image.shape[2]

        y_coords, x_coords = np.meshgrid(
            np.arange(self.height),
            np.arange(self.width),
            indexing="ij"
        )

        pixels = np.column_stack((
            x_coords.ravel(),
            y_coords.ravel(),
            image.reshape(-1, color)
            ))

        x = []
        y = []
        r = []
        g = []
        b = []

        for row in pixels:
            x.append(row[0])
            y.append(row[1])
            r.append(row[2])
            g.append(row[3])
            b.append(row[4])

        # Colors should be uint8 (0-255)
        r = np.array(r, dtype = np.uint8)
        g = np.array(g, dtype = np.uint8)
        b = np.array(b, dtype = np.uint8)

        # TODO
        # empty array for Nucleated Cells
        # empty array for Neighbor Annotations

        self.data = np.array([x,y,r,g,b])

    def __str__(self) -> str:
        return str(self.data)

    def get_point(self, x:int, y:int) -> list[int]:
        """
        random access for a specific point
        """
        # TODO make this the array index operation

        if x >= self.width:
            raise Exception(f"Out of Bounds error, {x} > {self.width -1}")

        if y >= self.height:
            raise Exception(f"Out of Bounds error, {y} > {self.height -1}")

        index = self.get_index(x,y)
        point = [0] * 5

        point[0] = self.data[0][index]
        point[1] = self.data[1][index]
        point[2] = self.data[2][index]
        point[3] = self.data[3][index]
        point[4] = self.data[4][index]
        
        return point

    def set_point(self, x:int, y:int, r:int, g:int, b:int) -> None:
        global changed_image
        changed_image = True

        index = self.get_index(x,y)

        self.data[0][index] = x
        self.data[1][index] = y
        self.data[2][index] = r
        self.data[3][index] = g
        self.data[4][index] = b

        return None

    def set_attribute(self, x: int, y: int, attribute: int, value):
        global changed_image
        changed_image = True

        index = self.get_index(x,y)
        self.data[attribute][index] = value

    def get_row(self, index) -> list:
        data = []
        for x in range(self.width):
            data.append(self.get_point(x, index))
        return data

    def get_column(self, index) -> list:
        data = []
        for y in range(self.height):
            data.append(self.get_point(index, y))
        return data

    def save_image(self, path) -> None:
        skimage.io.imsave(path, self.data, check_contrast=False)
        return

    def get_index(self, x:int, y:int) -> int:
        """
        Caluclated the Row index of any given pixel
        """

        # caluclates row index
        # using a 2x2 table as an example for the calculation:
        # | x | y | formula | value
        # | 0 | 0 | 0 + (0 * 2) | 0
        # | 1 | 0 | 1 + (0 * 2) | 1
        # | 0 | 1 | 0 + (1 * 2) | 2
        # | 1 | 1 | 1 + (1 * 2) | 3

        # index = x + (y * self.width)
        index = y + (x * self.height)

        assert(type(index) is int)
        return index

    def show(self) -> None:
        pixels = self.data.T

        width = int(pixels[:, 0].max()) + 1
        height = int(pixels[:, 1].max()) + 1

        image = np.zeros((height, width, 3), dtype=np.uint8)

        x = pixels[:, 0].astype(int)
        y = pixels[:, 1].astype(int)
        rgb = pixels[:, 2:5].astype(np.uint8)
        image[y, x] = rgb

        # Show image
        pyplot.imshow(image)
        pyplot.axis("off")
        pyplot.show()

    def print(self, *, amount: int = 100) -> None:
        """
        use amount=None to print the whole array
        """

        length = self.height * self.width
        length = min(length, amount)

        for row in range(length):
            x = self.data[0][row]
            y = self.data[1][row]
            r = self.data[2][row]
            g = self.data[3][row]
            b = self.data[4][row]

            print(f"({x},{y}) -> ({r}, {g}, {b})")
        return None

    def annotate_neighbors(self) -> None:
        """
        Given a Radius, annotate each pixel with the average pixel value for that radius
        """

        # For Radius = 1
        Radius = 1
        
        for pixel in self.data:
            x = pixel[0]
            y = pixel[1]

            # Get each circular value

            # Check width and height out of bounds error
        


