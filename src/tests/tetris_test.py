import unittest
from tetris import Game

class TestBlock(unittest.TestCase):
	def setUp(self):
	    game=Game()

	def test_block_moves(self):
	    self.assertNotEqual(game.all_tetriminos, None)
