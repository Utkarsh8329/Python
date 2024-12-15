import pygame

#Pygame Initialisation
pygame.init()

#Surface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Exercise 1')

#Regular Surface
box = pygame.Surface((100,200))
box.fill('Red')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(box,(200,100))
    pygame.display.update()