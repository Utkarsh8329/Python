import pygame

#Pygame Initialisation
pygame.init()

#Surface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Exercise 2')

#Text Surface
text_font = pygame.font.Font(None,40)
text_surface = text_font.render("My Game", False ,("Green"))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(text_surface ,(350,160))
    pygame.display.update()