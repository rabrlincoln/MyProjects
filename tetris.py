# left and right arrows move shape left and right
# up arrow turns shape clockwise
# down arrow soft pushes shape down
# space bar hard pushes shape down
# z key rotates shape counterclockwise
# x key rotates shape clockwise
# c holds shape to right and brings shape in hold to current

import pygame
from random import randrange

# Initialization
pygame.init()
# constants
SIZE = 25
COLORS = [[255, 100, 0], [255, 0, 0], [255, 0, 255], [0, 255, 0], [0, 255, 255], [0, 0, 255], [255, 255, 0]]
BOXES = [[[2], [0, 1, 2]], [[0], [0, 1], [1]], [[0], [0, 1], [0]], [[1], [0, 1], [0]], [[0], [0], [0], [0]],
         [[0, 1, 2], [2]], [[0, 1], [0, 1]]]

# Screen, Title, Icon, Font
screen = pygame.display.set_mode((SIZE * 17, SIZE * 20))
clock = pygame.time.Clock()
pygame.display.set_caption("Tetris")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', SIZE)
text = font.render('0', True, (0, 0, 0), (255, 255, 255))  # score
textRect = text.get_rect()


# SHAPE functions return points of polygons, sets box, width, height

def square(x, y, rotation):
    width = SIZE * 2
    height = 2 * SIZE
    box = [[0, 1], [0, 1]]
    return [[(x, y), (x, y - 2 * SIZE), (x + 2 * SIZE, y - 2 * SIZE), (x + 2 * SIZE, y)], box, width, height]


def Lshape(x, y, rotation):
    if rotation == 3:
        # up
        width = SIZE
        height = 3 * SIZE
        box = [[2], [0, 1, 2]]
        return [
            [(x, y), (x, y - 2 * SIZE), (x - SIZE, y - 2 * SIZE), (x - SIZE, y - 3 * SIZE), (x + SIZE, y - 3 * SIZE),
             (x + SIZE, y)], box, width, height]

    if rotation == 1:
        # down
        width = SIZE * 2
        height = 3 * SIZE
        box = [[0, 1, 2], [0]]
        return [[(x, y), (x, y - 3 * SIZE), (x + SIZE, y - 3 * SIZE), (x + SIZE, y - SIZE), (x + 2 * SIZE, y - SIZE),
                 (x + 2 * SIZE, y)], box, width, height]

    if rotation == 2:
        # left
        width = SIZE * 3
        height = SIZE * 2
        box = [[0, 1], [1], [1]]
        return [
            [(x, y), (x, y - 2 * SIZE), (x + 3 * SIZE, y - 2 * SIZE), (x + 3 * SIZE, y - SIZE), (x + SIZE, y - SIZE),
             (x + SIZE, y)], box, width, height]

    if rotation == 4:
        # right
        width = SIZE * 3
        height = SIZE * 2
        box = [[0], [0], [0, 1]]
        return [[(x, y), (x, y - SIZE), (x + 2 * SIZE, y - SIZE), (x + 2 * SIZE, y - 2 * SIZE),
                 (x + 3 * SIZE, y - 2 * SIZE), (x + 3 * SIZE, y)], box, width, height]


def Rshape(x, y, rotation):
    if rotation == 1:
        # up
        width = SIZE * 2
        height = SIZE * 3
        box = [[0, 1, 2], [2]]
        return [[(x, y), (x, y - 3 * SIZE), (x + 2 * SIZE, y - 3 * SIZE), (x + 2 * SIZE, y - 2 * SIZE),
                 (x + SIZE, y - 2 * SIZE), (x + SIZE, y)], box, width, height]
    if rotation == 3:
        # down
        width = SIZE * 2
        height = SIZE * 3
        box = [[0], [0, 1, 2]]
        return [[(x, y), (x, y - SIZE), (x + SIZE, y - SIZE), (x + SIZE, y - 3 * SIZE), (x + 2 * SIZE, y - 3 * SIZE),
                 (x + 2 * SIZE, y)], box, width, height]

    if rotation == 4:
        # left
        width = SIZE * 3
        height = SIZE * 2
        box = [[0, 1], [0], [0]]
        return [[(x, y), (x, y - 2 * SIZE), (x + SIZE, y - 2 * SIZE), (x + SIZE, y - SIZE), (x + 3 * SIZE, y - SIZE),
                 (x + 3 * SIZE, y)], box, width, height]

    if rotation == 2:
        # right
        width = SIZE
        height = SIZE * 2
        box = [[1], [1], [0, 1]]
        return [
            [(x, y), (x, y - SIZE), (x - 2 * SIZE, y - SIZE), (x - 2 * SIZE, y - 2 * SIZE), (x + SIZE, y - 2 * SIZE),
             (x + SIZE, y)], box, width, height]


def line(x, y, rotation):
    if rotation == 1 or rotation == 3:
        # down
        width = SIZE * 4
        height = SIZE
        box = [[0], [0], [0], [0]]
        return [[(x, y), (x, y - SIZE), (x + 4 * SIZE, y - SIZE), (x + 4 * SIZE, y)], box, width, height]

    if rotation == 2 or rotation == 4:
        # up
        width = SIZE
        height = SIZE * 4
        box = [[0, 1, 2, 3]]
        return [[(x, y), (x, y - 4 * SIZE), (x + SIZE, y - 4 * SIZE), (x + SIZE, y)], box, width, height]


