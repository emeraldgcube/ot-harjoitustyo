import pygame
from pygame import display

class Renderer:
    def __init__(self, display, level, scale):
        self._display = display
        self._level = level
        self._scale = scale

    def render(self):
        self._display.fill((0, 0, 0))
        pygame.draw.rect(self._display, (15, 15, 155),
                         [int(7.4*self._scale), 0, int(self._scale*0.6), 22*self._scale])
        pygame.draw.rect(self._display, (15, 15, 155),
                         [int(18*self._scale), 0, int(self._scale*0.6), 22*self._scale])
        pygame.draw.rect(self._display, (0, 255, 0),
                         [0, 0, self._scale*7.4, self._scale*22])
        pygame.draw.rect(self._display, (0, 255, 0),
                         [int(18.6*self._scale), 0, self._scale*7.4, self._scale*22])

        for tetrimino in self._level.all_tetriminos:
            if tetrimino[0] == 0:
                color = 255, 0, 0
            if tetrimino[0] == 1:
                color = 0, 255, 0
            if tetrimino[0] == 2:
                color = 0, 0, 255
            if tetrimino[0] == 3:
                color = 255, 255, 0
            if tetrimino[0] == 4:
                color = 255, 0, 255
            if tetrimino[0] == 5:
                color = 0, 255, 255
            if tetrimino[0] == 6:
                color = 100, 100, 255
            for block in tetrimino[1][tetrimino[3]%len(tetrimino[1])]:
                #field is supposed to start at (8,-2)
                y_coord = block[0]*self._scale+self._scale*tetrimino[2][0]
                x_coord = block[1]*self._scale+8*self._scale+self._scale*tetrimino[2][1]
                pygame.draw.rect(self._display, color, 
                pygame.Rect(x_coord, y_coord, self._scale, self._scale))

        pygame.display.flip()
