import cv2
import math

# Callback function for mouse events
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Convert the coordinates with respect to the bottom left corner of the frame
        y_inverted = frame.shape[0] - y  # Invert the y-coordinate to make the positive direction upwards

            # Calculate the angle from (27, 153) to the clicked point
        dx = x - 27
        dy = y_inverted - 153
        angle = math.atan2(dy, dx) * 180 / math.pi  # Convert to degrees
        if angle < 0:
            angle += 360  # Convert to the range [0, 360]

        print(f'Coordinates: ({x}, {y_inverted}), Angle: {angle} degrees')

# Start the webcam
cap = cv2.VideoCapture(0)

# Create a named window
cv2.namedWindow('Frame')

# Set the callback function for mouse events
cv2.setMouseCallback('Frame', get_coordinates)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Draw a vertical line passing through (27, y)
    cv2.line(frame, (27, 0), (27, frame.shape[0]), (0, 255, 0), 1)

    # Draw a horizontal line passing through (x, 153)
    cv2.line(frame, (0, frame.shape[0] - 153), (frame.shape[1], frame.shape[0] - 153), (0, 255, 0), 1)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()