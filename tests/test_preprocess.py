import unittest
from PIL import Image, ImageDraw
import numpy as np
import os
import sys

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import preprocess_canvas_image


class TestDigitPreprocessor(unittest.TestCase):
    def test_blank_canvas_returns_none(self):
        # White image (blank)
        img = Image.new("L", (280, 280), "white")
        result = preprocess_canvas_image(img)
        self.assertIsNone(result)

    def test_drawn_digit_returns_correct_shape_and_range(self):
        # White image with black line drawn in the center
        img = Image.new("L", (280, 280), "white")
        draw = ImageDraw.Draw(img)
        draw.line([(100, 50), (100, 200)], fill="black", width=18)

        result = preprocess_canvas_image(img)
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, (1, 28, 28, 1))
        self.assertTrue((result >= 0.0).all())
        self.assertTrue((result <= 1.0).all())
        # Make sure center has non-zero pixel intensity
        self.assertTrue(result.max() > 0.5)


if __name__ == '__main__':
    unittest.main()