def Zshape(x, y, rotation):
    if rotation == 1 or rotation == 3:
        width = SIZE * 2
        height = SIZE * 2
        box = [[1], [0, 1], [0]]
        return [[(x, y), (x, y - SIZE), (x - SIZE, y - SIZE), (x - SIZE, y - 2 * SIZE), (x + SIZE, y - 2 * SIZE),
                 (x + SIZE, y - SIZE), (x + 2 * SIZE, y - SIZE), (x + 2 * SIZE, y)], box, width, height]

    if rotation == 2 or rotation == 4:
        width = SIZE * 2
        height = SIZE * 3
        box = [[0, 1], [1, 2]]
        return [[(x, y), (x, y - 2 * SIZE), (x + SIZE, y - 2 * SIZE), (x + SIZE, y - 3 * SIZE),
                 (x + 2 * SIZE, y - 3 * SIZE), (x + 2 * SIZE, y - SIZE), (x + SIZE, y - SIZE), (x + SIZE, y)], box,
                width, height]


def Sshape(x, y, rotation):
    if rotation == 1 or rotation == 3:
        width = SIZE * 3
        height = SIZE * 2
        box = [[0], [0, 1], [1]]
        return [[(x, y), (x, y - SIZE), (x + SIZE, y - SIZE), (x + SIZE, y - 2 * SIZE), (x + 3 * SIZE, y - 2 * SIZE),
                 (x + 3 * SIZE, y - SIZE), (x + 2 * SIZE, y - SIZE), (x + 2 * SIZE, y)], box, width, height]

    if rotation == 2 or rotation == 4:
        width = SIZE
        height = SIZE * 3
        box = [[1, 2], [0, 1]]
        return [[(x, y), (x, y - SIZE), (x - SIZE, y - SIZE), (x - SIZE, y - 2 * SIZE), (x - SIZE, y - 3 * SIZE),
                 (x, y - 3 * SIZE), (x, y - 2 * SIZE), (x + SIZE, y - 2 * SIZE), (x + SIZE, y - SIZE), (x + SIZE, y)],
                box, width, height]


def Tshape(x, y, rotation):
    if rotation == 1:
        # down
        width = SIZE * 3
        height = SIZE * 2
        box = [[0], [0, 1], [0]]
        return [[(x, y), (x, y - SIZE), (x + SIZE, y - SIZE), (x + SIZE, y - 2 * SIZE), (x + 2 * SIZE, y - 2 * SIZE),
                 (x + 2 * SIZE, y - SIZE), (x + 3 * SIZE, y - SIZE), (x + 3 * SIZE, y)], box, width, height]

    if rotation == 2:
        # left
        width = SIZE * 2
        height = SIZE * 3
        box = [[0, 1, 2], [1]]
        return [[(x, y), (x, y - 3 * SIZE), (x + SIZE, y - 3 * SIZE), (x + SIZE, y - 2 * SIZE),
                 (x + 2 * SIZE, y - 2 * SIZE), (x + 2 * SIZE, y - SIZE), (x + SIZE, y - SIZE), (x + SIZE, y)], box,
                width, height]

    if rotation == 3:
        # up
        width = SIZE * 2
        height = SIZE * 2
        box = [[1], [0, 1], [1]]
        return [[(x, y), (x, y - SIZE), (x - SIZE, y - SIZE), (x - SIZE, y - 2 * SIZE), (x + 2 * SIZE, y - 2 * SIZE),
                 (x + 2 * SIZE, y - SIZE), (x + SIZE, y - SIZE), (x + SIZE, y)], box, width, height]

    if rotation == 4:
        # right
        width = SIZE
        height = SIZE * 3
        box = [[1], [0, 1, 2]]
        return [[(x, y), (x, y - SIZE), (x - SIZE, y - SIZE), (x - SIZE, y - 2 * SIZE), (x, y - 2 * SIZE),
                 (x, y - 3 * SIZE), (x + SIZE, y - 3 * SIZE), (x + SIZE, y)], box, width, height]


SHAPE = [Lshape, Sshape, Tshape, Zshape, line, Rshape, square]


def draw(state):
    text = font.render(str(state['score']), True, (0, 0, 0), (255, 255, 255))
    screen.blit(text, textRect)
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, SIZE * 10 + 1, SIZE * 20), width=1)
    pygame.draw.rect(screen, (0, 0, 0), (SIZE * 11, SIZE * 3, SIZE * 5, SIZE * 5), width=1)
    pygame.draw.polygon(screen, COLORS[state['num']],
                        SHAPE[state['num']](int(state['x'] / SIZE) * SIZE, int(state['y'] / SIZE) * SIZE,
                                            state['rotation'])[0])
    for i in range(0, 10):
        for j in range(0, 20):
            if state['cubes'][i][j]:
                pygame.draw.rect(screen, (0, 0, 0), (i * SIZE, (19 - j) * SIZE, SIZE, SIZE))
    pygame.display.update()


