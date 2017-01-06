#SUPER MAZE!
#Eliot D.
#December 9 2016
#Cool 2/3 player maze
#3 players: 2 players try to get coins, 1 player tries to stop them
#2 players: 1 player tries to get coins, 1 player tries to stop them
#Enemy controls: i j k l
#Player 1 controls: ▲ ◄ ▼ ►
#Player 2 controls: w a s d

# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1260
HEIGHT = 980
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
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
GREEN = (157, 186, 94)
BROWN = (65, 93, 35)
LGREEN = (155, 188, 15)
GRAY = (200, 200, 200)
DGRAY = (50, 50, 50)
ROYGBIV = (0, 0, 0)

# stages
START = 0
PLAYING = 1
END = 2

startscreen = pygame.image.load("splashscreen.png")
endscreen = pygame.image.load("endscreen.png")
coinsound = pygame.mixer.Sound("windows xp error.wav")
powersound = pygame.mixer.Sound("Windows Background.wav")
actionsound = pygame.mixer.Sound("windows xp start.wav")
powersound2 = pygame.mixer.Sound("Windows Foreground.wav")
actionsound2 = pygame.mixer.Sound("windows xp shutd.wav")

def setup():
    global walls, coins, powerups, player, player_vx, player_vy, player_speed, player2, player2_vx, player2_vy, player2_speed, player3, player3_vx, player3_vy, player3_speed, stage

    # Make player
    player =  [50, 350, 25, 25]
    player_vx = 0
    player_vy = 0
    player_speed = 10

    # Make player2
    player2 =  [50, 350, 25, 25]
    player2_vx = 0
    player2_vy = 0
    player2_speed = 10

    # Make player3
    player3 =  [56, 200, 12.5, 12.5]
    player3_vx = 0
    player3_vy = 0
    player3_speed = 12

    stage = START

    # make walls
    wall1 =  [300, 250, 200, 25]
    wall2 =  [300, 450, 300, 25]
    wall3 =  [100, 100, 25, 550]
    wall4 =  [500, 475, 25, 200]
    wall5 =  [300, -25, 25, 275]
    wall6 =  [100, 100, 450, 25]
    wall7 =  [200, 100, 25, 450]
    wall8 =  [0, 300, 100, 25]
    wall9 =  [100, 650, 500, 25]
    wall10 = [200, 550, 225, 25]
    wall11 = [200, 350, 400, 25]
    wall12 = [575, 0, 25, 350]
    wall13 = [775, 250, 2255, 25]
    wall14 = [775, 250, 25, 275]
    wall15 = [600, 550, 100, 25]
    wall16 = [675, 250, 25, 500]
    wall17 = [-25, 750, 1310, 25]
    wall18 = [775, 500, 350, 25]
    wall19 = [300, 150, 200, 25]
    wall20 = [0, -25, 25, 1030]
    wall21 = [900, 375, 335, 25]
    wall22 = [1030, -25, 25, 275]
    wall23 = [775, 625, 460, 25]
    wall24 = [1030, 875, 25, 135]
    wall25 = [802, 775, 25, 235]
    wall26 = [802, -25, 25, 150]
    wall27 = [1235, -25, 25, 1030]
    wall28 = [350, -25, 25, 125]
    wall29 = [400, -25, 25, 100]
    wall30 = [475, -25, 25, 100]
    wall31 = [525, -25, 25, 100]
    wall32 = [400, 50, 200, 25]
    wall33 = [350, 980, 25, 150]
    wall34 = [400, 980, 25, 150]
    wall35 = [475, 980, 25, 150]
    wall36 = [525, 980, 25, 150]
    wall37 = [300, 980, 25, 150]

    walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8,
             wall9, wall10, wall11, wall12, wall13, wall14, wall15,
             wall16, wall17, wall18, wall19, wall20, wall21, wall22,
             wall23, wall24, wall25, wall26, wall27, wall28, wall29,
             wall30, wall31, wall32, wall33, wall34, wall35, wall36,
             wall37]

    # Make coins
    coin1 = [300, 500, 25, 25]
    coin2 = [350, 200, 25, 25]
    coin3 = [150, 150, 25, 25]
    coin4 = [1150, 685, 25, 25]
    coin5 = [250, 150, 25, 25]
    coin6 = [437.5, 15, 25, 25]
    coin7 = [1150, 310, 25, 25]
    coin8 = [1130, 150, 25, 25]
    coin9 = [725, 150, 25, 25]
    coin10 = [250, 150, 25, 25]

    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8,
             coin9, coin10]

    # Make powerup
    powerup1 = [50, 250, 25, 25]

    powerups = [powerup1]

# Game loop
setup()
win = False
win2 = False
done = False
score = 0
score2 = 0
totalscore = 0
totalscore2 = 0
ticks = 0
time_remaining = 600
start_timer = False
twoplayer = False


