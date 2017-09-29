import sys
import pygame

pygame.init()

width = 500
height = 500
a = 500.0
k = 2.0
x = 100
y = 100
vx = 0
vy = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        vx -= dt * a
    if pressed[pygame.K_RIGHT]:
        vx += dt * a
    if pressed[pygame.K_UP]:
        vy -= dt * a
    if pressed[pygame.K_DOWN]:
        vy += dt * a

    vx -= dt * vx * k
    vy -= dt * vy * k
    x += vx * dt
    y += vy * dt

    if x < 20:
        if vx < 0:
            vx = -vx
        x = 20
    if y < 20:
        if vy < 0:
            vy = -vy
        y = 20

    screen.fill((0, 0, 0))
    col = min(255, int((vx ** 2 + vy ** 2) ** 0.5) + 100)
    pygame.draw.circle(screen, (col, col, col), (int(x), int(y)), 20)

    pygame.display.flip()
