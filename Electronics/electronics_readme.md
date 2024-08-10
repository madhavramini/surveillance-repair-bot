# SIMULATION OF AN ELECTRICAL FAILURE DETECTION ROBOT
Simulating an electrical failure detection and repair bot on Tinkercad was completed using the following components:

## Components Used:
1. Arduino Uno
2. Raspberry Pi (Note: The Raspberry Pi was represented theoretically as it was not available in Tinkercad)
3. Power Bank
4. LiDAR (Note: An ultrasonic sensor was used to simulate LiDAR)
5. 2 Cameras (assumed to be connected—one to the Raspberry Pi and the other to the Arduino via I2C)
6. 2 DC Motors
7. 6 Servo Motors (4 on the robotic arm)

## Assumptions Made:
- The LiDAR was represented by an ultrasonic sensor.
- The Raspberry Pi's functionality was simulated theoretically.
- The power bank was assumed to be the main power source.

## Circuit Connections:
### Power Distribution:
1. Power Bank:
   - The positive terminal was connected to the positive power rail on the breadboard.
   - The negative terminal was connected to the negative power rail on the breadboard.

2. Arduino:
   - The Arduino's 5V pin was connected to the positive power rail.
   - The Arduino's GND pin was connected to the negative power rail.

3. Raspberry Pi:
   - Connections were assumed to be made to the power bank, and communication with Arduino was represented via Serial/I2C.

### DC Motors:
1. L293D Motor Driver IC:
   - Pin 1 (Enable 1-2) was connected to Arduino pin 10.
   - Pin 2 (Input 1) was connected to Arduino pin 2.
   - Pin 3 (Output 1) was connected to DC Motor 1's positive terminal.
   - Pin 4 (Ground) was connected to the negative power rail.
   - Pin 5 (Ground) was connected to the negative power rail.
   - Pin 6 (Output 2) was connected to DC Motor 1's negative terminal.
   - Pin 7 (Input 2) was connected to Arduino pin 3.
   - Pin 8 (Vcc2) was connected to the positive power rail (9V from the power bank).
   - Pin 9 (Enable 3-4) was connected to Arduino pin 11.
   - Pin 10 (Input 3) was connected to Arduino pin 4.
   - Pin 11 (Output 3) was connected to DC Motor 2's positive terminal.
   - Pin 12 (Ground) was connected to the negative power rail.
   - Pin 13 (Ground) was connected to the negative power rail.
   - Pin 14 (Output 4) was connected to DC Motor 2's negative terminal.
   - Pin 15 (Input 4) was connected to Arduino pin 5.
   - Pin 16 (Vcc1) was connected to the positive power rail (5V from Arduino).

2. Servo Motor Connections:
   - Each servo motor's power pin was connected to the 5V power rail.
   - Each servo motor's ground pin was connected to the ground rail.
   - Control pins were connected to Arduino digital pins (6, 7, 8, 9 for the robot arm, and 12 and 13 for other functions).

### Ultrasonic Sensor (Simulating LiDAR):
   - VCC was connected to the positive power rail.
   - GND was connected to the negative power rail.
   - The Trig pin was connected to Arduino pin A0.
   - The Echo pin was connected to Arduino pin A1.

### Camera:
   - The main camera was assumed to be connected to the Raspberry Pi.
   - The gripper camera was assumed to be connected to the Arduino via I2C.


This setup provided a basic framework for simulating a bot that could move, detect obstacles, and control a robotic arm using servos. The actual implementation with a Raspberry Pi and advanced sensors like LiDAR would require more complex programming and setup, but this provided a good starting point for simulation on Tinkercad.
