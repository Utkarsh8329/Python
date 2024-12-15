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
playerX = 80
playerY = 220
playerX_change = 0
playerY_change = 0

#BLIT FUNCTIONS
# def snail():
#     screen.blit(snail_surface, snail_rect)

def sky(x,y):
    screen.blit(sky_surface ,(x,y))

def ground(x,y):
    screen.blit(ground_surface ,(x,y))

def score():
    screen.blit(score_surf , score_rect)

def player(x,y):
    screen.blit(player_surf ,(x,y))

#Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerY_change -= 10
            if event.key == pygame.K_RIGHT:
                playerX_change += 4
            if event.key == pygame.K_LEFT:
                playerX_change -= 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_SPACE:
                playerY_change += 10
       
    
    #Snail Movement
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    

    #FUNCTIONS
    sky(0, 0)
    ground(0, 300)
    # screen.blit(snail_surf,snail_rect)
    score()

    #Player
    playerY += playerY_change
    playerX += playerX_change
    player(playerX,playerY)
    

    pygame.display.update()
    clock.tick(60)