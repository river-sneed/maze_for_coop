# Imports
import pygame
import intersects
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 1250
HEIGHT = 950
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RAINBOW = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

# Make a player
player =  [200, 150, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 3


def rand_color(color):
    r = random.randint(color[0] - 5, color[0] + 5)
    b = random.randint(color[1] - 5, color[1] + 5)
    g = random.randint(color[2] - 5, color[2] + 5)

    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255

    return(color)




blocks = []
for x in range(0, WIDTH, 100):
    for y in range(0, HEIGHT, 100):
        b = [x, y, BLOCK_WIDTH, BLOCK_HEIGHT]
        blocks.append(b)

r = random.randint (0, 255)
g = random.randint (0, 255)
b = random.randint (0, 255)
block_color = [r, g, b]
    
coins = []
for x in range(50, (WIDTH-50), 100):
    for y in range(50, HEIGHT, 100):
        c = [x, y, BLOCK_WIDTH, BLOCK_HEIGHT]
        coins.append(c)

        
    

# make walls
wall1 =  [0, 0, WIDTH, BLOCK_HEIGHT]
wall2 =  [0, (HEIGHT-50), WIDTH, BLOCK_HEIGHT]
wall3 =  [0, 0, 50, WIDTH]
wall4 =  [(WIDTH-50), 0, BLOCK_WIDTH, HEIGHT]

walls = [wall1, wall2, wall3, wall4]




# Game loop
win = False
score = 0

done = False
 
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''


    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

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



    ''' resolve collisions horizontally '''
    for b in blocks:
        if intersects.rect_rect(player, b):        
            if player_vx > 0:
                player[0] = b[0] - player[2]
            elif player_vx < 0:
                player[0] = b[0] + b[2]

    
    ''' resolve collisions vertically '''
    for b in blocks:
        if intersects.rect_rect(player, b):                    
            if player_vy > 0:
                player[1] = b[1] - player[3]
            if player_vy < 0:
                player[1] = b[1] + b[3]


    ''' here is where you should resolve player collisions with screen edges '''





    ''' get the coins '''
    #coins = [c for c in coins if not intersects.rect_rect(player, c)]

    '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player, c):
            hit_list.append(c)
    '''
     
    hit_list = [c for c in coins if intersects.rect_rect(player, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score += 1
        print("sound!")
        

        
    

    
    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)

    for b in blocks:
        pygame.draw.rect(screen, block_color, b)

    
    # blit score on the screen somewhere
    
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, BLUE)
        screen.blit(text, [400, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
