import time
import math
import board
import busio
import adafruit_bno08x
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from adafruit_bno08x.i2c import BNO08X_I2C

# i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
i2c = busio.I2C(board.SCL, board.SDA)
bno = BNO08X_I2C(i2c)

bno.enable_feature(adafruit_bno08x.BNO_REPORT_ROTATION_VECTOR)

# ### Print yaw, pitc, and roll angles.
# print("Rotation Vector Euler:")
# while True:
#     quat_i, quat_j, quat_k, quat_real = bno.quaternion
#     # print(
#     # "I: %0.6f J: %0.6f K: %0.6f Real: %0.6f" % (quat_i, quat_j, quat_k, quat_real)
#     # )

#     # Convert quaternions to yaw, pitch, and roll
#     yaw = math.atan2(2 * (quat_i * quat_j + quat_real * quat_k), 1 - 2 * (quat_j**2 + quat_k**2))
#     pitch = math.asin(2 * (quat_i * quat_k - quat_real * quat_j))
#     roll = math.atan2(2 * (quat_j * quat_k + quat_real * quat_i), 1 - 2 * (quat_i**2 + quat_j**2))

#     # Convert radians to degrees if needed
#     yaw_degrees = math.degrees(yaw)
#     pitch_degrees = math.degrees(pitch)
#     roll_degrees = math.degrees(roll)

#     # Print the results
#     print("Yaw: %0.2f, Pitch: %0.2f, Roll: %0.2f" % (yaw_degrees, pitch_degrees, roll_degrees))

#     # # Add a delay to avoid excessive printing
#     time.sleep(0.5)

### Cube rotation based on the IMU quaternion values.
# # Initialize Pygame
# pygame.init()

# # Set the window size and display mode
# display = (800, 600)
# pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
# pygame.display.set_caption("Cube Orientation Based on Quaternion")

# # Set up the perspective
# gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
# glTranslatef(0.0, 0.0, -5)

# # Function to draw the cube
# def draw_cube():
#     glBegin(GL_QUADS)
#     # Front face
#     glVertex3f(-0.5, -0.5, 0.5)
#     glVertex3f(0.5, -0.5, 0.5)
#     glVertex3f(0.5, 0.5, 0.5)
#     glVertex3f(-0.5, 0.5, 0.5)
#     # Back face
#     glVertex3f(-0.5, -0.5, -0.5)
#     glVertex3f(0.5, -0.5, -0.5)
#     glVertex3f(0.5, 0.5, -0.5)
#     glVertex3f(-0.5, 0.5, -0.5)
#     # Left face
#     glVertex3f(-0.5, -0.5, -0.5)
#     glVertex3f(-0.5, -0.5, 0.5)
#     glVertex3f(-0.5, 0.5, 0.5)
#     glVertex3f(-0.5, 0.5, -0.5)
#     # Right face
#     glVertex3f(0.5, -0.5, -0.5)
#     glVertex3f(0.5, -0.5, 0.5)
#     glVertex3f(0.5, 0.5, 0.5)
#     glVertex3f(0.5, 0.5, -0.5)
#     # Top face
#     glVertex3f(-0.5, 0.5, -0.5)
#     glVertex3f(0.5, 0.5, -0.5)
#     glVertex3f(0.5, 0.5, 0.5)
#     glVertex3f(-0.5, 0.5, 0.5)
#     # Bottom face
#     glVertex3f(-0.5, -0.5, -0.5)
#     glVertex3f(0.5, -0.5, -0.5)
#     glVertex3f(0.5, -0.5, 0.5)
#     glVertex3f(-0.5, -0.5, 0.5)
#     glEnd()

# # Function to handle IMU data and update the cube orientation
# def update_cube_orientation(quaternion_data):
#     glLoadIdentity()
#     quat_i, quat_j, quat_k, quat_real = quaternion_data
#     glMultMatrixf([1 - 2*(quat_j**2 + quat_k**2), 2*(quat_i*quat_j - quat_real*quat_k), 2*(quat_i*quat_k + quat_real*quat_j), 0,
#                    2*(quat_i*quat_j + quat_real*quat_k), 1 - 2*(quat_i**2 + quat_k**2), 2*(quat_j*quat_k - quat_real*quat_i), 0,
#                    2*(quat_i*quat_k - quat_real*quat_j), 2*(quat_j*quat_k + quat_real*quat_i), 1 - 2*(quat_i**2 + quat_j**2), 0,
#                    0, 0, 0, 1])

# # Main loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     # Get IMU quaternion data (replace this with your actual data)
#     quat_i, quat_j, quat_k, quat_real = bno.quaternion

#     # Clear the screen
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

#     # Update and draw the cube based on quaternion orientation
#     update_cube_orientation((quat_i, quat_j, quat_k, quat_real))
#     draw_cube()

#     pygame.display.flip()
#     pygame.time.wait(10)


# ### Cube with axes.
# # Initialize Pygame
# pygame.init()

# # Set the window size and display mode
# display = (800, 600)
# pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
# pygame.display.set_caption("Cube with Axes Based on Quaternion")

# # Set up the perspective
# gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
# glTranslatef(0.0, 0.0, -5)

