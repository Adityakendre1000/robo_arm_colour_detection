import cv2
import numpy as np

# Start the webcam
cap = cv2.VideoCapture(0)

# Define new origin
origin_x = 0
origin_y = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # Bottom of the frame

ret, frame = cap.read()

# Convert the frame from BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Define range for red color in HSV
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([180, 255, 255])

# Threshold the HSV image to get only red colors
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the biggest contour (if any)
if contours:
    biggest_contour = max(contours, key=cv2.contourArea)

    # Calculate the center of the biggest contour
    moments = cv2.moments(biggest_contour)
    center_x = int(moments['m10'] / moments['m00'])
    center_y = int(moments['m01'] / moments['m00'])

    # Adjust the coordinates to the new origin
    center_x -= origin_x
    center_y = int(origin_y - center_y)  # Invert y-coordinate

    # Check if the detected center lies outside of the specified region
    if 215 <= center_x <= 419 and 0 <= center_y <= 480:
        print(f'Center of biggest red object: ({center_x}, {center_y})')
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