import cv2
import numpy as np

# Start the webcam
cap = cv2.VideoCapture(0)

# Define new origin
origin_x = 0
origin_y = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # Bottom of the frame

# Capture frame-by-frame
ret, frame = cap.read()

# Convert the frame from BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Define range for green color in HSV
lower_green = np.array([60, 50, 50])
upper_green = np.array([100, 255, 255])

# Threshold the HSV image to get only green colors
mask = cv2.inRange(hsv, lower_green, upper_green)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the biggest contour (if any)
if contours:
    biggest_contour = max(contours, key=cv2.contourArea)

    # Calculate the center of the biggest contour
    moments = cv2.moments(biggest_contour)
    
    # Ensure that moments['m00'] is non-zero to avoid division by zero
    if moments['m00'] != 0:
        center_x = int(moments['m10'] / moments['m00'])
        center_y = int(moments['m01'] / moments['m00'])

        # Adjust the coordinates to the new origin
        center_x -= origin_x
        center_y = int(origin_y - center_y)  # Invert y-coordinate

        # Check if the detected center lies outside of the specified region
        if 215 <= center_x <= 419 and 0 <= center_y <= 480:
            print(f'Center of biggest green object: ({center_x}, {center_y})')
        else:
            center_x = 0
            center_y = 0
    else:
        center_x = 0
        center_y = 0
else:
    center_x = 0
    center_y = 0

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame, frame, mask=mask)

# Display the resulting frame
cv2.imshow('Frame', res)


cap.release()
cv2.destroyAllWindows()
