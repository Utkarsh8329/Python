import pygame

#Pygame Initialisation
pygame.init()

clock = pygame.time.Clock()

#Surface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Exercise 2')

#Text Surface
text_font = pygame.font.Font(None,40)
text_surface = text_font.render("My Game", False ,("Green"))

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
player_gravity = 0

#BLIT FUNCTIONS
# def snail():
#     screen.blit(snail_surface, snail_rect)

def sky(x,y):
    screen.blit(sky_surface ,(x,y))

def ground(x,y):
    screen.blit(ground_surface ,(x,y))

def text(x,y):
    screen.blit(text_surface ,(x,y))

def player():
    screen.blit(player_surf ,player_rect)

#Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity -= 20
        # if event.type == pygame.KEYUP:
            # if event.key == pygame.K_SPACE:
            #     player_rect.bottom +=20
        
        
    #Snail Movement
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    if player_rect.bottom >= 300:
        player_rect.bottom = 300

    player_gravity += 1
    player_rect.y += player_gravity
    
    #FUNCTIONS
    sky(0, 0)
    ground(0, 300)
    screen.blit(snail_surf,snail_rect)
    text(350, 140)
    player()
    

    pygame.display.update()
    clock.tick(60)