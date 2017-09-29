import sys
import random
import pygame

pygame.init()

width = 200
height = 100
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('FLAME')

ar = pygame.PixelArray(screen)
s2 = pygame.Surface((width, height + 5))
ar2 = pygame.PixelArray(s2)


def gradient(col1, col2, n):
    return [tuple(((n - i) * col1[k] + i * col2[k]) / n for k in range(3)) for i in range(n)]

pallate = gradient((0, 0, 0), (200, 20, 20), 30) + \
          gradient((200, 20, 20), (220, 220, 50), 100) + \
          gradient((200, 220, 50), (240, 240, 240), 81)

while True:
    clock.tick(1000)
    print(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for i in range(0, width):
        ar2[i, height + 3] = random.randrange(2) * 200
        ar2[i, height + 4] = random.randrange(2) * 200

    mx, my = pygame.mouse.get_pos()
    pygame.draw.circle(s2, 200,
            (mx + random.randrange(-2, 2), my + random.randrange(-2, 2)), 2)

    for y in range(0, height + 3):
        for x in range(1, width - 1):
            ar2[x, y] = (ar2[x - 1, y + 1] + ar2[x, y + 1] +
                            ar2[x + 1, y + 1] + ar2[x, y + 2]) * 240 // 1000

    for y in range(height):
        for x in range(width):
            ar[x, y] = pallate[ar2[x, y]]

    pygame.display.flip()
