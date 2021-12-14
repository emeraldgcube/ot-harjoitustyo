import pygame
from pygame import event
from clock import Clock
from level import Level
from renderer import Renderer
from game_loop import GameLoop
from event_queue import EventQueue

def main():
    pygame.init()
    pygame.display.set_caption("Tetris")
    #new_game()
    scale=30
    screen_width=26*scale
    screen_height=22*scale
    window = pygame.display.set_mode((screen_width, screen_height))

    clock=Clock()
    position=2
    control=""
    time1=0
    rotation=0
    matrix=[]
    for a in range(0,22):
        matrix.append([])
        for b in range(0,10):
            matrix[a].append(0)
    #collision=False
    
    level=Level()
    event_queue=EventQueue()
    renderer=Renderer(window, level, scale)
    loop=GameLoop(level, renderer, event_queue, clock, scale)
    loop.start()

main()











































