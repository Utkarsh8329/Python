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
    #FUNCTIONS
    sky(0, 0)
    ground(0, 300)
    pygame.draw.rect(screen, "Red", score_rect)
    # pygame.draw.line(screen, "Gold", (0,0), pygame.mouse.get_pos(),10)
    pygame.draw.ellipse(screen,"Green", pygame.Rect(50,200,100,100))
    player()
    score()
    pygame.display.update()
    clock.tick(60)