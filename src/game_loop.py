import pygame
import sys

class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, scale):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._scale = scale

    def start(self):
        while True:
            gravity=pygame.time.set_timer(25, int(1000/self._level.speed))
            self.go_throught_events()
            self._renderer.render()
            self._level.controls()




    def go_throught_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    control="left"
                if event.key == pygame.K_RIGHT:
                    control="right"
                if event.key == pygame.K_SPACE:
                    self._level.drop()
                if event.key == pygame.K_DOWN:
                    control="down"
                if event.key == pygame.K_UP:
                    self._level.all_tetriminos[-2][3]+=1
                    
                    #rotating clockwise and counter-clockwise
                if event.key == pygame.K_a:
                    control="countercw"
                if event.key == pygame.K_d:
                    control="cw"

            if event.type == 25:
                self._level.all_tetriminos[-2][2]=self._level.all_tetriminos[-2][2][0]+1, self._level.all_tetriminos[-2][2][1]