# # Function to draw the cube
# def draw_cube():
#     glBegin(GL_QUADS)
#     # Front face
#     glVertex3f(-0.5, -0.5, 0.5)
#     glVertex3f(0.5, -0.5, 0.5)
#     glVertex3f(0.5, 0.5, 0.5)
#     glVertex3f(-0.5, 0.5, 0.5)
#     # Back face
#     glVertex3f(-0.5, -0.5, -0.5)
#     glVertex3f(0.5, -0.5, -0.5)
#     glVertex3f(0.5, 0.5, -0.5)
#     glVertex3f(-0.5, 0.5, -0.5)
#     # Left face
#     glVertex3f(-0.5, -0.5, -0.5)
#     glVertex3f(-0.5, -0.5, 0.5)
#     glVertex3f(-0.5, 0.5, 0.5)
#     glVertex3f(-0.5, 0.5, -0.5)
#     # Right face
#     glVertex3f(0.5, -0.5, -0.5)
#     glVertex3f(0.5, -0.5, 0.5)
#     glVertex3f(0.5, 0.5, 0.5)
#     glVertex3f(0.5, 0.5, -0.5)
#     # Top face
#     glVertex3f(0.5, -0.5, -0.5)
#     glVertex3f(0.5, -0.5, 0.5)
#     glVertex3f(0.5, 0.5, 0.5)
#     glVertex3f(0.5, 0.5, -0.5)
#     # Bottom face
#     glVertex3f(-0.5, -0.5, -0.5)
#     glVertex3f(-0.5, -0.5, 0.5)
#     glVertex3f(-0.5, 0.5, 0.5)
#     glVertex3f(-0.5, 0.5, -0.5)
#     glEnd()

# # Function to draw axes at the center of the cube
# def draw_axes():
#     glBegin(GL_LINES)
#     # X-axis (roll axis)
#     glColor3f(1, 0, 0)
#     glVertex3f(0, 0, 0)
#     glVertex3f(1, 0, 0)
#     # Y-axis (pitch axis)
#     glColor3f(0, 1, 0)
#     glVertex3f(0, 0, 0)
#     glVertex3f(0, 1, 0)
#     # Z-axis (yaw axis)
#     glColor3f(0, 0, 1)
#     glVertex3f(0, 0, 0)
#     glVertex3f(0, 0, 1)
#     glEnd()

# # Function to handle IMU data and update the cube orientation
# def update_cube_orientation(quaternion_data):
#     glLoadIdentity()
#     quat_i, quat_j, quat_k, quat_real = quaternion_data
#     glMultMatrixf([1 - 2*(quat_j**2 + quat_k**2), 2*(quat_i*quat_j - quat_real*quat_k), 2*(quat_i*quat_k + quat_real*quat_j), 0,
#                    2*(quat_i*quat_j + quat_real*quat_k), 1 - 2*(quat_i**2 + quat_k**2), 2*(quat_j*quat_k - quat_real*quat_i), 0,
#                    2*(quat_i*quat_k - quat_real*quat_j), 2*(quat_j*quat_k + quat_real*quat_i), 1 - 2*(quat_i**2 + quat_j**2), 0,
#                    0, 0, 0, 1])

# # Main loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     # Get IMU quaternion data (replace this with your actual data)
#     quat_i, quat_j, quat_k, quat_real = bno.quaternion

#     # Clear the screen
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

#     # Update and draw the cube based on quaternion orientation
#     update_cube_orientation((quat_i, quat_j, quat_k, quat_real))
#     draw_cube()

#     # Draw axes at the center of the cube
#     draw_axes()

#     pygame.display.flip()

### Axes and a rectangle.
# Initialize Pygame
pygame.init()

# Set the window size and display mode
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Inverted Z-Axis Rectangle at Origin")

# Set up the perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Function to draw a colored and transparent rectangle centered at the origin
def draw_rectangle(width, height, color, alpha):
    half_width = width / 2
    half_height = height / 2
    glColor4f(color[0], color[1], color[2], alpha)
    glBegin(GL_QUADS)
    glVertex3f(-half_width, -half_height, 0)
    glVertex3f(half_width, -half_height, 0)
    glVertex3f(half_width, half_height, 0)
    glVertex3f(-half_width, half_height, 0)
    glEnd()

# Function to draw axes at the center
def draw_axes():
    glBegin(GL_LINES)
    # X-axis (roll axis)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    # Y-axis (pitch axis)
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, -1, 0)
    # Z-axis (yaw axis)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, -1)  # Invert the direction by changing the sign
    glEnd()

# Function to handle IMU data and update the view
def update_view(quaternion_data):
    glLoadIdentity()
    quat_i, quat_j, quat_k, quat_real = quaternion_data
    glMultMatrixf([1 - 2*(quat_j**2 + quat_k**2), 2*(quat_i*quat_j - quat_real*quat_k), 2*(quat_i*quat_k + quat_real*quat_j), 0,
                   2*(quat_i*quat_j + quat_real*quat_k), 1 - 2*(quat_i**2 + quat_k**2), 2*(quat_j*quat_k - quat_real*quat_i), 0,
                   2*(quat_i*quat_k - quat_real*quat_j), 2*(quat_j*quat_k + quat_real*quat_i), 1 - 2*(quat_i**2 + quat_j**2), 0,
                   0, 0, 0, 1])

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get IMU quaternion data (replace this with your actual data)
    quat_i, quat_j, quat_k, quat_real = bno.quaternion

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Update and draw the axes based on quaternion orientation
    update_view((quat_i, quat_j, quat_k, quat_real))
    draw_axes()

    # Draw a colored and transparent rectangle centered at the origin
    draw_rectangle(1, 0.5, (0.5, 0.5, 1), 0.7)  # (R: 0.5, G: 0.5, B: 1), Alpha: 0.7

    pygame.display.flip()
    pygame.time.wait(10)