#MAZE
#RIVER SNEED
#Jan 12 2016


# Imports
import pygame
import intersects
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
TITLE = "PEPE MAZE"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255, 0)
GREEN = (0,255,0)
BLUE = (8,8,253)
ORANGE = (255,86,24)
LAVENDER = (196,150,255)
PINK = (248,50,255)
TEAL = (48,232,183)
SWEET_PEPE_GREEN = (104,152,76)
SWEET_PEPE_BLUE = (35,74,252)
SWEET_PEPE_RED = (169,106,64)



# stages
START = 0
PLAYING = 1
END = 2

startscreen = pygame.image.load("splashscreen.jpg")
endscreen = pygame.image.load("endscreen.jpg")


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
    
def setup():
    global walls, not_reals, invisibles, coins, supers, teleporters, fake_walls, player, player_vx, player_vy, player_speed,player2, player2_vx, player2_vy, player2_speed, player3, player3_vx, player3_vy,player3_speed, stage

    # Make player
    player =  [225, 337, 25, 25]
    player_vx = 0
    player_vy = 0
    player_speed = 5

    # Make player2
    player2 =  [487, 125, 25, 25]
    player2_vx = 0
    player2_vy = 0
    player2_speed = 5

    # Make player3
    player3 =  [725, 337, 25, 25]
    player3_vx = 0
    player3_vy = 0
    player3_speed = 5

    stage = START

    # make walls
    #section 1
    wall1 =  [0,0,1000,25]
    wall2 =  [0,0,25,700]
    wall3 =  [975,0,25,700]
    wall4 =  [0,675,1000,25]
    wall5 =  [75,75,75,75]
    wall6 =  [200,25,75,75]
    wall7 =  [75,200,50,50]
    wall8 =  [200,150,75,100]
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

    #make invisible walls
    #section 1
    invisible1 = [75,25,25,50]
    invisible2 = [125,150,25,50]
    invisible3 = [250,250,25,50]
    #no section 2
    #section 3
    invisible4 = [700,400,25,50]
    invisible5 = [800,400,25,50]
    invisible6 = [725,450,75,50]
    invisible7 = [875,500,50,25]
    invisible8 = [650,525,50,25]
    invisible9 = [825,525,50,25]
    invisible10 = [550,550,50,25]
    invisible11 = [725,575,75,50]
    invisible12 = [775,625,50,50]
    #section 4
    invisible13 = [700,25,25,50]
    invisible14 = [725,250,25,50]

    invisibles = [invisible1, invisible2, invisible3, invisible4, invisible5, invisible6, invisible7,
                  invisible8, invisible9, invisible10, invisible11, invisible12, invisible13, invisible14]
       
    
    
             
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
    coin16 = [825,400,50,50]
    coin17 = [925,535,50,50]
    coin18 = [550,575,50,50]
    coin19 = [725,625,50,50]
    coin20 = [825,625,50,50]
    #section 4
    coin21 = [600,250,50,50]
    coin22 = [725,250,50,50]
    coin23 = [750,25,50,50]
    coin24 = [825,25,50,50]
    coin25 = [850,250,50,50]
    coin26 = [925,200,50,50]



    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
             coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20,
             coin21, coin22, coin23, coin24, coin25, coin26]

    #make fake coins
    #no section 1
    #no section 2
    #section 3
    not_real1 = [700,400,50,50]
    not_real2 = [775,400,50,50]
    #section 4
    not_real3 = [550,25,50,50]
    not_real4 = [550,175,50,50]
    not_real5 = [550,125,50,50]
    not_real6 = [550,75,50,50]
    not_real7 = [600,25,50,50]
    not_real8 = [650,25,50,50]

    not_reals = [not_real1, not_real2, not_real3, not_real4,
                 not_real5, not_real6, not_real7, not_real8]
    
    
    #Make teleporters
    teleporter1 = [400,250,50,50]
    teleporter2 = [175,525,50,50]
    teleporter3 = [550,400,50,50]
    teleporter4 = [550,250,50,50]

    
    teleporters = [teleporter1, teleporter2, teleporter3, teleporter4]

    #make super
    super1 = [475,325,50,50]

    supers = [super1]


    #Make fake walls
    fake_wall1 = [175,525,100,50]
    fake_wall2 = [275,525,100,100]
    fake_wall3 = [650,125,50,125]
    fake_wall4 = [700,125,225,50]

    fake_walls = [fake_wall1, fake_wall2, fake_wall3, fake_wall4]

