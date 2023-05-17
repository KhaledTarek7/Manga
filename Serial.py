import serial

# Establish Serial Connection
ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace with the correct port name
ser.flushInput()

# Main Loop
while True:
    # Read line from Serial
    line = ser.readline().decode().strip()

    # Check if data is received
    if line:
        pinValue = int(line)
        
        # Perform actions based on pin value
        if pinValue == 1:
            # Pin is HIGH, do something
            print("Pin is HIGH")
            # Continue with your desired actions
        else:
            # Pin is LOW, do something else
            print("Pin is LOW")
            # Continue with your desired actions
    
    # Continue with other code or actions
    
# Close Serial Connection
ser.close()