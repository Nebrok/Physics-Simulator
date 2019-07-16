import math
import pygame
import Particle_class
import mapper
import Grav_Function

class Blackhole():
    def __init__(self, screen, x, y, mass):
        self.posX = x
        self.posY = y
        self.mass = mass
        self.L = 5

        self.x_speed = 0
        self.y_speed = 0
        self.x_vel = 0
        self.y_vel = 0

        self.screen = screen
        
    def display(self):
        pygame.draw.rect(self.screen, [0,0,0], (self.posX-self.L, self.posY-self.L, self.L, self.L))

    def update(self, speeds):
        self.x_speed = speeds[0]
        self.y_speed = speeds[1]
        
        self.x_vel += self.x_speed
        self.y_vel += self.y_speed

        self.posX += self.x_vel
        self.posY += self.y_vel
        
    def returnpos(self):
        return [self.posX, self.posY]

    def area(self):
        #returns a list of the coordinate points which the object occupys
        area_list = []
        for i in range(self.L):
            for j in range(self.L):
                area_list.append([self.posX+i,self.posY+j])
        return area_list

    def touching(self, particle):
        if particle.posX-(particle.L/2) < self.posX+(self.L/2) and particle.posY-(particle.L/2) < self.posY+(self.L/2):
            return True

        #if particle.posX+(particle.L/2) > self.posX-(self.L/2) and particle.posY+(particle.L/2) > self.posY-(self.L/2):
        #    return True


        
        touching = False
        for i in range(len(self.area())):
            for j in range(len(particle.area())):
                if self.area()[i] == particle.area()[j]:
                    touching = True
        return touching
