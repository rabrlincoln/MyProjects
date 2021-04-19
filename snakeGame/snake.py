import pygame
from random import randrange

# Initialization
pygame.init()
clock=pygame.time.Clock()
#create Screen
size = 25
boardWidth = size * 10
boardHeight = size * 10

screen = pygame.display.set_mode((boardWidth, boardHeight))

# Title and Icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', size)
text = font.render('0', True, (0,0,0), (255,255,255)) # score
textRect = text.get_rect()
# Player
appleX = randrange(0, boardWidth - size)
appleY = randrange(0, boardHeight - size)
def player(body):
    for i in range(0, len(body)):
        pygame.draw.rect(screen, (0, 255, 0), (body[i][0], body[i][1], size, size))

def apple():
    pygame.draw.rect(screen, (255, 0, 0), (int(appleX /25) * 25, int(appleY /25) * 25, size, size))
# Game Loop
game = True
while game:
    running = True
    direction = "none"
    score = 0
    length = 1
    playerX = boardWidth / 2
    playerY = boardHeight / 2
    body = [[int(playerX/25) * 25, int(playerY/25) * 25]]
    move = [int(playerX /25) * 25, int(playerY /25) * 25]
    speed = 10

    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if direction != "up":
                        direction = "down"
                if event.key == pygame.K_UP:
                    if direction != "down":
                        direction = "up"
                if event.key == pygame.K_LEFT:
                    if direction != "right":
                        direction = "left"
                if event.key == pygame.K_RIGHT:
                    if direction != "left":
                        direction = "right"
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            #         changeY = 0
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         changeX = 0
        if direction == "left":
            playerX -= speed
        if direction == "right":
            playerX += speed
        if direction == "down":
            playerY += speed
        if direction == "up":
            playerY -= speed

        if int(playerX/25) * 25 < 0:
            playerX = boardWidth - size
        if int(playerX/25) * 25 > boardWidth - size:
            playerX = 0
        if int(playerY/25) * 25 < 0:
            playerY = boardHeight - size
        if int(playerY/25) * 25 > boardHeight - size:
            playerY = 0
        for i in body :
            if i == [int(playerX/25) * 25, int(playerY/25) * 25] and length > 1:
                running = False
        if move != [int(playerX/25) * 25, int(playerY/25) * 25]:
            body.append(move)
            move = [int(playerX/25) * 25, int(playerY/25) * 25]
        if int(playerX/25) * 25 == int(appleX/25) * 25 and int(playerY/25) * 25 == int(appleY/25) * 25:
            appleX = randrange(0, boardWidth - size)
            appleY = randrange(0, boardHeight - size)
            score += 1
            length +=1
        if len(body) > length:
            body.pop(0)
        apple()
        player(body)

        text = font.render(str(score), True, (0,0,0), (255,255,255))
        screen.blit(text, textRect)
        clock.tick(30)
        pygame.display.update()
