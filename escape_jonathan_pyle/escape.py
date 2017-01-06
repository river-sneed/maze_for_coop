# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
TITLE = "Escape"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (8, 8, 253)
ORANGE = (255, 86, 24)


def setup():
    global player, player_vx, player_vy, player_speed, enemy1, enemy1_vx, enemy1_vy, enemy1_speed, time_remaining, ticks

#Stages
START = 0
PLAYING = 1
END = 2

 # Make a player
player =  [130, 50, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5


 #Make an enemy
enemy1 = [950, 775, 25, 25]
enemy1_vx = 0
enemy1_vy = 0
enemy1_speed = 5

stage = START
time_remaining = 90
ticks = 0
MY_FONT = pygame.font.Font(None, 48)

# make walls
wall1 =  [475, 325, 25, 200]
wall2 =  [300, 500, 200, 25]
wall3 =  [100, 100, 25, 200]
wall4 =  [100, 300, 25, 200]
wall5 =  [100, 500, 200, 25]
wall6 =  [175, 100, 25, 200]
wall7 =  [175, 275, 25, 200]
wall8 =  [175, 450, 200, 25]
wall9 =  [375, 275, 25, 200]
wall10 = [375, 250, 200, 25]
wall11 = [300, 250, 25, 200]
wall12 = [200, 125, 400, 25]
wall13 = [0, 100, 100, 25]
wall14 = [500, 325, 200, 25]
wall15 = [525, 250, 200, 25]
wall16 = [675, 350, 25, 200]
wall17 = [175, 0, 25, 100]
wall18 = [575, 0, 25, 125]
wall19 = [500, 550, 200, 25]
wall20 = [700, 325, 200, 25]
wall21 = [800, 150, 25, 200]
wall22 = [600, 50, 200, 25]
wall23 = [800, 50, 200, 25]
wall24 = [1000, 50, 25, 200]
wall25 = [1000, 250, 25, 200]
wall26 = [825, 450, 200, 25]
wall27 = [825, 475, 25, 200]
wall28 = [650, 650, 200, 25]
wall29 = [475, 550, 25, 200]
wall30 = [650, 675, 25, 200]
wall31 = [300, 750, 200, 25]
wall32 = [275, 850, 400, 25]
wall33 = [75, 850, 200, 25]
wall34 = [75, 650, 25, 200]
wall35 = [75, 650, 200, 25]
wall36 = [275, 500, 25, 175]
wall37 = [500, 200, 25, 50]
wall38 = [500, 700, 75, 25]
wall39 = [400, 800, 25, 75]
wall40 = [600, 200, 200, 25]
wall41 = [750, 500, 25, 150]
wall42 = [100, 775, 150, 25]
wall43 = [375, 650, 25, 100]
wall44 = [450, 775, 25, 50]
wall45 = [350, 775, 25, 50]
wall46 = [500, 800, 25, 50]
wall47 = [575, 550, 25, 100]
wall48 = [300, 800, 25, 50]
wall49 = [700, 400, 100, 25]
wall50 = [700, 75, 25, 100]
wall51 = [750, 100, 25, 100]
wall52 = [850, 75, 25, 100]
wall53 = [825, 200, 100, 25]
wall54 = [900, 250, 100, 25]
wall55 = [900, 375, 100, 25]
wall56 = [400, 400, 50, 25]
wall57 = [325, 600, 175, 25]
wall58 = [625, 400, 25, 175]
wall59 = [625, 600, 25, 25]
wall60 = [700, 625, 50, 25]
wall61 = [550, 725, 25, 75]
wall62 = [600, 725, 25, 125]
wall63 = [200, 675, 25, 75]
wall64 = [200, 700, 150, 25]
wall65 = [125, 150, 25, 25]
wall66 = [150, 200, 25, 25]
wall67 = [125, 250, 25, 25]
wall68 = [150, 300, 25, 25]
wall69 = [125, 350, 25, 25]
wall70 = [150, 400, 25, 25]
wall71 = [125, 450, 25, 25]
wall72 = [475, 275, 25, 25]
wall73 = [525, 300, 25, 25]
wall74 = [575, 275, 25, 25]
wall75 = [625, 300, 25, 25]
wall76 = [675, 275, 25, 25]
wall77 = [725, 300, 25, 25]
wall78 = [525, 375, 25, 175]
wall79 = [575, 350, 25, 175]
wall80 = [700, 450, 100, 25]
wall81 = [200, 350, 100, 25]
wall82 = [775, 400, 75, 25]
wall83 = [925, 300, 25, 75]
wall84 = [335, 150, 25, 75]
wall85 = [450, 150, 25, 75]
wall86 = [400, 175, 25, 75]
wall87 = [500, 175, 25, 25]
wall88 = [550, 150, 25, 75]
wall89 = [0, 0, 25, 125]
wall90 = [0, 0, 175, 25]
wall91 = [200, 0, 375, 25]
wall92 = [325, 525, 25, 50]
wall93 = [375, 550, 25, 50]
wall94 = [425, 525, 25, 50]
wall95 = [650, 100, 25, 100]
wall96 = [600, 75, 25, 75]
wall97 = [800, 75, 25, 50]
wall98 = [1000, 400, 25, 475]
wall99 = [675, 850, 325, 25]
wall100 = [800, 725, 200, 25]
wall101 = [850, 600, 100, 25]
wall102 = [875, 775, 25, 50]






walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11,
         wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20,
         wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30,
         wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38, wall39,
         wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47, wall48,
         wall49, wall50, wall51, wall52, wall53, wall54, wall55, wall56, wall57,
         wall58, wall59, wall60, wall61, wall62, wall63, wall64, wall65, wall66,
         wall67, wall68, wall69, wall70, wall71, wall72, wall73, wall74, wall75,
         wall76, wall77, wall78, wall79, wall80, wall81, wall82, wall83, wall84,
         wall85, wall86, wall87, wall88, wall89, wall90, wall91, wall92, wall93,
         wall94, wall95, wall96, wall97, wall98, wall99, wall100, wall101, wall102]


