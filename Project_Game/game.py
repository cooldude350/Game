import pygame


pygame.init()
pygame.display.set_caption("Test")
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 255, 0))
    pygame.display.update()       

