import pygame

class Particle():
    def __init__(self, screen, x, y, L, InitVel):
        self.posX = x
        self.posY = y
        self.x_speed = 0
        self.y_speed = 0
        self.x_vel = InitVel
        self.y_vel = 0
        self.L = L
        self.mass = 30

        
        self.screen = screen
        
    
    def display(self):
        #Taking the length of the object away from the position centers
        #the coordinates on the middle of the rectangle.
        pygame.draw.rect(self.screen, [255,255,0], (self.posX-self.L, self.posY-self.L, self.L, self.L))

    def update(self, speeds):
        self.x_speed = speeds[0]
        self.y_speed = speeds[1]
        
        self.x_vel += self.x_speed
        self.y_vel += self.y_speed

        self.posX += self.x_vel/self.mass
        self.posY += self.y_vel/self.mass

    def area(self):
        area_list = []
        for i in range(self.L):
            for j in range(self.L):
                area_list.append([self.posX+i,self.posY+j])
        return area_list

    def returnpos(self):
        return [self.posX, self.posY]
