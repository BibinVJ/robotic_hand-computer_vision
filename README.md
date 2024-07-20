# Control of Mechanical Arm Using Computer Vision

The goal of this project is to establish a direct interaction between human hand movements and a robotic arm, utilizing computer vision instead of traditional joystick controls.

## Project Setup

### Hardware Specifications
- Arduino UNO
- Servo motors
- Camera
- Power supply
- Buck converter

## Steps to Setup the Robotic Arm

1. **Assembly**
   - Use the provided 3D model files in `robotic_arm_3Dmodel` directory to print and build the parts for the robotic arm.
    ***or, Alternatively go creative and design a cool hand model***
   - Install and connect the servo motors according to the model specifications.

2. **Arduino Setup**
   - Upload the code from the `arduino_code` directory to the Arduino board.
   - Ensure to note or modify pin configurations as per your setup.
   - Connect each servo motor to its designated pin on the Arduino.

## Steps to Setup the Host Machine (Camera Module)

1. **Python Code**
   - Locate the Python code in the `python_code` directory.
   - Open the code and configure the Arduino COM port, camera COM port, and other variables as needed.
    ***Optionally, utilize the system's built-in camera if required.***

2. **Execution**
   - Run the Python code on the host machine.
   ***!!!BOOM!!!***
   - A window will appear displaying the camera feed, enabling real-time tracking of hand movements.

## Conclusion

With these steps completed, your system is ready to enable intuitive control of the robotic arm through computer vision. Explore the possibilities of this setup for various applications!
