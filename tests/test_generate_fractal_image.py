import unittest
import numpy as np
from fractal_image_generator import generate_fractal_image

class TestFractalGeneration(unittest.TestCase):
    def test_generate_fractal_image(self):
        D = np.random.uniform(1.0, 2.0)
        depth = np.random.randint(1, 11)
        img = generate_fractal_image(D=D, depth=depth)
        width = 2**depth
        self.assertEqual(img.shape[0], width)
        self.assertEqual(img.shape[1], width)
        self.assertEqual(img.shape[0], img.shape[1])


if __name__ =='__main__':
    unittest.main()