import unittest
from models.tone import Tone


class TestTone(unittest.TestCase):
    def setup(self):
        return Tone(98.6)  # works! done.
        pass

if __name__ == '__main__':
    unittest.main()