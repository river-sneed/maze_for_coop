# Imports
import pygame
import intersects
import random




# Window
WIDTH = 1000
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
TITLE = "Solve that $###"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 1

# Colors
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255, 0)
GREEN = (0,255,0)
BLUE = (8,8,253)
ORANGE = (255,86,24)
LAVENDER = (206,160,255)
PINK = (248,50,255)
TEAL = (48,232,183)
SWEET_PEPE_GREEN = (104,152,76)
SWEET_PEPE_BLUE = (35,74,252)
SWEET_PEPE_RED = (169,106,64)

def draw_pepe(x, y):

    pygame.draw.ellipse(screen, SWEET_PEPE_BLUE, [x-100, y+400, 650, 400])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [x-20, y+150, 750, 400])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [x+50, y+10, 380, 500])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [x+250, y+10, 380, 500])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [x+200, y+70, 500, 170])
    pygame.draw.rect(screen, SWEET_PEPE_RED, [x+225, y+375, 485, 75])
    pygame.draw.ellipse(screen, SWEET_PEPE_RED, [x+190, y+375, 75, 75])
    pygame.draw.ellipse(screen, SWEET_PEPE_RED, [x+655, y+375, 100, 37])
    pygame.draw.ellipse(screen, SWEET_PEPE_RED, [x+655, y+415, 75, 37])
    pygame.draw.ellipse(screen, WHITE, [x+450, y+110, 250, 90])
    pygame.draw.ellipse(screen, BLACK, [x+450, y+110, 250, 90], 7)
    pygame.draw.ellipse(screen, WHITE, [x+200, y+110, 200, 90])
    pygame.draw.ellipse(screen, BLACK, [x+200, y+110, 200, 90], 7)
    pygame.draw.ellipse(screen, BLACK, [x+250, y+115, 75, 75])
    pygame.draw.ellipse(screen, BLACK, [x+520, y+115, 75, 75])
