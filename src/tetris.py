import random
import pygame

class Game:
    #initalizement settings
    def __init__(self):
        pygame.init()
        self.new_game()
        self.scale=30
        self.screen_width=26*self.scale
        self.screen_height=22*self.scale
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock=pygame.time.Clock()
        self.position=2
        self.control=""
        self.time1=0
        self.rotation=0
        #self.collision=False
        self.matrix=[]
        self.gravity=pygame.time.set_timer(25, int(1000/self.speed))
        self.loop()

        #starts a new game
    def new_game(self):
        pygame.display.set_caption("Tetris")
        self.all_tetriminos=[]
        self.speed=1
        self.generate_tetrimino()
        self.new_tetrimino()
        self.score=0

        #does this part throughout
    def loop(self):
        while True:
            self.go_throught_events()
            self.controls()
            self.draw_screen()

        #check for keystrokes
    def go_throught_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.control="left"
                if event.key == pygame.K_RIGHT:
                    self.control="right"
                if event.key == pygame.K_SPACE:
                    self.drop()
                if event.key == pygame.K_DOWN:
                    self.control="down"
                if event.key == pygame.K_UP:
                    self.all_tetriminos[-2][3]+=1

                    #rotating clockwise and counter-clockwise
                if event.key == pygame.K_a:
                    self.control="countercw"
                if event.key == pygame.K_d:
                    self.control="cw"


            if event.type == 25:
                self.all_tetriminos[-2][2]=self.all_tetriminos[-2][2][0]+1, self.all_tetriminos[-2][2][1]

        #new block on the game field
    def new_tetrimino(self):
        self.generate_tetrimino()
        self.all_tetriminos[-2][2]=(0,4)

        #logic of falling
    #def gravity(self):

   # def check_for_collision(self):
  #      for a in range(0,4):
 #           for b in range (0,4):
#                f=3

        #generates new block for queue
    def generate_tetrimino(self):
        tetrimino=random.randint(0,6)
        if tetrimino==0: # cube
            blocks=[[(0,0), (0,1), (1,0), (1,1)]]
        if tetrimino==1: # T
            blocks=[[(0,1), (1,0), (1,1), (2,1)], [(0,0), (0,1), (0,2), (1,1)], [(0,0), (1,0), (1,1), (2,0)], [(0,1), (1,0), (1,1), (1,2)]]
        if tetrimino==2: # L
            blocks=[[(0,0), (0,1), (0,2), (1,0)], [(0,0), (1,0), (2,0), (2,1)], [(1,0), (1,1), (1,2), (0,2)], [(0,0), (0,1), (1,1), (2,1)]]
        if tetrimino==3: # J
            blocks=[[(0,0), (1,0), (1,1), (1,2)], [(2,0), (2,1), (1,1), (0,1)], [(0,0), (0,1), (0,2), (1,2)], [(0,0), (0,1), (1,0), (2,0)]]
        if tetrimino==4: # I
            blocks=[[(0,0), (1,0), (2,0), (3,0)], [(1,0), (1,1), (1,2), (1,3)]]
        if tetrimino==5: # S
            blocks=[[(0,0), (1,0), (1,1), (2,1)], [(1,0), (1,1), (0,1), (0,2)]]
        if tetrimino==6: # Z
            blocks=[[(1,0), (2,0), (0,1), (1,1)], [(0,0), (0,1), (1,1), (1,2)]]
        self.all_tetriminos.append([tetrimino, blocks, (3 , 13), 0])
                                #  blocktypes, blocks, location, rotation
                                #  x and y   ,

        #how the player can move the block
    def controls(self):
        position=self.all_tetriminos[-2][2]
        if self.control=="left":
            self.all_tetriminos[-2][2]=position[0], position[1]-1
            self.control=""

        if self.control=="down":
            self.all_tetriminos[-2][2]=position[0]+1, position[1]
            self.control=""
            print(self.all_tetriminos)

        if self.control=="right":
            self.all_tetriminos[-2][2]=position[0], position[1]+1
            self.control=""

        if self.control=="ccw":
            self.all_tetriminos[-2][1]
       # if self.control=="cw":
        #    self.all_tetriminos[-2]

        #screen draw
    def draw_screen(self):
        self.window.fill((0, 0, 0))
        pygame.draw.rect(self.window, (15, 15, 155), [int(7.4*self.scale), 0, int(self.scale*0.6), 22*self.scale])
        pygame.draw.rect(self.window, (15, 15, 155), [int(18*self.scale), 0, int(self.scale*0.6), 22*self.scale])
        pygame.draw.rect(self.window, (0, 255, 0), [0, 0, self.scale*7.4, self.scale*22])
        pygame.draw.rect(self.window, (0, 255, 0), [int(18.6*self.scale), 0, self.scale*7.4, self.scale*22])
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
                for block in tetrimino[1][tetrimino[3]%len(tetrimino[1])]:
                    #field is supposed to start at (8,-2)
                    y=block[0]*self.scale+2*self.scale+self.scale*tetrimino[2][0]
                    x=block[1]*self.scale+8*self.scale+self.scale*tetrimino[2][1]
                    pygame.draw.rect(self.window, color, pygame.Rect(x, y, self.scale, self.scale))
            
        pygame.display.flip()

Game()