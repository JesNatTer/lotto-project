import unittest
from functionstotest import TestFunctions


class TestLotto(unittest.TestCase):
    def test_lotto_game(self):
        lottogame = TestFunctions()
        self.assertEqual(1, lottogame.lotto([1,2,3], [1,3,5]),
                         "With one identical item in two lists, count should equal 1")
