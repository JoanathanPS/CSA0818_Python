import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Bouncing Ball")

x, y = 100, 100
dx, dy = 3, 3
radius = 20

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    x += dx
    y += dy

    if x - radius <= 0 or x + radius >= 600:
        dx = -dx
    if y - radius <= 0 or y + radius >= 400:
        dy = -dy

    pygame.display.flip()
    clock.tick(60)