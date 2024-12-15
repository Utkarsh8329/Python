import pygame

#Pygame Initialisation
pygame.init()

clock = pygame.time.Clock()

#Surface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Exercise 2')

#Text Surface
text_font = pygame.font.Font(None,40)
score_surf = text_font.render("Score", False ,("Green"))
score_rect = score_surf.get_rect(center = (400,50) )

#Ground
ground_surface = pygame.image.load("graphics/ground.png")
#Sky
sky_surface = pygame.image.load("graphics/Sky.png")

#Snail
snail_surf = pygame.image.load('graphics/snail/snail1.png')
snail_rect = snail_surf.get_rect(bottomright = (800,300))

#Player
player_surf = pygame.image.load('graphics/Player/player_walk_1.png')
player_rect = player_surf.get_rect(midbottom = (80,300))

#BLIT FUNCTIONS
# def snail():
#     screen.blit(snail_surface, snail_rect)

def sky(x,y):
    screen.blit(sky_surface ,(x,y))

def ground(x,y):
    screen.blit(ground_surface ,(x,y))

def score():
    screen.blit(score_surf , score_rect)

def player():
    screen.blit(player_surf ,player_rect)

#Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # #shows that mouse is moving or not 
        # if event.type == pygame.MOUSEMOTION:
        # #Give Mouse Position in (x,y)
        #     print(event.pos)

        # #Shows that whether a mouse button is pressed or not
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("Mouse button is pressed")
        # #Shows that whether the mouse button is free or not
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print("Mouse button is free")

        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("Collision")
    
    #Snail Movement
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    

    #FUNCTIONS
    sky(0, 0)
    ground(0, 300)
    screen.blit(snail_surf,snail_rect)
    score()
    player()
    

    pygame.display.update()
    clock.tick(60)