import random
import pygame

def display_score():
    text_fonts = pygame.font.Font("font/Pixeltype.ttf", 50)
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = text_fonts.render(f"SCORE:{current_time}",False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time
#Pygame Initialisation
pygame.init()
clock = pygame.time.Clock()

#Code for Screen Formation 
screen = pygame.display.set_mode((800,400))

#Code for caption and icon
pygame.display.set_caption("Pixel Runner")

#Sky
sky_surf = pygame.image.load("graphics/Sky.png")
sky_rect = sky_surf.get_rect(topleft = (0,0))
def sky():
    screen.blit(sky_surf,sky_rect)

#Ground
ground_surf = pygame.image.load("img/ground.png")
ground_rect = ground_surf.get_rect(topleft = (0,300))
def ground():
    screen.blit(ground_surf,ground_rect)

#Snail
snail_surf = pygame.image.load("img/snail1.png")
snail_rect = snail_surf.get_rect(midbottom = (800,300))
def snail():
    screen.blit(snail_surf,snail_rect)

#Fly
fly_surf = pygame.image.load("img/Fly1.png")
fly_rect = fly_surf.get_rect(center = (800,180))
def fly():
    screen.blit(fly_surf,fly_rect)

#Player
player_surf = pygame.image.load("img/player_stand.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0
def player():
    screen.blit(player_surf,player_rect)

#Intro Screen
player_stand = pygame.image.load("img/player_stand.png")
# player_stand_scaled = pygame.transform.scale(player_stand,(200,400))
# player_stand_scaled = pygame.transform.scale2x(player_stand)
player_stand_scaled = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand_scaled.get_rect(center = (400,200))
def player_stand_func():
    screen.blit(player_stand_scaled,player_stand_rect)
    # screen.blit(player_stand,player_stand_rect)

#Game Name
text_font = pygame.font.Font("font/Pixeltype.ttf", 42)
game_name_surf = text_font.render("Pixel Runner" ,False,(64,64,64))
game_name_rect = game_name_surf.get_rect(center = (405,100))
def game_name_func():
    screen.blit(game_name_surf, game_name_rect)

#Intro Message
text_font = pygame.font.Font("font/Pixeltype.ttf", 32)
text_surf = text_font.render("Press  SPACE  to Start Game" ,False,(64,64,64))
text_rect = text_surf.get_rect(center = (400,310))
def text():
    screen.blit(text_surf, text_rect)

#Final Score
def final():
    final_surf = text_font.render(f"Your Score: {final_score}" ,False,(64,64,64))
    final_rect = final_surf.get_rect(center = (400,310))
    screen.blit(final_surf, final_rect)


#Game Loop
start_time = 0 
final_score = 0
game_in_progress = False
running = True
while running:
    # screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_in_progress:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        player_gravity = -20

            #To locate coordinates of any point on screen
            # if event.type == pygame.MOUSEMOTION:
            #     print(event.pos)
                # print(pygame.mouse.get_pos())
        else:
            if event.type == pygame.KEYDOWN and event.key  == pygame.K_SPACE:
                game_in_progress = True
                snail_rect.x = 800
                start_time = int(pygame.time.get_ticks()/1000)
                
    
    if game_in_progress:
        #Snail Movement
        snail_rect.x -= 5
        if snail_rect.x <= -100:
            snail_rect.x = random.randint(900,1200)

        #Fly Movement
        fly_rect.x -= 7
        if fly_rect.x <= -100:
            fly_rect.x = random.randint(1000,1600)

        #Player Movement
        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300

        #Functions
        sky()
        ground()
        snail()
        fly()
        player()
        final_score = display_score()

        #Collision
        if player_rect.colliderect(snail_rect):
            game_in_progress = False

    else:
        screen.fill((94,129,162))
        game_name_func()
        player_stand_func()
        if final_score == 0:text()
        else: final()

        

    clock.tick(60)
    pygame.display.update()