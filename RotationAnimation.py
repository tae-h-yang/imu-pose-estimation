import time
import math
import board
import busio
import adafruit_bno08x
import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from adafruit_bno08x.i2c import BNO08X_I2C

i2c = busio.I2C(board.SCL, board.SDA)
bno = BNO08X_I2C(i2c)

bno.enable_feature(adafruit_bno08x.BNO_REPORT_ROTATION_VECTOR)
# bno.enable_feature(adafruit_bno08x.BNO_REPORT_MAGNETOMETER)

# # Initialize Pygame
# pygame.init()

# # Set the window size and display mode
# display = (800, 600)
# pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
# pygame.display.set_caption("IMU 3D Rotation")

# # Set up the perspective
# gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
# glTranslatef(0.0, 0.0, -5)

# # Function to draw a colored and transparent rectangle centered at the origin
# def draw_rectangle(width, height, color, alpha):
#     half_width = width / 2
#     half_height = height / 2
#     glColor4f(color[0], color[1], color[2], alpha)
#     glBegin(GL_QUADS)
#     glVertex3f(-half_width, -half_height, 0)
#     glVertex3f(half_width, -half_height, 0)
#     glVertex3f(half_width, half_height, 0)
#     glVertex3f(-half_width, half_height, 0)
#     glEnd()

# # Function to draw axes at the center
# def draw_axes():
#     glBegin(GL_LINES)
#     # X-axis (roll axis)
#     glColor3f(1, 0, 0)
#     glVertex3f(0, 0, 0)
#     glVertex3f(1, 0, 0)
#     # Y-axis (pitch axis)
#     glColor3f(0, 1, 0)
#     glVertex3f(0, 0, 0)
#     glVertex3f(0, -1, 0)
#     # Z-axis (yaw axis)
#     glColor3f(0, 0, 1)
#     glVertex3f(0, 0, 0)
#     glVertex3f(0, 0, -1)  # Invert the direction by changing the sign
#     glEnd()

# # Function to handle IMU data and update the view
# def update_view(quaternion_data):
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

#     # Update and draw the axes based on quaternion orientation
#     update_view((quat_i, quat_j, quat_k, quat_real))
#     draw_axes()

#     # Convert quaternions to yaw, pitch, and roll
#     # Roll (X-axis rotation)
#     roll = math.atan2(2 * (quat_real * quat_i + quat_j * quat_k), 1 - 2 * (quat_i**2 + quat_j**2))

#     # Pitch (Y-axis rotation)
#     pitch = math.asin(2 * (quat_real * quat_j - quat_k * quat_i))

#     # Yaw (Z-axis rotation)
#     yaw = math.atan2(2 * (quat_real * quat_k + quat_i * quat_j), 1 - 2 * (quat_j**2 + quat_k**2))

#     # Convert radians to degrees if needed
#     yaw_degrees = math.degrees(yaw)
#     pitch_degrees = math.degrees(pitch)
#     roll_degrees = math.degrees(roll)

#     # Print the results
#     print("Yaw: %0.2f, Pitch: %0.2f, Roll: %0.2f" % (yaw_degrees, pitch_degrees, roll_degrees))

#     # print(
#     # "I: %0.6f J: %0.6f K: %0.6f Real: %0.6f" % (quat_i, quat_j, quat_k, quat_real)
#     # )
    
#     # x, y, z = bno.magnetic
#     # print("x: %0.2f, y: %0.2f, z: %0.2f"% (x, y, z))

#     # Draw a colored and transparent rectangle centered at the origin
#     draw_rectangle(1, 0.5, (0.5, 0.5, 1), 0.7)  # (R: 0.5, G: 0.5, B: 1), Alpha: 0.7

#     pygame.display.flip()
#     pygame.time.wait(10)


# Initialize Pygame
pygame.init()

# Set the window size and display mode
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("IMU 3D Rotation")

# Set up the perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

