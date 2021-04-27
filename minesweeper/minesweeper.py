import pygame
from random import randrange
# Initialization
pygame.init()

#create Screen
GRAY = (50, 50, 50)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
LIGHTGRAY = (100, 100, 100)
GREEN = (0, 255, 0)
size = 25
width = 16 * size
height = 16 * size
numBombs = 40
screen = pygame.display.set_mode((width, height))

# Title and Icon
pygame.display.set_caption("Mindstorm")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 32)

def adjacentCount(randBombs, i, j):
    count = 0
    for bomb in randBombs:
        if i == bomb[0]:
            if j == bomb[1]:
                count = "B"
                return count
            if j + size == bomb[1]:
                count += 1
            if j - size == bomb[1]:
                count += 1
        if i + size == bomb[0]:
            if j == bomb[1]:
                count += 1
            if j + size == bomb[1]:
                count += 1
            if j - size == bomb[1]:
                count += 1
        if i - size == bomb[0]:
            if j == bomb[1]:
                count += 1
            if j + size == bomb[1]:
                count += 1
            if j - size == bomb[1]:
                count += 1
    return count

def reveal(i, j):
    grid[int(i / size)][int(j / size)][0] = True
    if grid[int(i / size)][int(j / size)][1] == 0:
        pygame.draw.rect(screen,LIGHTGRAY,[i,j, size, size])
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not any([x == 0 and y == 0, i + x*size < 0, j + y*size < 0, i + x*size >= width, j + y*size >= height]):
                    if grid[int(i / size + x)][int(j / size + y)][0] != True:
                        reveal(i+(x*size), j+(y*size))
    else:
        text = font.render(str(grid[int(i / size)][int(j/size)][1]), True, BLACK, GRAY)
        screen.blit(text, (i, j))

def drawSquares(mouse, grid):
    for i in range(0, width, size):
        for j in range(0, height, size):
            if grid[int(i / size)][int(j / size)][0]:
                # pygame.draw.rect(screen,RED,[i,j, size, size])
                if grid[int(i /size)][int(j/size)][1] == 0:
                    pygame.draw.rect(screen, LIGHTGRAY, [i, j, size, size])
                else:
                    text = font.render(str(grid[int(i / size)][int(j / size)][1]), True, BLACK, GRAY)
                    screen.blit(text, (i, j))
            elif mouse[0][0] - size < i < mouse[0][0] and mouse[0][1] - size< j < mouse[0][1]:
                if mouse[1]:
                    # pygame.draw.rect(screen,RED,[i,j, size, size])
                    reveal(i, j)
                    # grid[int(i / size)][int(j / size)][0] = True
                    # if grid[int(i / size)][int(j / size)][1] == 0:
                    #     pygame.draw.rect(screen, RED, [i, j, size, size])
                    #     for x in range(-1, 2):
                    #         for y in range(-1, 2):
                    #             if x != 0 and y != 0:
                    #                 reveal(i+x, j+y)
                    # elif grid[int(i / size)][int(j / size)][1] == "B":
                    #     return False
                    # else:
                    #     text = font.render(str(grid[int(i / size)][int(j / size)][1]), True, BLACK, GRAY)
                    #     screen.blit(text, (i, j))
                else:
                    pygame.draw.rect(screen,GRAY,[i,j, size, size])
                pygame.draw.rect(screen,LIGHTGRAY,[i,j, size, size], 1)
            else:
                pygame.draw.rect(screen,GRAY,[i,j, size, size])
                pygame.draw.rect(screen,BLACK,[i,j, size, size], 1)
def hitBomb(grid):
    for i in range(0, width, size):
        for j in range(0, height, size):
            if grid[int(i / size)][int(j / size)][0] and grid[int(i / size)][int(j / size)][1] == "B":
                return True
    return False


def won(grid):
    for i in range(0, width, size):
        for j in range(0, height, size):
            if not grid[int(i / size)][int(j / size)][0] and grid[int(i / size)][int(j / size)][1] != "B": # if square not revealed and not bomb
                return False
    return True


def makeBombs():
    bombs = []
    while len(bombs) < numBombs:
        i = [randrange(0, width, size), randrange(0, height, size)]
        if i not in bombs:
            bombs.append(i)
    return bombs
def makeGrid():
    randBombs = makeBombs()
    grid = []
    for i in range(0, width, size):
        grid.append([])
        for j in range(0, height, size):
            grid[int(i/size)].append([False, adjacentCount(randBombs, i, j)])
    return grid


# Game Loop
running = True
grid = makeGrid()


while running:
    screen.fill(GRAY)
    pressed= False
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            pressed = False
    mouse = [pos, pressed]
    drawSquares(mouse, grid)
    if won(grid):
        screen.fill(GREEN)
    pygame.display.update()
    if hitBomb(grid):
        running = False