# Make coins
coin1 = [275, 275, 25, 25]
coin2 = [600, 225, 25, 25]
coin3 = [500, 500, 25, 25]
coin4 = [500, 300, 25, 25]
coin5 = [825, 300, 25, 25]
coin6 = [800, 600, 25, 25]
coin7 = [500, 650, 25, 25]
coin8 = [300, 775, 25, 25]
coin9 = [825, 75, 25, 25]
coin10 = [650, 525, 25, 25]
coin11 = [700, 425, 25, 25]

coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
         coin11]

#Make teleporter
teleporter1 = [425, 700, 25, 25]
teleporter2 = [900, 650, 25, 25]
teleporter3 = [200, 475, 25, 25]
teleporter4 = [650, 350, 25, 25]

teleporters = [teleporter1, teleporter2, teleporter3, teleporter4]


img = pygame.image.load('splashscreen.jpg')
lose = False


# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:

            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING

                elif stage == END:
                     if event.key == pygame.K_SPACE:
                         setup()

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()


        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
   
        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if left:
            player_vx = -player_speed
        elif right:
            player_vx = player_speed
        else:
            player_vx = 0
        

        up = pressed[pygame.K_w]
        down = pressed[pygame.K_s]
        left = pressed[pygame.K_a]
        right = pressed[pygame.K_d]

        if up:
            enemy1_vy = -enemy1_speed
        elif down:
            enemy1_vy = enemy1_speed
        else:
            enemy1_vy = 0
            
        if left:
            enemy1_vx = -enemy1_speed
        elif right:
            enemy1_vx = enemy1_speed
        else:
            enemy1_vx = 0

    


    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    enemy1[0] += enemy1_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(enemy1, w):        
            if enemy1_vx > 0:
                enemy1[0] = w[0] - enemy1[2]
            if enemy1_vx < 0:
                enemy1[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    enemy1[1] += enemy1_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(enemy1, w):                    
            if enemy1_vy > 0:
                enemy1[1] = w[1] - enemy1[3]
            if enemy1_vy < 0:
                enemy1[1] = w[1] + w[3]


        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player[0] += player_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player, w):        
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player[1] += player_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player, w):                    
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]



    ''' get the coins '''
    coins = [c for c in coins if not intersects.rect_rect(player, c)]

    if len(coins) == 0:
        win = True
        

    '''Teleporter'''
    if intersects.rect_rect(player, teleporter1):
        player = [900, 700, 25, 25]

    if intersects.rect_rect(enemy1, teleporter1):
        enemy1 = [900, 775, 25, 25]

    if intersects.rect_rect(enemy1, teleporter2):
        enemy1 = [950, 125, 25, 25]

    if intersects.rect_rect(player, teleporter2):
        player = [250, 250, 25, 25]

    if intersects.rect_rect(player, teleporter3):
        player = [100, 800, 25, 25]

    if intersects.rect_rect(enemy1, teleporter3):
        enemy1 = [500, 600, 25, 25]
        
    if intersects.rect_rect(player, teleporter4):
        player = [500, 725, 25, 25]
        
    if intersects.rect_rect(enemy1, teleporter4):
        enemy1 = [850, 375, 25, 25]

    '''Timer'''
    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            lose = True
  
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, ORANGE, player)
    pygame.draw.rect(screen, RED, enemy1)
    
    
    timer_text = MY_FONT.render(str(time_remaining), True, GREEN)
    screen.blit(timer_text, [1100, 50])


    if intersects.rect_rect(player, enemy1):
        lose = True
        
        
    for w in walls:
        pygame.draw.rect(screen, BLUE, w)

    for t in teleporters:
        pygame.draw.rect(screen, GREEN, t)
        

    for c in coins:
        pygame.draw.ellipse(screen, YELLOW, c)
        
    if win:
        text = MY_FONT.render("Player wins!", 1, ORANGE)
        screen.blit(text, [300, 50])
        
        
    if lose:
        text = MY_FONT.render("Enemy1 Wins!", 1, RED)
        lose = True
        screen.blit(text, [300, 50])
        
        
    if lose:
        time_remaining = 0
        
    if time_remaining == 0:
        lose = True
        
    if stage == START:
        screen.blit(img, (0, 0))

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()
    

    # Limit refresh rate of game loop  
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
