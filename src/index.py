import pygame
from tetris import Game
def main():
    pygame.init()
    self.new_game()
    self.scale=30
    self.screen_width=26*self.scale
    screen_height=22*self.scale
    window = pygame.display.set_mode((self.screen_width, self.screen_height))
    self.clock=pygame.time.Clock()
    self.position=2
    self.control=""
    self.time1=0
    self.rotation=0
    self.matrix=[]
    for a in range(0,22):
        self.matrix.append([])
        for b in range(0,10):
            self.matrix[a].append(0)
    #self.collision=False
    self.gravity=pygame.time.set_timer(25, int(1000/self.speed))
    self.loop()















































    def go_throught_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

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
