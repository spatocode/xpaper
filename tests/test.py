import os
import unittest
from xpaper import wallpaper

class TestXpaper(unittest.TestCase):

    def test_get_wallpaper(self):
        self.assertTrue(wallpaper.get(), "Should return wallpaper path")

    def test_change_wallpaper(self):
        image = os.path.join(os.getcwd(), "test_image.png")
        self.assertFalse(wallpaper.change(image), "Should return nothing")
        self.assertEqual(wallpaper.get(), image, "Should return test image path")

if __name__ == '__main__':
    unittest.main()
