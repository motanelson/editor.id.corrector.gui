from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glEnable(GL_DEPTH_TEST)  # Enable depth testing
    glEnable(GL_LIGHTING)    # Enable lighting
    glEnable(GL_LIGHT0)      # Enable light source 0

    # Define light properties
    light_position = [1.0, 1.0, 1.0, 0.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Define material properties
    material_ambient = [0.2, 0.2, 0.2, 1.0]
    material_diffuse = [1.0, 1.0, 1.0, 1.0]  
    material_specular = [1.0, 1.0, 1.0, 1.0]
    material_shininess = [50.0]

    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutSolidTeapot(0.5)  # Render a teapot
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"OpenGL Material Example")
    # Fundo amarelo
    glClearColor(1.0, 1.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
