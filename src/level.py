import pygame
import random

class Level:
	def __init__(self):
		self.speed=1
		self.matrix=[]
		self.all_tetriminos=[]
		self.control=""
		for a in range(0,22):
			self.matrix.append([])
			for b in range(0,10):
				self.matrix[a].append(0)
		self.generate_tetrimino()
		self.new_tetrimino()


	def generate_tetrimino(self):
		tetrimino=random.randint(0,6)
		if tetrimino==0: 
			blocks=[[(0,0), (0,1), (1,0), (1,1)]]
		if tetrimino==1: # T
			blocks=[[(0,1), (1,0), (1,1), (2,1)], [(0,0), (0,1), (0,2), (1,1)],
					[(0,0), (1,0), (1,1), (2,0)], [(0,1), (1,0), (1,1), (1,2)]]
		if tetrimino==2: # L
			blocks=[[(0,0), (0,1), (0,2), (1,0)], [(0,0), (1,0), (2,0), (2,1)],
					[(1,0), (1,1), (1,2), (0,2)], [(0,0), (0,1), (1,1), (2,1)]]
		if tetrimino==3: # J
			blocks=[[(0,0), (1,0), (1,1), (1,2)], [(2,0), (2,1), (1,1), (0,1)], 
					[(0,0), (0,1), (0,2), (1,2)], [(0,0), (0,1), (1,0), (2,0)]]
		if tetrimino==4: # I
			blocks=[[(0,1), (1,1), (2,1), (3,1)], [(1,0), (1,1), (1,2), (1,3)]]
		if tetrimino==5: # S
			blocks=[[(0,0), (1,0), (1,1), (2,1)], [(1,0), (1,1), (0,1), (0,2)]]
		if tetrimino==6: # Z
			blocks=[[(1,0), (2,0), (0,1), (1,1)], [(0,0), (0,1), (1,1), (1,2)]]
		self.all_tetriminos.append([tetrimino, blocks, (3 , 13), 0])


	def new_tetrimino(self):
		self.generate_tetrimino()
		self.all_tetriminos[-2][2]=(0,4)
		
	def controls(self):
		position=self.all_tetriminos[-2][2]
		if self.control=="left":
			newpos=position[0], position[1]-1
			print (self.intersects(newpos))
			if not self.intersects(newpos):
				self.all_tetriminos[-2][2]=newpos
			
			self.control=""

		if self.control=="down":
			newpos=position[0]+1, position[1]
			if self.intersects(newpos):
				self.new_tetrimino()
			else:
				self.all_tetriminos[-2][2]=newpos
			self.control=""

		if self.control=="right":
			newpos=position[0], position[1]+1     
			if not self.intersects(newpos):
				self.all_tetriminos[-2][2]=newpos
			self.control=""

		if self.control=="ccw":
			self.all_tetriminos[-2][1]
		# if self.control=="cw":
		#    self.all_tetriminos[-2]

		if self.control=="drop":  
			newpos=position[0]+1, position[1]
			for _ in range(22):
				if self.intersects(newpos)==False:
					self.control="down"
			self.control=""
			

	def intersects(self, position):
		tetrimino = self.all_tetriminos[-2].copy()
		tetrimino[2]=position
		for block in tetrimino[1][tetrimino[3]%len(tetrimino[1])]:
			if block[0]+tetrimino[2][0]>=22 or block[1]+tetrimino[2][1]>=10 or block[1]+tetrimino[2][1]<0:
				return True
		return False
