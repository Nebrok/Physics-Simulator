import pygame
import math
import random
import Particle_class
import mapper
import Grav_Function
import Blackhole_class

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SPACE = (25,25,25)

size = (1000,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Physics Simulation")


done = False
clock = pygame.time.Clock()
screen.fill(BLACK)

p_list = []
b_list = []

gravity_pos = (size[0]/2,size[1]/2);

InitVel = 0

fr = 30

type_of_ob = "Particle"

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            p_list = []
        if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
            InitVel -= 1
            print(InitVel)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            InitVel += 1
            print(InitVel)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            type_of_ob = "Particle"
            print(type_of_ob)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            type_of_ob = "Blackhole"
            print(type_of_ob)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if type_of_ob == "Particle":
                new_p = Particle_class.Particle(screen,mousePos[0],mousePos[1],2,InitVel)
                p_list.append(new_p)
            elif type_of_ob == "Blackhole":
                b = Blackhole_class.Blackhole(screen,mousePos[0],mousePos[1],98)
                b_list.append(b)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            fr -= 1
            print(fr)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            fr += 1
            print(fr)

    screen.fill(SPACE)

    for i in range(len(b_list)):
        b_list[i].display()

    for i in range(len(p_list)):
        for k in range(len(p_list)):
            if i != k:
                p_list[i].update(Grav_Function.gravforce(p_list[k].posX, p_list[k].posY, p_list[i].posX, p_list[i].posY, p_list[k].mass))
        for j in range(len(b_list)):
            p_list[i].update(Grav_Function.gravforce(b_list[j].posX, b_list[j].posY, p_list[i].posX, p_list[i].posY, b_list[j].mass))

        p_list[i].display()

    #End of Loop
    pygame.display.flip()
    clock.tick(fr)

pygame.quit()