# Set the camera position
gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
# gluLookAt(5, 0, 0, 0, 0, 0, 0, 1, 0)


# Function to draw a 3D rectangle centered at the origin
def draw_3d_rectangle(length, width, height, alpha):
    half_length = length / 2
    half_width = width / 2
    half_height = height / 2
    glColor4f(0.5, 0.5, 1, alpha)  # (R: 0.5, G: 0.5, B: 1), Alpha: specified value
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glBegin(GL_QUADS)
    # Top face
    glVertex3f(-half_length, half_width, half_height)
    glVertex3f(half_length, half_width, half_height)
    glVertex3f(half_length, -half_width, half_height)
    glVertex3f(-half_length, -half_width, half_height)
    # Bottom face
    glVertex3f(-half_length, half_width, -half_height)
    glVertex3f(half_length, half_width, -half_height)
    glVertex3f(half_length, -half_width, -half_height)
    glVertex3f(-half_length, -half_width, -half_height)
    # Front face
    glVertex3f(-half_length, half_width, half_height)
    glVertex3f(half_length, half_width, half_height)
    glVertex3f(half_length, half_width, -half_height)
    glVertex3f(-half_length, half_width, -half_height)
    # Back face
    glVertex3f(-half_length, -half_width, half_height)
    glVertex3f(half_length, -half_width, half_height)
    glVertex3f(half_length, -half_width, -half_height)
    glVertex3f(-half_length, -half_width, -half_height)
    # Left face
    glVertex3f(-half_length, half_width, half_height)
    glVertex3f(-half_length, -half_width, half_height)
    glVertex3f(-half_length, -half_width, -half_height)
    glVertex3f(-half_length, half_width, -half_height)
    # Right face
    glVertex3f(half_length, half_width, half_height)
    glVertex3f(half_length, -half_width, half_height)
    glVertex3f(half_length, -half_width, -half_height)
    glVertex3f(half_length, half_width, -half_height)
    glEnd()

# Function to handle IMU data and update the view
def update_view(quaternion_data):
    glLoadIdentity()
    quat_i, quat_j, quat_k, quat_real = quaternion_data
    glMultMatrixf([1 - 2 * (quat_j**2 + quat_k**2), 2 * (quat_i * quat_j + quat_real * quat_k),
                   2 * (quat_i * quat_k - quat_real * quat_j), 0, 2 * (quat_i * quat_j - quat_real * quat_k),
                   1 - 2 * (quat_i**2 + quat_k**2), 2 * (quat_j * quat_k + quat_real * quat_i), 0,
                   2 * (quat_i * quat_k + quat_real * quat_j), 2 * (quat_j * quat_k - quat_real * quat_i),
                   1 - 2 * (quat_i**2 + quat_j**2), 0, 0, 0, 0, 1])

# Function to draw distinctive axes with labels
def draw_axes():
    # Adjusted length of axes
    axis_length = 0.8

    # X-axis
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(axis_length, 0, 0)
    glEnd()
    draw_text((axis_length, 0, 0), "X")

    # Y-axis
    glColor3f(0, 1, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, axis_length, 0)
    glEnd()
    draw_text((0, axis_length, 0), "Y")

    # Z-axis
    glColor3f(0, 0, 1)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, axis_length)
    glEnd()
    draw_text((0, 0, axis_length), "Z")

def draw_text(position, text):
    font_size = 20
    font = pygame.font.SysFont(None, int(font_size))
    text_surface = font.render(text, True, (255, 255, 255), (0, 0, 0))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos3d(*position)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

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

    # Draw a more transparent and smaller 3D rectangle centered at the origin
    draw_3d_rectangle(0.6, 0.25, 0.1, 0.5)  # Adjusted size and alpha value

    # Update and draw the axes based on quaternion orientation
    update_view((quat_i, quat_j, quat_k, quat_real))
    draw_axes()

    pygame.display.flip()
    pygame.time.wait(10)