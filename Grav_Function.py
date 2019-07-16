import math

def gravforce(gravobx, gravoby, objectx, objecty, gravobmass):
    x_diff = gravobx - objectx
    y_diff = gravoby - objecty

    mag = math.sqrt(x_diff**2 + y_diff**2)

    x_force = x_diff/mag * (gravobmass/1000)
    y_force = y_diff/mag * (gravobmass/1000)
    
    if objectx < gravobx:
        dx = 1
    elif objectx == gravobx:
        x_force = 0
        dx = 1
    else:
        dx = -1
    if objecty < gravoby:
        dy = 1
    elif objecty == gravoby:
        y_force = 0
        dy = 1
    else:
        dy = -1

    return [x_force, y_force]


#Unused function from Main file, dumped here to clean main file
"""
def returnxandyfromgravity(angle, mag):
    x = math.cos(math.radians(angle-angle_adjust)) * mag
    y = math.sin(math.radians(angle-angle_adjust)) * mag

    return [x + gravity_pos[0],y + gravity_pos[1]]
"""
