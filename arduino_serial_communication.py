import serial
import time

# Initialize serial communication with Arduino
ser = serial.Serial('COM6', 9600, timeout=1)

def send_data_to_arduino(data):
    # Ensure data is a string
    if not isinstance(data, str):
        print("Data must be a string.")
        return

    # Send data
    ser.write(data.encode())
    time.sleep(3)  # Give the Arduino time to receive the data

# Test the function
# send_data_to_arduino("Hello, Arduino!")