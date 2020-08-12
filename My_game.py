import pygame
import random
import time

pygame.init()
#we loading music here
music = pygame.mixer.music.load('Rockville.mp3')
#we loop it so it can play forever
pygame.mixer.music.play(-1)
#these are the colour codes we are going to use
black = (0,0,0)
red = (255,0,0)
#we load the font we going to usre
font = pygame.font.Font('FreeSansBold.ttf', 50) 
#we assign the text You Lose with the colours
lose_txt = font.render('You Lose', True, black, red) 
#we assign the text You Win with the colours
win_txt = font.render('You Win', True, black, red)
#this is the center of the screen which is where we want to place the text
text_center = (1100 // 2, 650 // 2) 

#we set thte screen ratio
screen = pygame.display.set_mode((1280,650))

#we name the game here
pygame.display.set_caption("FIRST GAME")

#we load all the enemy immages 
enemy1 = pygame.image.load('L1E.png')
enemy2 = pygame.image.load('R2E.png')
enemy3 = pygame.image.load('L3E.png')
enemy4 = pygame.image.load('R4E.png')
enemy5 = pygame.image.load('L5E.png')
enemy6 = pygame.image.load('R6E.png')

#we get the width of the enemy here
enemy_width = enemy1.get_width()

#we load all the images for the player when walkingleft and walking right 
walkRight= [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

#we load the backround image 
bg = pygame.image.load('bg.png')

#we load the image of the player stand still 
#this will show when the player isnt moving 
char = pygame.image.load('standing.png')

#we assign clock to this
clock = pygame.time.Clock()

#we creat a method here called redrawGameWindow
def redrawGameWindow():
    global walkCount
    #the screen is set to the top left
    screen.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0
    #if left this is to change the pictures with the x and y 
    if left:
        screen.blit(walkLeft[walkCount//3], (PlayerXPosition,playerYPosition ))
        walkCount += 1
    #if right this is to change the pictures with the x and y 
    elif right:
        screen.blit(walkRight[walkCount//3], (PlayerXPosition,playerYPosition ))
        walkCount +=1
    #else we use the standing picture 
    else:
        screen.blit(char, (PlayerXPosition,playerYPosition ))

#The players X and Y posiiton
PlayerXPosition = 1000//2
playerYPosition = 650//2

#we declare the players width
width = 65
#we declare the players hight
height = 70
#the velocity of the players movement
vel = 10
#we assign left with false
left = False
#we assign right with false
right = False
#we assign up with false
up = False
#we assign down with false
down = False
#we assign run with true
run = True 
#we assign walkcount = 0
walkCount = 0
#we assign each enemy with a X-axis starting point
enemy1XPosition= 1280
enemy2XPosition= 0
enemy3XPosition= 1280
enemy4XPosition= 0
enemy5XPosition= 1280
enemy6XPosition= 0
#we assign each enemy witha random y-axis starting point
enemy1YPosition= random.randint(0,650 - 64)
enemy2YPosition= random.randint(0,650 - 64)
enemy3YPosition= random.randint(0,650 - 64)
enemy4YPosition= random.randint(0,650 - 64)
enemy5YPosition= random.randint(0,650 - 64)
enemy6YPosition= random.randint(0,650 - 64)

#main while loop
while run:
    clock.tick(27)
    #This draws the player image to the screen at the postion specfied.
    screen.blit(enemy1,(enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2,(enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3,(enemy3XPosition, enemy3YPosition))
    screen.blit(enemy4,(enemy4XPosition, enemy4YPosition))
    screen.blit(enemy5,(enemy5XPosition, enemy5YPosition))
    screen.blit(enemy6,(enemy6XPosition, enemy6YPosition))

#we update the screen

    pygame.display.update()

# Bounding box for the player:    

    playerBoxR1 = pygame.Rect(walkLeft[0].get_rect())
    playerBoxR2 = pygame.Rect(walkLeft[1].get_rect())
    playerBoxR3 = pygame.Rect(walkLeft[2].get_rect())
    playerBoxR4 = pygame.Rect(walkLeft[3].get_rect())
    playerBoxR5 = pygame.Rect(walkLeft[4].get_rect())
    playerBoxR6 = pygame.Rect(walkLeft[5].get_rect())
    playerBoxR7 = pygame.Rect(walkLeft[6].get_rect())
    playerBoxR8 = pygame.Rect(walkLeft[7].get_rect())
    playerBoxR9 = pygame.Rect(walkLeft[8].get_rect())

# Bounding box for the player:    

    playerBoxL1 = pygame.Rect(walkRight[0].get_rect())
    playerBoxL2 = pygame.Rect(walkRight[1].get_rect())
    playerBoxL3 = pygame.Rect(walkRight[2].get_rect())
    playerBoxL4 = pygame.Rect(walkRight[3].get_rect())
    playerBoxL5 = pygame.Rect(walkRight[4].get_rect())
    playerBoxL6 = pygame.Rect(walkRight[5].get_rect())
    playerBoxL7 = pygame.Rect(walkRight[6].get_rect())
    playerBoxL8 = pygame.Rect(walkRight[7].get_rect())
    playerBoxL9 = pygame.Rect(walkRight[8].get_rect())

#we make a list of all the players boxs 
#for the right and left

    playerBoxsR = [playerBoxR1,playerBoxR2,playerBoxR3,playerBoxR4,playerBoxR5,playerBoxR6,playerBoxR7,playerBoxR8,playerBoxR9]
    playerBoxsL = [playerBoxL1,playerBoxL2,playerBoxL3,playerBoxL4,playerBoxL5,playerBoxL6,playerBoxL7,playerBoxL8,playerBoxL9]

#we applying the rectangle around the players right Right images

    playerBoxR1.top = playerYPosition
    playerBoxR1.left = PlayerXPosition
    playerBoxR2.top = playerYPosition
    playerBoxR2.left = PlayerXPosition
    playerBoxR3.top = playerYPosition
    playerBoxR3.left = PlayerXPosition
    playerBoxR4.top = playerYPosition
    playerBoxR4.left = PlayerXPosition
    playerBoxR5.top = playerYPosition
    playerBoxR5.left = PlayerXPosition
    playerBoxR6.top = playerYPosition
    playerBoxR6.left = PlayerXPosition
    playerBoxR7.top = playerYPosition
    playerBoxR7.left = PlayerXPosition
    playerBoxR8.top = playerYPosition
    playerBoxR8.left = PlayerXPosition
    playerBoxR9.top = playerYPosition
    playerBoxR9.left = PlayerXPosition

# we applying the rectangle around the players right left images
 
    playerBoxL1.top = playerYPosition
    playerBoxL1.left = PlayerXPosition
    playerBoxL2.top = playerYPosition
    playerBoxL2.left = PlayerXPosition
    playerBoxL3.top = playerYPosition
    playerBoxL3.left = PlayerXPosition
    playerBoxL4.top = playerYPosition
    playerBoxL4.left = PlayerXPosition
    playerBoxL5.top = playerYPosition
    playerBoxL5.left = PlayerXPosition
    playerBoxL6.top = playerYPosition
    playerBoxL6.left = PlayerXPosition
    playerBoxL7.top = playerYPosition
    playerBoxL7.left = PlayerXPosition
    playerBoxL8.top = playerYPosition
    playerBoxL8.left = PlayerXPosition
    playerBoxL9.top = playerYPosition
    playerBoxL9.left = PlayerXPosition

# Bounding box for the player:    

    enemyBox1 =pygame.Rect(enemy1.get_rect())
    enemyBox2 =pygame.Rect(enemy2.get_rect())
    enemyBox3 =pygame.Rect(enemy3.get_rect())
    enemyBox4 =pygame.Rect(enemy4.get_rect())
    enemyBox5 =pygame.Rect(enemy5.get_rect())
    enemyBox6 =pygame.Rect(enemy6.get_rect())
    
# we applying the rectangle around the enemys

    enemyBox1.top = enemy1YPosition
    enemyBox1.left = enemy1XPosition
    enemyBox2.top = enemy2YPosition
    enemyBox2.left = enemy2XPosition
    enemyBox3.top = enemy3YPosition
    enemyBox3.left = enemy3XPosition
    enemyBox4.top = enemy4YPosition
    enemyBox4.left = enemy4XPosition
    enemyBox5.top = enemy5YPosition
    enemyBox5.left = enemy5XPosition
    enemyBox6.top = enemy6YPosition
    enemyBox6.left = enemy6XPosition

    #if enemy box 1 collides with any of the images in list playerboxL and right than
    #update the screen pause the screen for 5 seconds we display you lose in the center 
    #then we quit the game
    if not enemyBox1.collidelist(playerBoxsL) and not enemyBox1.collidelist(playerBoxsR):
        screen.blit(lose_txt, text_center)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        exit(0)

    #if enemy box 2 collides with any of the images in list playerboxL and right than
    #update the screen pause the screen for 5 seconds we display you lose in the center 
    #then we quit the game    

    elif not enemyBox2.collidelist(playerBoxsL) and not enemyBox2.collidelist(playerBoxsR):
        screen.blit(lose_txt, text_center)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        exit(0)

    #if enemy box 3 collides with any of the images in list playerboxL and right than
    #update the screen pause the screen for 5 seconds we display you lose in the center 
    #then we quit the game
    elif not enemyBox3.collidelist(playerBoxsL) and not enemyBox3.collidelist(playerBoxsR):
        screen.blit(lose_txt, text_center)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        exit(0)
    #if enemy box 4 collides with any of the images in list playerboxL and right than
    #update the screen pause the screen for 5 seconds we display you lose in the center 
    #then we quit the game
    elif not enemyBox4.collidelist(playerBoxsL) and enemyBox4.collidelist(playerBoxsR):
        screen.blit(lose_txt, text_center)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        exit(0)
    #if enemy box 5 collides with any of the images in list playerboxL and right than
    #update the screen pause the screen for 5 seconds we display you lose in the center 
    #then we quit the game
    elif not enemyBox5.collidelist(playerBoxsL) and not enemyBox5.collidelist(playerBoxsR):
        screen.blit(lose_txt, text_center)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        exit(0)
    #if enemy box 6 collides with any of the images in list playerboxL and right than
    #update the screen pause the screen for 5 seconds we display you lose in the center 
    #then we quit the game
    elif not enemyBox6.collidelist(playerBoxsL) and not enemyBox6.collidelist(playerBoxsR):
        screen.blit(lose_txt, text_center)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        exit(0)      

    if enemy1XPosition < 0 - enemy_width:
        screen.blit(win_txt, text_center)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        exit(0)

    #if the user quits the game the run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #we assign keys to method get pressed 
    keys = pygame.key.get_pressed()

    #if the left key gets pressed the left = True and right = False
    #and moves with the assigned velocity
    if keys[pygame.K_LEFT] and PlayerXPosition > vel:
        PlayerXPosition -= vel
        left = True
        right = False

    #if the right key gets pressed the right = True and left = False
    #and moves with the assigned velocity
    elif keys[pygame.K_RIGHT] and PlayerXPosition < 1280 - width - vel:
        PlayerXPosition += vel
        right = True
        left = False

    #else right = false and left = false and the walkcount is = 0
    else:
        right = False
        left = False
        walkCount = 0
    #if the up key is presed up = true and down = false 
    #and moves with the assigned velocity
    if keys [pygame.K_UP] and playerYPosition > vel:
        playerYPosition -= vel
        up = True
        down = False
    #if the down key is presed down = true and up = false 
    #and moves with the assigned velocity
    elif keys [pygame.K_DOWN] and playerYPosition < 600 - height - vel:
        playerYPosition += vel
        down = True
        up = False
    else:
        up = False
        down = False
        walkCount = 0

    #if enemy1XPosition < 1280 + enemy_width:
    enemy1XPosition -= 5
    enemy2XPosition += 5
    enemy3XPosition -= 5
    enemy4XPosition += 5
    enemy5XPosition -= 5
    enemy6XPosition += 5

    pygame.display.update()
    #we activate the redrawgamewindow function
    redrawGameWindow()

pygame.quit()