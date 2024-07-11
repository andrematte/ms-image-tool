"""
# ---------------------------------------------------------------------------- #
#                           Multispectral Image Class                          #
# ---------------------------------------------------------------------------- #
"""

import numpy as np
import tifffile


class Image:
    """
    This class is used to represent a five-band multispectral image object.

    """

    def __init__(self, input_path: str) -> None:
        """
        The bands should be ordered as follows:

        1. Red (R)
        2. Green (G)
        3. Blue (B)
        4. Red Edge (RE)
        5. Near Infrared (NIR)
        6. Cutline (optional)

        Parameters:
            input_path (str): Path to the .tiff file.

        """
        self.path = input_path
        tensor = self._load_tiff(input_path)

        self.height = tensor.shape[0]
        self.width = tensor.shape[1]
        self.shape = (self.height, self.width)

        self.red = self._correct_bands(tensor[:, :, 0])
        self.green = self._correct_bands(tensor[:, :, 1])
        self.blue = self._correct_bands(tensor[:, :, 2])
        self.rededge = self._correct_bands(tensor[:, :, 3])
        self.nir = self._correct_bands(tensor[:, :, 4])

    def _load_tiff(self, input_path: str) -> np.ndarray:
        """
        Load an image from a .tiff file and return it as a numpy array.

        Parameters:
            input_path (str): Path to the .tiff file.
        """
        possible_extensions = ["tiff", "tif"]
        extension = input_path.split(".")[-1]

        if extension not in possible_extensions:
            raise ValueError("Invalid file extension. Please provide a .tiff file.")

        return tifffile.imread(input_path)

    def _correct_bands(self, tensor: np.ndarray) -> np.ndarray:
        """
        Correct values in the input tensor to be within the range of 0-1.

        Parameters:
            tensor (np.ndarray): Single band of the input image.
        """
        tensor[np.where(tensor > 1)] = 1
        tensor[np.where(tensor < 0)] = 0
        return tensor