def getInput(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state['playing'] = False
            state['game'] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_x:
                state['rotation'] += 1
                if state['rotation'] > 4:
                    state['rotation'] = 1
            if event.key == pygame.K_z:
                state['rotation'] -= 1
                if state['rotation'] < 1:
                    state['rotation'] = 4
            if event.key == pygame.K_DOWN:
                state['changeY'] += state['speed'] + 2
            if event.key == pygame.K_LEFT:
                state['changeX'] = - 7
            if event.key == pygame.K_RIGHT:
                state['changeX'] = 7
            if event.key == pygame.K_SPACE:
                state['space'] = True

            if event.key == pygame.K_c:
                if state['first']:
                    state['second'] = True
                    state['lastShape'] = state['holdShape']
                state['first'] = True
                state['holdShape'] = SHAPE[state['num']]
                state['holdColor'] = COLORS[state['num']]
                state['holdBox'] = BOXES[state['num']]
                state['hold'] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                state['changeX'] = 0
            if event.key == pygame.K_DOWN:
                state['changeY'] = 0
            if event.key == pygame.K_c:
                state['hold'] = False
    return state


def clearline(grid):
    for column in range(0, 20):
        full = True
        for row in range(0, 10):
            if not grid[row][column]:
                full = False
                break
        if full:
            return column
    return False


def blockAtTop(grid):
    for i in range(0, 10):
        if grid[i][19]:
            return True
    return False


def bound(box):
    for row in range(0, len(box)):
        for column in box[row]:
            if column == 0:
                return row * SIZE
    return 0


def highestInRow(grid, row, box):
    highest = -1
    border = bound(box)
    for line in range(0, len(box)):
        for i in range(0, 20):
            if grid[int((row - border) / SIZE) + line][19 - i] and 19 - i > highest:
                highest = 19 - i
                break
    return highest


def reset():
    state['num'] = randrange(0, 7)
    state['y'] = 0
    state['x'] = SIZE * 10 / 2
    state['rotation'] = 1


def atBottom(state, box, border):
    condition = [state['y'] > 20 * SIZE]
    for i in range(0, len(box)):
        condition.append(state['cubes'][i + int((state['x'] - border) / SIZE)][box[i][0] + 19 - int(state['y'] / SIZE)])

    if any(condition):  # when hits another block or the bottom of the screen or hold
        # add SHAPE to black cubes
        if not state['hold']:
            for row in range(0, len(box)):
                for column in box[row]:
                    state['cubes'][int((state['x'] - border) / SIZE) + row][20 - int(state['y'] / SIZE) + column] = True
        reset()
    if state['hold']:
        reset()
        if state['second']:
            state['num'] = SHAPE.index(state['lastShape'])


def outOfBounds(border, x, width):
    if x < border:
        x = border
    elif x > SIZE * 10 - width:
        x = SIZE * 10 - width
    return x


def spaceBar(box):
    if state['space']:
        highest = highestInRow(state['cubes'], state['x'], box)
        state['y'] = 20 * SIZE - (highest + 1) * SIZE
        state['space'] = False


def updateState(state):
    getInput(state)
    state['x'] += state['changeX']
    state['y'] += state['changeY']
    box = SHAPE[state['num']](state['x'], state['y'], state['rotation'])[1]
    # height = SHAPE[state['num']](state['x'], state['y'], state['rotation'])[2]
    width = SHAPE[state['num']](state['x'], state['y'], state['rotation'])[2]
    # keep SHAPE from going out of left and right border
    border = bound(box)
    state['x'] = outOfBounds(border, state['x'], width)

    # when space bar pressed
    spaceBar(box)
    atBottom(state, box, border)
    if clearline(state['cubes']) is not False:
        state['score'] += 1
        state['speed'] += 1
        for i in range(0, 10):
            state['cubes'][i].pop(clearline(state['cubes']))
            state['cubes'][i].append(False)

    # If the a cube is at the top of the screen end the game
    if blockAtTop(state['cubes']):
        state['playing'] = False

    state['y'] += state['speed']
    return state


# Game Loop
state = {'game': True}
while state['game']:
    onecubes = []
    for i in range(0, 12):
        onecubes.append([])
        for j in range(0, 30):
            onecubes[i].append(False)
    state = {'game': True,
             'playing': True,
             'num': randrange(0, 6),
             'rotation': 1, 'x': SIZE * 10 / 2,
             'y': 0,
             'changeX': 0,
             'changeY': 0,
             'cubes': onecubes,
             'score': 0,
             'speed': 2,
             'first': False,
             'hold': False,
             'second': False,
             'space': False,
             'holdShape': None,
             'lastShape': None,
             'holdColor': None,
             'holdBox': None
             }
    while state['playing']:

        screen.fill((255, 255, 255))
        if state['first']:
            pygame.draw.polygon(screen, state['holdColor'], state['holdShape'](SIZE * 12, SIZE * 7, 1)[0])
        updateState(state)
        clock.tick(30)
        draw(state)
