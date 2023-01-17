# this file is for the basic implementations of the feature of the switching controls

import pygame
import random

from player import player
from obstacles import obstacle

pygame.init()

width = 500
height = 500

font = pygame.font.Font('freesansbold.ttf', 20)

screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)

player = player(100, 100, (0, 255, 0))
run = True
clock = pygame.time.Clock()

waitToResetObstacles = 0
obstacles = []


def addObstacles():
    obstacles.clear()
    randomNum = random.randint(0,2)
    print(randomNum)
    if randomNum == 0 :
        obstacles.append(
            obstacle((0, 0, 1), random.randint(0, screen.get_width()), random.randint(0, screen.get_height()), 45) )
        obstacles.append(
            obstacle((0,0,1), random.randint(0,screen.get_width()), random.randint(0, screen.get_height()), -45))
    if randomNum == 1:
        obstacles.append(obstacle((0,0,1), 0, random.randint(0, screen.get_height()), 0))
        obstacles.append(obstacle((0,0,1), random.randint(0, screen.get_width()), 0, 90))
    else:
        obstacles.append(obstacle((0,0,1), 0,0,45))
        obstacles.append(obstacle((0,0,1), 0, random.randint(0,int(screen.get_height()/2)), 0))
        obstacles.append(obstacle((0,0,1), random.randint(int(screen.get_width()/2), screen.get_width()), 0,90))


def updateScreen(screen, player, thick):
    screen.fill(white)
    player.move(screen)
    player.update()
    player.draw(screen)

    # just displays the regular controls or what the controls below actually do
    text = "For the controls: Left, right, up, down"
    label = font.render(text, 1, (0, 0, 0))
    screen.blit(label, (0, 0))
    text = "Controls are " + str(player.get_controls())
    label = font.render(text, 1, (0, 0, 0))
    screen.blit(label, (0, 40))
    text = str(player.health)
    label = font.render(text, 1, (0,0,0))
    screen.blit(label,(200,80))
    for obs in obstacles:
        obs.draw(screen,thick)
        obs.checkForCollision(screen, player)

    pygame.display.update()


pygame.time.set_timer(pygame.USEREVENT, 5000)


displayObstacles = False
thick =0

while player.health > 0:
    # determines if the controls switch
    randomNum = random.randint(0, 1000)
    if randomNum == 1:
        random.shuffle(player.controls)

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.USEREVENT:
            if displayObstacles:
                pygame.time.set_timer(pygame.USEREVENT+1,1000)
                addObstacles()
                displayObstacles = False
                print("thin")
                thick = 1
                print("add obstacles")
                player.immune = True

            else:
                obstacles.clear()
                displayObstacles = True
                print("clear obstacles")
        elif event.type == pygame.USEREVENT+1:
            addObstacles()
            displayObstacles = False
            print("fill")
            thick = 0
            pygame.time.set_timer(pygame.USEREVENT+1, 0)
            player.immune = False

    updateScreen(screen, player,thick)

pygame.quit()


# TODO create better amount of obstacles and more variety, put in the collision stuff and display health