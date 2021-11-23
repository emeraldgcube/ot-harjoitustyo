import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.new_game()
        self.scale=30
        self.screen_width=26*self.scale
        self.screen_height=22*self.scale
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))  
        self.clock=pygame.time.Clock()
        # position: 1 - menu  2 - game  3 - end screen 4 - hiscore
        self.position=2
        self.newdir=""

        self.loop()

        
        
    def new_game(self):
        pygame.display.set_caption("Tetris") 
        self.all_tetriminos=[]
        self.speed=1
        self.new_tetrimino()
        self.score=0

    def loop(self):
        while True:
            self.go_throught_events()
            self.movement()
            self.draw_screen()
            print(self.all_tetriminos)
 
    def go_throught_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.newdir="left"
                if event.key == pygame.K_RIGHT:
                    self.newdir="right"
                if event.key == pygame.K_SPACE:
                    self.drop()
                if event.key == pygame.K_DOWN:
                    self.newdir="down"


    def new_tetrimino(self):
        self.generate_tetrimino()
        self.all_tetriminos[-1][2]=(0,5)


    def drop(self):
        #tiputa
        honda=1

    def generate_tetrimino(self):
        tetrimino=random.randint(0,6)
        if tetrimino==0:
            blocks=[(0,0), (0,1), (1,0), (1,1)]
        if tetrimino==1:
            blocks=[(0,1), (1,0), (1,1), (2,1)]
        if tetrimino==2:
            blocks=[(0,0), (0,1), (0,2), (1,0)]
        if tetrimino==3:
            blocks=[(0,0), (1,0), (1,1), (1,2)]
        if tetrimino==4:
            blocks=[(0,0), (1,0), (2,0), (3,0)]
        if tetrimino==5:
            blocks=[(0,0), (1,0), (1,1), (2,1)]
        if tetrimino==6:
            blocks=[(1,0), (0,1), (1,1), (2,1)]
        self.all_tetriminos.append([tetrimino, blocks, None])

    def movement(self):
        if self.newdir=="left":
            self.all_tetriminos[-1][2][1]-=1
        

        
    def draw_screen(self):
        self.window.fill((0, 0, 0))
        if self.position==2:
            for tetrimino in self.all_tetriminos:
                if tetrimino[0]==0:
                    color=255, 0, 0
                if tetrimino[0]==1:
                    color=0, 255, 0
                if tetrimino[0]==2:
                    color=0, 0, 255
                if tetrimino[0]==3:
                    color=255, 255, 0
                if tetrimino[0]==4:
                    color=255, 0, 255
                if tetrimino[0]==5:
                    color=0, 255, 255
                if tetrimino[0]==6:
                    color=100, 100, 255
                for block in tetrimino[1]:
                    y=block[0]*self.scale+8*self.scale
                    x=block[1]*self.scale+2*self.scale

                    pygame.draw.rect(self.window, color, pygame.Rect(y, x, self.scale, self.scale))
            
        pygame.display.flip()

Game()


# Peli tällä hetkellä printtaa yksittäisen palikan: seuraavana vuorossa varsinainen pelilogiikka ja kenttään kunnolla sijoittaminen.
