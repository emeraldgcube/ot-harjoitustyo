import unittest
from tetris import Game

class TestBlock(unittest.TestCase):
	def setUp(self):
	    print("Setup")

	def test_block_moves(self):
	    self.assertNotEqual(self.all_tetriminos, None)
