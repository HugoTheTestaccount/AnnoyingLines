import winsound
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo

import random
import pygame
from pygame.locals import *
pygame.init()
display = (500, 400)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
class cube():
    vertices = (
        (1,-1,-1),
        (1,1,-1),
        (-1,1,-1),
        (-1,-1,-1),
        (1,-1,1),
        (1,1,1),    
        (-1,-1,1),
        (-1,1,1)
    )
    edges=(
        (0,1), 
        (0,3), 
        (0,4),
        (2,1), 
        (2,3), 
        (2,7), 
        (6,3), 
        (6,4), 
        (6,7), 
        (5,1), 
        (5,4), 
        (5,7) 
    )
    surfaces = (
        (0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6),
    )
    def lineCube(self,x,y,z):
        glPushMatrix()
        glBegin(GL_LINES)
        for edge in cube.edges:
            for vertex in edge:
                glVertex3fv((random.randint(-1,1),random.randint(-1,1),random.randint(-1,1)))
        glEnd()
        glPopMatrix()
cub = cube
while True:
    cub.lineCube(0,0,0,0)
    glRotatef(random.randint(1,350),1,0,0)
    pygame.display.flip()
    winsound.Beep(random.randint(2000,4000),random.randint(40,100))
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #glClearColor(135.0/255.0, 206.0/255.0, 235.0/255.0, 0.0)
