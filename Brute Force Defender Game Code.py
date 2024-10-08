import pygame
import math
import random

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((1000, 600))

background = pygame.image.load('resized background.jpg')

# Title Icon
pygame.display.set_caption("Brute Force Defender")
icon = pygame.image.load('hacker.png')
pygame.display.set_icon(icon)

# Moving NPC Enemy

movingNpcImg = pygame.image.load('evil.png')
movingNpcX = random.randint(5, 1000)
movingNpcY = random.randint(50, 300)
movingNpcX_change = 0.5
movingNpcY_change = 50


def movingNpc(x, y):
    screen.blit(movingNpcImg, (x, y))


# NPC Enemy

playerImg1 = pygame.image.load('Enemy NPC.png')
playerNpcX = 465
playerNpcY = 25


def playerNpc():
    screen.blit(playerImg1, (playerNpcX, playerNpcY))


# playablePlayer

playerImg = pygame.image.load('Player 1 Character.png')
playerX = 465
playerY = 500
playerX_change = 0


def playablePlayer(x, y):
    screen.blit(playerImg, (x, y))

# Server
serverImg = pygame.image.load('server.png')
serverX = 900
serverY = 500

def Server(x,y):
    screen.blit(serverImg,(x,y))


# Lightning Bolt Attack

# Ready - You cant see the attack on the screen
# Fire - The lightning attack is in motion
lightningImg = pygame.image.load('light.png')
lightningX = 0
lightningY = 500
lightningX_change = 0
lightningY_change = 0.8
lightning_state = "ready"

lightnings = []  # array to store bullet position

# Scoring system

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

def score_display(x, y):
    score = font.render("Score  :" + str(score_value), True, (50, 100, 255))
    screen.blit(score, (x, y))

def fire_lightning(x, y):
    global lightning_state
    lightning_state = "fire"
    screen.blit(lightningImg, (x + 10 , y + 10))

    def inside():
        global var
        var = 'info'

    inside()

    # Lightning Movement


if lightning_state == "fire":
    fire_lightning(playerX, lightningY)
    lightningY -= lightningY_change

# 3 right of hacker
botNet6X = 885
botNet6Y = 25

# 2 right of hacker
botNet5X = 745
botNet5Y = 25

# 1 right of hacker
botNet4X = 605
botNet4Y = 25

# 3 left of hacker
botNet3X = 45
botNet3Y = 25

# 2 left of hacker
botNet2X = 185
botNet2Y = 25

# 1 Left of Hacker
botNetX = 325
botNetY = 25
botNetImg = pygame.image.load('evil.png')

# Document Attack botNet

# Ready - You cant see the attack on the screen

# Fire - The document attack is in motion
docImg = pygame.image.load('documents attack.png')
docX = 0
docY = 30
docX_change = 0
docY_change = 1.5
doc_state = "ready"


def fire_doc(x, y):
    global doc_state
    doc_state = "fire"
    screen.blit(docImg, (x, y))

    def inside():
        global var
        var = 'info'

    inside()

    # docAttack Movement
    if doc_state == "fire":
        fire_doc(botNetImg, docY)
        docY -= docY_change


class botNet:
    botNetImg = pygame.image.load('evil.png')


def botNet():
    screen.blit(botNetImg, (botNetX, botNetY))
    screen.blit(botNetImg, (botNet2X, botNet2Y))
    screen.blit(botNetImg, (botNet3X, botNet3Y))
    screen.blit(botNetImg, (botNet4X, botNet4Y))
    screen.blit(botNetImg, (botNet5X, botNet5Y))
    screen.blit(botNetImg, (botNet6X, botNet6Y))


# Projectile collision detection

def isCollision(movingNpcX,movingNpcY,lightningX,lightningY):
    distance = math.sqrt((math.pow(movingNpcX-lightningX,2))+ (math.pow(movingNpcY-lightningY,2)))
    if distance < 50:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Red, Green, Blue
    screen.fill((200, 200, 200))
    # background image
    screen.blit(background, (0, 0))

    # if keystroke pressed check whether it is left or it is right
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.8
            print("Left arrow is pressed dude")
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.8
            print("Right arrow is pressed dude")
        if event.key == pygame.K_UP:
            if lightning_state is "ready":
                lightningX = playerX
                print("UP is pressed dude")
                fire_lightning(lightningX, lightningY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    # Lightning motion/activity
    if lightningY <= 0:
        lightningY = 500
        lightning_state = "ready"

    if lightning_state is "fire":
        fire_lightning(lightningX, lightningY)
        lightningY -= lightningY_change

    # Collision/Moving NPC Hitbox

    collision = isCollision(movingNpcX,movingNpcY,lightningX,lightningY)
    if collision:
        lightningY = 500
        lightning_state = "ready"
        score_value += 1
        movingNpcX = random.randint(0, 1000)
        movingNpcY = random.randint(100,200)
    # Player and Moving NPC boundaries

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936

    movingNpcX += movingNpcX_change
    if movingNpcX <= 0:
        movingNpcX_change = 0.4
        movingNpcY += movingNpcY_change
    elif movingNpcX >= 900:
        movingNpcX = 900
        movingNpcX_change = -0.4
        movingNpcY += movingNpcY_change

        #End Game, You Lose!
        if movingNpcY > 425:
            for j in range(movingNpcX):
                movingNpcY[j] = 2000
            break


    playerNpc()
    botNet()
    playablePlayer(playerX, playerY)
    movingNpc(movingNpcX, movingNpcY)
    Server(serverX,serverY)
    score_display(textX, textY)

    pygame.display.update()