stage = 0
def setup():
    global player, player_vx, player_vy, player_speed, player2, player2_vx, player2_vy, player2_speed, player3, player3_vx, player3_vy, player3_speed, time_remaining, ticks






     # Make a player 1
    player1 =  [225, 337, 25, 25]
    player1_vx = 0
    player1_vy = 0
    player1_speed = 5


     #Make an player 2
    player2 = [487, 125, 25, 25]
    player2_vx = 0
    player2_vy = 0
    player2_speed = 5

     # Make a player 3
    player3 =  [725, 337, 25, 25]
    player3_vx = 0
    player3_vy = 0
    player3_speed = 5

    stage = START_SPLASH_SCREEN
    time_remaining = 90
    ticks = 0
    """MY_FONT = pygame.font.Font(None, 48)"""

    # make walls
    #section 1
    wall1 =  [0,0,1000,25]
    wall2 =  [0,0,25,700]
    wall3 =  [975,0,25,700]
    wall4 =  [0,675,1000,25]
    wall5 =  [75,75,75,75]
    wall6 =  [200,25,75,75]
    wall7 =  [75,200,50,50]
    wall8 =  [250,150,75,100]
    wall9 =  [325,75,75,175]
    wall10 = [450,0,25,325]
    wall11 = [0,300,475,25]
    #section 2
    wall12 = [75,450,100,175]
    wall13 = [75,450,325,75]
    wall14 = [75,575,200,50]
    wall15 = [375,450,25,175]
    wall16 = [0,375,475,25]
    wall17 = [450,375,25,325]
    #section 3
    wall18 = [525,375,475,25]
    wall19 = [525,375,25,325]
    wall20 = [600,450,50,50]
    wall21 = [700,450,25,50]
    wall22 = [800,450,25,50]
    wall23 = [875,450,50,50]
    wall24 = [600,525,50,25]
    wall25 = [700,525,25,25]
    wall26 = [800,525,25,25]
    wall27 = [875,525,50,25]
    wall28 = [600,575,50,50]
    wall29 = [700,575,25,50]
    wall30 = [800,575,25,50]
    wall31 = [875,575,50,50]
    #section 4
    wall32 = [525,0,25,325]
    wall33 = [525,300,475,25]
    wall34 = [600,75,325,50]
    wall35 = [600,75,50,175]
    wall36 = [700,175,225,75]


    walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11,
             wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20,
             wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30,
             wall31, wall32, wall33, wall34, wall35, wall36]


    # Make coins
    #section 1
    coin1 = [100,25,50,50]
    coin2 = [25,150,50,50]
    coin3 = [200,250,50,50]
    coin4 = [275,100,50,50]
    coin5 = [275,250,50,50]
    coin6 = [350,250,50,50]
    coin7 = [400,100,50,50]
    coin8 = [400,200,50,50]
    #section 2
    coin9 = [25,400,50,50]
    coin10 = [225,400,50,50]
    coin11 = [400,400,50,50]
    coin12 = [400,500,50,50]
    coin13 = [400,625,50,50]
    coin14 = [225,625,50,50]
    #section 3
    coin15 = [650,400,50,50]
    coin16 = [700,400,50,50]
    coin17 = [775,400,50,50]
    coin18 = [825,400,50,50]
    coin19 = [925,535,50,50]
    coin20 = [550,575,50,50]
    coin21 = [725,625,50,50]
    coin22 = [825,625,50,50]
    #section 4
    coin23 = [550,75,50,50]
    coin24 = [550,125,50,50]
    coin25 = [550,175,50,50]
    coin26 = [600,25,50,50]
    coin27 = [650,25,50,50]
    coin28 = [600,250,50,50]
    coin29 = [725,250,50,50]
    coin30 = [750,25,50,50]
    coin31 = [825,25,50,50]
    coin32 = [850,250,50,50]
    coin33 = [925,200,50,50]
    coin34 = [550,25,50,50]

    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
             coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20,
             coin21, coin22, coin23, coin24, coin25, coin26, coin27, coin28, coin29, coin30,
             coin31, coin32, coin33, coin34]

    #Make teleporters
    teleporter1 = [400,250,50,50]
    teleporter2 = [175,525,50,50]
    teleporter3 = [550,400,50,50]
    teleporter4 = [550,250,50,50]
    teleporter5 = [475,325,50,50]

    teleporters = [teleporter1, teleporter2, teleporter3, teleporter4, teleporter5]

    #Make fake walls
    fake_wall1 = [175,525,100,50]
    fake_wall2 = [275,525,100,100]
    fake_wall3 = [650,125,50,125]
    fake_wall4 = [700,125,225,50]

    fake_walls = [fake_wall1, fake_wall2, fake_wall3, fake_wall4]

    img = pygame.image.load('splashscreen.jpg')
lose = False
START_SPLASH_SCREEN = 0
PLAY = 1
END_SPLASH_SCREEN = 2

# Game loop
player1_wins = False
player2_wins = False
player3_wins = False
done = False


