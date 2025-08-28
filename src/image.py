
global changed_image

import skimage
import numpy as np

class image_array:
    """
    Class to hold a pixel matrix
    """

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

        # NOTE
        # Image returns transposed in numpy

        x_coords, y_coords= np.meshgrid(
            np.arange(self.width), 
            np.arange(self.height), 
            indexing="ij"
            )

        pixels = np.column_stack((
            x_coords.ravel(), 
            y_coords.ravel(), 
            image.reshape(-1, color)
            ))

        pixels_list = pixels
        self.data = pixels_list

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

        index = y + (x * self.height)
        return self.data[index]
        
    def set_point(self, x:int, y:int, r:int, g:int, b:int) -> None:
        global changed_image
        changed_image = True
        self.data[(x*self.height) + y][2:5] = [r,g,b]
        return None

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

    def save(self, path) -> None:
        skimage.io.imsave(path, self.data, check_contrast=False)
        return

    def __get_index(self, x:int, y:int) -> int:
        
        # using a 2x2 table as an example for the calculation:
        # | x | y | formula | value
        # | 0 | 0 | 0 + (0 * 2) | 0
        # | 1 | 0 | 1 + (0 * 2) | 1
        # | 0 | 1 | 0 + (1 * 2) | 2
        # | 1 | 1 | 1 + (1 * 2) | 3

        index = x + (y * self.width)


