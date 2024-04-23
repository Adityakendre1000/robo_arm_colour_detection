import numpy as np
import math

# Fixed point coordinates
fixed_x = 60
fixed_y = 240

# Frame dimensions in cm
frame_width_cm = 83.79
frame_height_cm = 62.842

# Frame dimensions in pixels
frame_width_px = 640
frame_height_px = 480

# Pixel-to-cm ratios
px_to_cm_ratio_x = frame_width_cm / frame_width_px
px_to_cm_ratio_y = frame_height_cm / frame_height_px

def calculate_distance(x, y):
    # Convert pixel distances to cm
    dx_cm = (x - fixed_x)
    dy_cm = (y - fixed_y)

    # Calculate the distance between the two points in cm
    distance_pix = np.sqrt(dx_cm ** 2 + dy_cm ** 2)
    distance = distance_pix * px_to_cm_ratio_x
    return distance

import math

def calculate_angle(x2, y2):
    # Calculate the differences in coordinates
    dx = x2 - fixed_x
    dy = y2 - fixed_y
    
    # Calculate the angle in radians using arctangent
    angle_radians = math.atan2(dy, dx)
    
    # Convert the angle to degrees
    angle_degrees = math.degrees(angle_radians)
    
    # Ensure the angle is between -180 and 180 degrees
    angle_degrees = ((angle_degrees + 180) % 360) - 180
    
    return angle_degrees

# while True:
#     a=int(input("x:"))
#     b=int(input("y:"))
#     print(calculate_distance(a,b))

# import redcen
# print(calculate_distance(redcen.center_x,redcen.center_y))