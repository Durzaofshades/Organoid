
import skimage.io as skimage
import numpy as np

class image_array:
    """
    Class to hold a pixel matrix
    """

    def __init__(self, path:str) -> None:
        # Initialize variables
        self.data = []

        # Returns Nested Lists
        image = skimage.imread(path)

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

        return self.data[y + x * self.height]
    
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