# Game loop
setup()
win = False
win2 = False
done = False
score = 0
score2 = 0
score3 = 0
totalscore = 0
totalscore2 = 0
totalscore3 = 0
ticks = 0
time_remaining = 600
start_timer = False



while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_SPACE:
                    start_timer = False
                    time_remaining = 600
                    score = 0
                    score2 = 0
                    score3 = 0
                    stage = PLAYING

            elif stage == END:
                if event.key == pygame.K_RETURN:
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
    
        
    ''' move the players in horizontal direction '''
    '''1'''
    player[0] += player_vx
    '''2'''
    player2[0] += player2_vx
    '''3'''
    player3[0] += player3_vx
    ''' resolve collisions horizontally for walls'''
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


    '''resolve collisions horizontally for invisible walls'''
    '''1'''
    for i in invisibles:
        if intersects.rect_rect(player, i):        
            if player_vx > 0:
                player[0] = i[0] - player[2]
            elif player_vx < 0:
                player[0] = i[0] + i[2]

    '''2'''
    for i in invisibles:
        if intersects.rect_rect(player2, i):        
            if player2_vx > 0:
                player2[0] = i[0] - player2[2]
            elif player2_vx < 0:
                player2[0] = i[0] + i[2]

    '''3'''
    for i in invisibles:
        if intersects.rect_rect(player3, i):        
            if player3_vx > 0:
                player3[0] = i[0] - player3[2]
            elif player3_vx < 0:
                player3[0] = i[0] + i[2]
    ''' move the player in vertical direction '''
    '''1'''
    player[1] += player_vy
    '''2'''
    player2[1] += player2_vy
    '''3'''
    player3[1] += player3_vy
    
    ''' resolve collisions vertically for walls'''
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



    ''' resolve collistions vertically for invisibles'''
    for i in invisibles:
        if intersects.rect_rect(player, i):                    
            if player_vy > 0:
                player[1] = i[1] - player[3]
            if player_vy < 0:
                player[1] = i[1] + i[3]

    '''2'''
    for i in invisibles:
        if intersects.rect_rect(player2, i):                    
            if player2_vy > 0:
                player2[1] = i[1] - player2[3]
            if player2_vy < 0:
                player2[1] = i[1] + i[3]

    '''3'''
    for i in invisibles:
        if intersects.rect_rect(player3, i):                    
            if player3_vy > 0:
                player3[1] = i[1] - player3[3]
            if player3_vy < 0:
                player3[1] = i[1] + i[3] 
    '''1'''
    for t in teleporters:
        if intersects.rect_rect(player, t):
            z = random.randint(0,3)
            #put player into middle
            if z == 0:
                player = [37, 337, 25, 25]
            elif z == 1:
                player = [487, 637, 25, 25]
            elif z == 2:
                player = [937, 337, 25, 25]
            elif z == 3:
                player = [487, 37, 25, 25]


    '''1'''
    for s in supers:
        if intersects.rect_rect(player, s):
            z = random.randint(0,3)
            #put player into blocks
            if z == 0:
                player = [37, 37, 25, 25]
            elif z == 1:
                player = [37, 637, 25, 25]
            elif z == 2:
                player = [937, 637, 25, 25]
            elif z == 3:
                player = [937, 37, 25, 25]

    '''2'''
    for t in teleporters:
        if intersects.rect_rect(player2, t):
            z = random.randint(0,3)
            #put player into middle
            if z == 0:
                player2 = [37, 337, 25, 25]
            elif z == 1:
                player2 = [487, 637, 25, 25]
            elif z == 2:
                player2 = [937, 337, 25, 25]
            elif z == 3:
                player2 = [487, 37, 25, 25]


    '''2'''
    for s in supers:
        if intersects.rect_rect(player2, s):
            z = random.randint(0,3)
            #put player into blocks
            if z == 0:
                player2 = [37, 37, 25, 25]
            elif z == 1:
                player2 = [37, 637, 25, 25]
            elif z == 2:
                player2 = [937, 637, 25, 25]
            elif z == 3:
                player2 = [937, 37, 25, 25]


    '''3'''
    for t in teleporters:
        if intersects.rect_rect(player3, t):
            z = random.randint(0,3)
            #put player into middle
            if z == 0:
                player3 = [37, 337, 25, 25]
            elif z == 1:
                player3 = [487, 637, 25, 25]
            elif z == 2:
                player3 = [937, 337, 25, 25]
            elif z == 3:
                player3 = [487, 37, 25, 25]


    '''3'''
    for s in supers:
        if intersects.rect_rect(player3, s):
            z = random.randint(0,3)
            #put player into blocks
            if z == 0:
                player3 = [37, 37, 25, 25]
            elif z == 1:
                player3 = [37, 637, 25, 25]
            elif z == 2:
                player3 = [937, 637, 25, 25]
            elif z == 3:
                player3 = [937, 37, 25, 25]

            
                
            
            




    ''' get the coins '''
    hit_list = [c for c in coins if intersects.rect_rect(player, c)]
    hit_list2 = [c for c in coins if intersects.rect_rect(player2, c)]
    hit_list3 = [c for c in coins if intersects.rect_rect(player3, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score += 1
        totalscore +=1
        

    for hit in hit_list2:
        coins.remove(hit)
        score2 += 1
        totalscore2 += 1

        
    for hit in hit_list3:
        coins.remove(hit)
        score3 += 1
        totalscore3 += 1

        
    if len(coins) == 0:
        stage = END
    
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(LAVENDER)

     
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, YELLOW, player2)
    pygame.draw.rect(screen, BLUE, player3)


    

    for w in walls:
        pygame.draw.rect(screen, PINK, w)

    for s in supers:
        pygame.draw.rect(screen, ((random.randint(0,255)),(random.randint(0,255)),random.randint(0,255)), s)

    for i in invisibles:
        pygame.draw.rect(screen, LAVENDER, i)

    for t in teleporters:
        pygame.draw.rect(screen, TEAL, t)        

    for n in not_reals:
        pygame.draw.rect(screen, YELLOW, n)
    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)

    for f in fake_walls:
        pygame.draw.rect(screen, PINK, f)

    if stage == START:
        screen.fill(BLACK)
        screen.blit(startscreen, (0,0))

    if stage == PLAYING:
        font = pygame.font.Font(None,40)
        p1_rscore_print = font.render("P1  Round: " + str(score), 1, RED)
        p2_rscore_print = font.render("P2 Round: " + str(score2), 1, YELLOW)
        p3_rscore_print = font.render("P3 Round: " + str(score3), 1, BLUE)
        p1_tscore_print = font.render("P1 Total: " + str(totalscore), 1, RED)
        p2_tscore_print = font.render("P2 Total: " + str(totalscore2), 1, YELLOW)
        p3_tscore_print = font.render("P3 Total: " + str(totalscore3), 1, BLUE)
        screen.blit(p1_rscore_print, [100,700])
        screen.blit(p2_rscore_print, [400,700])
        screen.blit(p3_rscore_print, [700,700])
        screen.blit(p1_tscore_print, [100,750])
        screen.blit(p2_tscore_print, [400,750])
        screen.blit(p3_tscore_print, [700,750])
        

    if stage == END:
        screen.fill(BLACK)

        
    if stage == END and len(coins) == 0:
        font = pygame.font.Font(None, 45)
        font2 = pygame.font.Font(None, 120)
        text1 = font.render("Coins collected", 1, WHITE)
        text2 = font.render("P1 Round School: " + str(score), 1, RED)
        text3 = font.render("P2 Round School: " + str(score2), 1, YELLOW)
        text4 = font.render("P3 Round School: " + str(score3), 1, BLUE)        
        text5 = font.render("P1 Total School: " + str(totalscore), 1, RED)
        text6 = font.render("P2 Total School: " + str(totalscore2), 1, YELLOW)
        text7 = font.render("P3 Total School: " + str(totalscore3), 1, BLUE)
        text8 = font.render("Press Enter to Start Next Round", 1, WHITE)
        screen.blit(text1, [425, 25])
        screen.blit(text2, [100, 200])
        screen.blit(text3, [400, 200])
        screen.blit(text4, [700, 200])
        screen.blit(text5, [100, 400])
        screen.blit(text6, [400, 400])
        screen.blit(text7, [700, 400])
        screen.blit(text8, [250, 550])
        
        player2_speed = 0
        player_speed = 0
        player3_speed = 0
        



    
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
