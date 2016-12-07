# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1250
HEIGHT = 950
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
WALL_COLOR = (random.randint(0,255),random.randint(0,255),random.randint)

# Make a player
player =  [200, 150, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 3

def make_maze(w = 200 , h = 100):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [[MAZE_WALL, SPACE, SPACE] * w + [MAZE_WALL] for _ in range(h)] + [[]]
    hor = [[MAZE_WALL, SPACE, SPACE] * w + [MAZE_WALL] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = [MAZE_WALL, SPACE, SPACE]
            if yy == y: ver[y][max(x, xx)] = [SPACE, SPACE, SPACE]
            walk(xx, yy)
            
    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s



MAZE_WALL = pygame.draw.rect(screen, WALL_COLOR, [25, 25, 25, 25])
SPACE = pygame.draw.rect(screen, BLACK, [25, 25, 25, 25])

if __name__ == '__main__':
    print(make_maze())
    
"""# make walls
wall1 =  [300, 275, 200, 25]
wall2 =  [400, 450, 200, 25]
wall3 =  [100, 100, 25, 200]

walls = [wall1, wall2, wall3]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]

coins = [coin1, coin2, coin3]"""


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

"""        
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

"""        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)


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