while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:

            if stage == START_SPLASH_SCREEN:
                if event.key == pygame.K_SPACE:
                    stage = PLAY

                elif stage == END_SPLASH_SCREEN:
                     if event.key == pygame.K_SPACE:
                         setup()

    if stage == PLAY:
        pressed = pygame.key.get_pressed()


        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
   
        if up:
            player1_vy = -player1_speed
        elif down:
            player1_vy = player1_speed
        else:
            player1_vy = 0
            
        if left:
            player1_vx = -player1_speed
        elif right:
            player1_vx = player1_speed
        else:
            player1_vx = 0
        

        up = pressed[pygame.K_w]
        down = pressed[pygame.K_s]
        left = pressed[pygame.K_a]
        right = pressed[pygame.K_d]

        if up:
            player2_vy = -player2_speed
        elif down:
            player2_vy = player2_speed
        else:
            player2_vy = 0
            
        if left:
            player2_vx = -player2_speed
        elif right:
            player2_vx = player2_speed
        else:
            player2_vx = 0

        up = pressed[pygame.K_8]
        down = pressed[pygame.K_5]
        left = pressed[pygame.K_4]
        right = pressed[pygame.K_6]

        if up:
            player3_vy = -player3_speed
        elif down:
            player3_vy = player3_speed
        else:
            player3_vy = 0
            
        if left:
            player3_vx = -player3_speed
        elif right:
            player3_vx = player3_speed
        else:
            player3_vx = 0

    


    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player1[0] += player1_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if player1_vx > 0:
                player1[0] = w[0] - player1[2]
            if player1_vx < 0:
                player1[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player1[1] += player1_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if player1_vy > 0:
                player1[1] = w[1] - player1[3]
            if player1_vy < 0:
                player1[1] = w[1] + w[3]


        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player2[0] += player2_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player2, w):        
            if player2_vx > 0:
                player2[0] = w[0] - player2[2]
            elif player2_vx < 0:
                player2[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player2[1] += player2_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player2, w):                    
            if player2_vy > 0:
                player2[1] = w[1] - player2[3]
            if player2_vy < 0:
                player2[1] = w[1] + w[3]

    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player3[0] += player3_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player3, w):        
            if player3_vx > 0:
                player3[0] = w[0] - player3[2]
            if player3_vx < 0:
                player3[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player3[1] += player3_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player3, w):                    
            if player3_vy > 0:
                player3[1] = w[1] - player3[3]
            if player3_vy < 0:
                player3[1] = w[1] + w[3]



    ''' get the coins '''
    coins = [c for c in coins if not intersects.rect_rect(player1, c)]

    PLAYER1_CC = 34 - len(coins)

    coins = [c for c in coins if not intersects.rect_rect(player2, c)]

    PLAYER2_CC = 34 - len(coins)

    coins = [c for c in coins if not intersects.rect_rect(player3, c)]

    PLAYER3_CC = 34 - len(coins)

        

    '''Teleporter'''
    if intersects.rect_rect((player1), teleporter1):
        d = random.randint(0,3)
        if d == 0:
            player1 = [37,337,25,25]
        elif d == 1:
            player1 = [487,637,25,25]
        elif d == 2:
            player1 = [937,337,25,25]
        elif d == 3:
            player1 = [487,37,25,25]
        else:
            pass

    if intersects.rect_rect((player1), teleporter2):
        destintion = random.randint(0,3)
        if d == 0:
            player1 = [37,337,25,25]
        elif d == 1:
            player1 = [487,637,25,25]
        elif d == 2:
            player1 = [937,337,25,25]
        elif d == 3:
            player1 = [487,37,25,25]
        else:
            pass
        
    if intersects.rect_rect((player1), teleporter3):
        destintion = random.randint(0,3)       
        if d == 0:
            player1 = [37,337,25,25]
        elif d == 1:
            player1 = [487,637,25,25]
        elif d == 2:
            player1 = [937,337,25,25]
        elif d == 3:
            player1 = [487,37,25,25]
        else:
            pass
        
    if intersects.rect_rect((player1), teleporter4):
        destintion = random.randint(0,3)        
        if d == 0:
            player1 = [37,337,25,25]
        elif d == 1:
            player1 = [487,637,25,25]
        elif d == 2:
            player1 = [937,337,25,25]
        elif d == 3:
            player1 = [487,37,25,25]
        else:
            pass
        
    if intersects.rect_rect((player1), teleporter5):
        destintion = random.randint(0,3)        
        if d == 0:
            player1 = [37,37,25,25]
        elif d == 1:
            player1 = [37,652,25,25]
        elif d == 2:
            player1 = [937,652,25,25]
        elif d == 3:
            player1 = [987,37,25,25]
        else:
            pass
        
    if intersects.rect_rect((player2), teleporter1):
        d = random.randint(0,3)       
        if d == 0:
            player = [37,337,25,25]
        elif d == 1:
            player = [487,637,25,25]
        elif d == 2:
            player = [937,337,25,25]
        elif d == 3:
            player = [487,37,25,25]
        else:
            pass
    if intersects.rect_rect((player2), teleporter2):
        d = random.randint(0,3)
        if d == 0:
            player = [37,337,25,25]
        elif d == 1:
            player = [487,637,25,25]
        elif d == 2:
            player = [937,337,25,25]
        elif d == 3:
            player = [487,37,25,25]
        else:
            pass
        
    if intersects.rect_rect((player2), teleporter3):
        d = random.randint(0,3)
        if d == 0:
            player = [37,337,25,25]
        elif d == 1:
            player = [487,637,25,25]
        elif d == 2:
            player = [937,337,25,25]
        elif d == 3:
            player = [487,37,25,25]
        else:
            pass
        
    if intersects.rect_rect((player2), teleporter4):
        destintion = random.randint(0,3)
        if d == 0:
            player = [37,337,25,25]
        elif d == 1:
            player = [487,637,25,25]
        elif d == 2:
            player = [937,337,25,25]
        elif d == 3:
            player = [487,37,25,25]
        else:
            pass
        
    if intersects.rect_rect((player2), teleporter5):
        d = random.randint(0,3)       
        if d == 0:
            player = [37,37,25,25]
        elif d == 1:
            player = [37,652,25,25]
        elif d == 2:
            player = [937,652,25,25]
        elif d == 3:
            player = [987,37,25,25]
        else:
            pass
        
    if intersects.rect_rect((player3), teleporter1):
        d = random.randint(0,3)
        if d == 0:
            player = [37,337,25,25]
        elif d == 1:
            player = [487,637,25,25]
        elif d == 2:
            player = [937,337,25,25]
        elif d == 3:
            player = [487,37,25,25]
        else:
            pass
        
    if intersects.rect_rect((player3), teleporter2):
        d = random.randint(0,3)
        if d == 0:
            player = [37,337,25,25]
        elif d == 1:
            player = [487,637,25,25]
        elif d == 2:
            player = [937,337,25,25]
        elif d == 3:
            player = [487,37,25,25]
        else:
            pass
    if intersects.rect_rect((player3), teleporter3):
        d = random.randint(0,3)
        if d == 0:
            player = [37,337,25,25]
        elif d == 1:
            player = [487,637,25,25]
        elif d == 2:
            player = [937,337,25,25]
        elif d == 3:
            player = [487,37,25,25]
        else:
            pass
        
    if intersects.rect_rect((player3), teleporter4):
        d = random.randint(0,3)
        if d == 0:
            player = [37,337,25,25]
        elif d == 1:
            player = [487,637,25,25]
        elif d == 2:
            player = [937,337,25,25]
        elif d == 3:
            player = [487,37,25,25]
        else:
            pass
        
    if intersects.rect_rect((player3), teleporter5):
        d = random.randint(0,3)
        if d == 0:
            player = [37,37,25,25]
        elif d == 1:
            player = [37,652,25,25]
        elif d == 2:
            player = [937,652,25,25]
        elif d == 3:
            player = [987,37,25,25]
        else:
            pass


    '''Timer'''
    if stage == PLAY:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            lose = True
  
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, YELLOW, player2)
    pygame.draw.rect(screen, BLUE, player3)   
    
    
    """timer_text = MY_FONT.render(str(time_remaining), True, GREEN)"""
    """screen.blit(timer_text, [1100, 50])"""



        
        
    for w in walls:
        pygame.draw.rect(screen, PINK, w)

    for t in teleporters:
        pygame.draw.rect(screen, TEAL, t)
        
    for c in coins:
        pygame.draw.ellipse(screen, YELLOW, c)
        
    for f in fake_walls:
        pygame.draw.rect(screen, PINK, f)
        
    if player1_wins:
        screen.fill(BLACK)
        draw_pepe()
        print("""text = MY_FONT.render("Player1 wins!", 1, RED)
        screen.blit(text, [300, 50])""")
        
        
    if player2_wins:
        screen.fill(BLACK)
        draw_pepe()
        print("""text = MY_FONT.render("Player2 Wins!", 1, YELLOW)
        screen.blit(text, [300, 50])""")

    if player3_wins:
        screen.fill(BLACK)
        draw_pepe()
        print("""text = MY_FONT.render("Player3 Wins!", 1, BLUE)
        screen.blit(text, [300, 50])""")
        
        
   

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()
    

    # Limit refresh rate of game loop  
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
