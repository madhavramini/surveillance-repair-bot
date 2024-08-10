# Automation Team

## Cone Detection:
Used OpenCV to detect the color of the cones (red/blue).

Received image data from `/camera/image_raw` topic, and converted it to CV2 data.

Used Contour and Color range functions to determine whether the cones are red or blue.

Published strings based on color detected to the `/task_status` topic.


## Path Planning:
Used RRT* sampling and A* graph algorithm.

The planner node publishes the predicted gazebo coordinates to the PID controller.

## PID Controller:
Created a basic PID controller class

Linear and angular velocities get updated every 0.01s

The velocities are then published to `/cmd_vel` to move the bot.