while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_3:
                    actionsound.play(0)
                    start_timer = False
                    twoplayer = False
                    time_remaining = 600
                    score = 0
                    score2 = 0
                    stage = PLAYING
                elif event.key == pygame.K_2:
                    actionsound.play(0)
                    start_timer = False
                    twoplayer = True
                    time_remaining = 600
                    score = 0
                    score2 = 0
                    player = [55, 350, 12.5, 12.5]
                    player2 = [0, 0, 0, 0]
                    stage = PLAYING
                  
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()
                    
    if stage == PLAYING:                
        pressed = pygame.key.get_pressed()
        
        '''player 1'''
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

        '''player 2'''
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
        

        '''player 3'''
        up = pressed[pygame.K_i]
        down = pressed[pygame.K_k]
        left = pressed[pygame.K_j]
        right = pressed[pygame.K_l]

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
    '''ticks'''
    frame = ticks // 2
    
    ticks += 1

    if ticks >= 14:
        ticks = 0
        
    ''' get block edges (makes collision resolution easier to read) '''
    '''1'''
    top = player[1] 
    bottom = player[1] +player[3]
    left = player[0]
    right = player[0] + player[2]
    '''2'''
    top2 = player2[1] 
    bottom2 = player2[1] +player2[3]
    left2 = player2[0]
    right2 = player2[0] + player2[2]
    '''3'''
    top3 = player3[1] 
    bottom3 = player3[1] +player3[3]
    left3 = player3[0]
    right3 = player3[0] + player3[2]
    
    ''' if the block is moved completely off of the window, reposition it on the other side '''
    if bottom < 0:
        player[1] = HEIGHT
    elif top > HEIGHT:
        player[1] = 0 - player[3]

    if left > WIDTH:
        player[0] = 0 - player[2]
    elif right < 0:
        player[0] = WIDTH

    '''player 2 loop ocllision'''
    if bottom2 < 0:
        player2[1] = HEIGHT
    elif top2 > HEIGHT:
        player2[1] = 0 - player2[3]

    if left2 > WIDTH:
        player2[0] = 0 - player2[2]
    elif right2 < 0:
        player2[0] = WIDTH

    '''player 3 loop ocllision'''
    if bottom3 < 0:
        player3[1] = HEIGHT
    elif top3 > HEIGHT:
        player3[1] = 0 - player3[3]

    if left3 > WIDTH:
        player3[0] = 0 - player3[2]
    elif right3 < 0:
        player3[0] = WIDTH
        
    ''' move the players in horizontal direction '''
    '''1'''
    player[0] += player_vx
    '''2'''
    player2[0] += player2_vx
    '''3'''
    player3[0] += player3_vx
    ''' resolve collisions horizontally '''
    '''1'''
    for w in walls:
        if intersects.rect_rect(player, w):        
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]

    '''2'''
    for w in walls:
        if intersects.rect_rect(player2, w):        
            if player2_vx > 0:
                player2[0] = w[0] - player2[2]
            elif player2_vx < 0:
                player2[0] = w[0] + w[2]

    '''3'''
    for w in walls:
        if intersects.rect_rect(player3, w):        
            if player3_vx > 0:
                player3[0] = w[0] - player3[2]
            elif player3_vx < 0:
                player3[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    '''1'''
    player[1] += player_vy
    '''2'''
    player2[1] += player2_vy
    '''3'''
    player3[1] += player3_vy
    
    ''' resolve collisions vertically '''
    '''1'''
    for w in walls:
        if intersects.rect_rect(player, w):                    
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]

    '''2'''
    for w in walls:
        if intersects.rect_rect(player2, w):                    
            if player2_vy > 0:
                player2[1] = w[1] - player2[3]
            if player2_vy < 0:
                player2[1] = w[1] + w[3]

    '''3'''
    for w in walls:
        if intersects.rect_rect(player3, w):                    
            if player3_vy > 0:
                player3[1] = w[1] - player3[3]
            if player3_vy < 0:
                player3[1] = w[1] + w[3]


    '''players colliding'''
    if intersects.rect_rect(player, player3) and player_speed == 10:
        player_speed = 0
        actionsound2.play(0)
        
    elif intersects.rect_rect(player2, player3) and player2_speed == 10:
        player2_speed = 0
        actionsound2.play(0)
        
    if player2_speed + player_speed == 0:
        stage = END

    if player_speed == 0 and twoplayer == True:
        stage = END

    '''powerup interaction'''
    power_list = [p for p in powerups if intersects.rect_rect(player, p)]
    power_list2 = [p for p in powerups if intersects.rect_rect(player2, p)]

    for pow in power_list:
        powerups.remove(pow)
        player_speed = int(player_speed) * 1.2
        powersound.play(0)
        start_timer = True

    for pow in power_list2:
        powerups.remove(pow)
        player2_speed = int(player2_speed) * 1.2
        powersound.play(0)
        start_timer = True
    
    if start_timer == True:
        time_remaining -=1
        
    if time_remaining == 0 and player_speed == ((10) * 1.2):
        player_speed = 10
        powersound2.play(0)
        start_timer = False
    elif time_remaining == 0 and player2_speed == ((10) * 1.2):
        player2_speed = 10
        powersound2.play(0)
        start_timer = False
        

    ''' get the coins '''
    hit_list = [c for c in coins if intersects.rect_rect(player, c)]
    hit_list2 = [c for c in coins if intersects.rect_rect(player2, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        coinsound.play(0)
        score += 1
        totalscore +=1

    for hit in hit_list2:
        coins.remove(hit)
        coinsound.play(0)
        score2 += 1
        totalscore2 += 1

    if len(coins) == 0:
        stage = END
    
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BROWN)


    '''Rainbow'''
    if frame == 0:
        ROYGBIV = (255, 0, 0)
    if frame == 1:
        ROYGBIV = (255, 127.5, 0)
    if frame == 2:
        ROYGBIV = (255, 255, 0)
    if frame == 3:
        ROYGBIV = (0, 255, 0)
    if frame == 4:
        ROYGBIV = (0, 0, 255)
    if frame == 5:
        ROYGBIV = (127.5, 0, 255)
    if frame == 6:
        ROYGBIV = (255, 0, 255)

    '''Rainbow Player1'''
    if frame == 0 and player_speed == ((10) * 1.2):
        WHITE = (255, 0, 0)
    if frame == 1 and player_speed == ((10) * 1.2):
        WHITE = (255, 127.5, 0)
    if frame == 2 and player_speed == ((10) * 1.2):
        WHITE = (255, 255, 0)
    if frame == 3 and player_speed == ((10) * 1.2):
        WHITE = (0, 255, 0)
    if frame == 4 and player_speed == ((10) * 1.2):
        WHITE = (0, 0, 255)
    if frame == 5 and player_speed == ((10) * 1.2):
        WHITE = (127.5, 0, 255)
    if frame == 6 and player_speed == ((10) * 1.2):
        WHITE = (255, 0, 255)
    if player_speed == 10:
        WHITE = (255, 255, 255)
    if player_speed == 0 and len(coins) > 0:
        WHITE = (0, 0, 0)

    '''Rainbow Player2'''
    if frame == 0 and player2_speed == ((10) * 1.2):
        GRAY = (255, 0, 0)
    if frame == 1 and player2_speed == ((10) * 1.2):
        GRAY = (255, 127.5, 0)
    if frame == 2 and player2_speed == ((10) * 1.2):
        GRAY = (255, 255, 0)
    if frame == 3 and player2_speed == ((10) * 1.2):
        GRAY = (0, 255, 0)
    if frame == 4 and player2_speed == ((10) * 1.2):
        GRAY = (0, 0, 255)
    if frame == 5 and player2_speed == ((10) * 1.2):
        GRAY = (127.5, 0, 255)
    if frame == 6 and player2_speed == ((10) * 1.2):
        GRAY = (255, 0, 255)
    if player2_speed == 10:
        GRAY = (200, 200, 200)
    if player2_speed == 0 and len(coins) > 0:
        GRAY = (0, 0, 0)

        
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, GRAY, player2)
    pygame.draw.rect(screen, DGRAY, player3)

    for p in powerups:
        pygame.draw.rect(screen, ROYGBIV, p)
    

    for w in walls:
        pygame.draw.rect(screen, GREEN, w)
        
            
    for c in coins:
        pygame.draw.rect(screen, LGREEN, c)

    if stage == START:
        screen.blit(startscreen, (0,0))

    if stage == END:
        screen.blit(endscreen, (500,250))
        
    if stage == END and len(coins) == 0 and twoplayer == False:
        font = pygame.font.Font(None, 30)
        text1 = font.render("Coins collected!", 1, GREEN)
        text2 = font.render("White Block Round: " + str(score) + "!", 1, GREEN)
        text3 = font.render("Gray Block Round: " + str(score2) + "!", 1, GREEN)
        text4 = font.render("White Block Total: " + str(totalscore) + "!", 1, GREEN)
        text5 = font.render("Gray Block Total: " + str(totalscore2) + "!", 1, GREEN)
        screen.blit(text1, [580, 320])
        screen.blit(text2, [550, 390])
        screen.blit(text3, [545, 460])
        screen.blit(text4, [550, 530])
        screen.blit(text5, [550, 600])
        player2_speed = 0
        player_speed = 0
        player3_speed = 0
        
    elif stage == END and len(coins) > 0:
        font = pygame.font.Font(None, 80)
        text1 = font.render("Enemy", 1, GREEN)
        text2 = font.render("is", 1, GREEN)
        text3 = font.render("Winner", 1, GREEN)
        screen.blit(text1, [550, 340])
        screen.blit(text2, [620, 440])
        screen.blit(text3, [550, 540])
        player2_speed = 0
        player_speed = 0
        player3_speed = 0

    if stage == END and len(coins) == 0 and twoplayer == True:
        font = pygame.font.Font(None, 30)
        text1 = font.render("Coins collected!", 1, GREEN)
        text2 = font.render("White Block Round: " + str(score) + "!", 1, GREEN)
        text3 = font.render("White Block Total: " + str(totalscore) + "!", 1, GREEN)
        screen.blit(text1, [580, 320])
        screen.blit(text2, [545, 420])
        screen.blit(text3, [540, 520])
        player_speed = 0
        player3_speed = 0
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
