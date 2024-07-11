"""
Tests for the Image class.
"""

import os

import pytest

from ms_image_tool.image import Image


class TestImage:
    """
    Test methods for the Image class.
    """

    @pytest.fixture
    def image(self):
        """
        Image object fixture. Loads an Image object to use in other tests.
        """
        return Image("data/sample/sample-image.tif")

    def test_invalid_file(self):
        """
        Tests that an error is raised when an invalid file is provided.
        """
        with pytest.raises(ValueError):
            Image("data/sample/sample-image.jpg")

    def test_valid_file(self, image):
        """
        Tests that the sample image was loaded correctly.
        """
        assert os.path.isfile(image.path)

    def test_sample_dimensions(self, image):
        """
        Tests that the sample image has the correct dimensions.
        """
        assert image.height == 500
        assert image.width == 500
        assert image.shape == (500, 500)
        assert image.red.shape == (500, 500)
        assert image.green.shape == (500, 500)
        assert image.blue.shape == (500, 500)
        assert image.rededge.shape == (500, 500)
        assert image.nir.shape == (500, 500)
