import sys
import random
import pygame

pygame.init()

width = 400
height = 100
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('FLAME')

ar = pygame.PixelArray(screen)
while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for i in range(0, width):
        ar[i, height - 1] = random.randrange(2) * 200
        ar[i, height - 2] = random.randrange(2) * 200

    for y in range(0, height - 2):
        for x in range(1, width - 1):
            ar[x, y] = int((ar[x - 1, y + 1] + ar[x, y + 1] +
                            ar[x + 1, y + 1] + ar[x, y + 2]) * 0.24) 

    for i in range(0, width):
        ar[i, height - 1] = 100
        ar[i, height - 2] = 100

    pygame.display.flip()
