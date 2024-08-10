########################################################################################################

# Wassup! This is where your Path Planning code goes for the Automation Task of the ERC Hackathon '24
#
# Remember to use the transform points function in obstacle_detection.py to get points corresponding to
#         your path in the gazebo coordinate system. This is what controller.py should use!!
#
#                                       Happy Planning!!!

########################################################################################################

# import functions from obstacle_detection.py

# Cooridinates of the cones as per the map (image version) - look at get_landmarks.py & obstacle_detection.py
# ERC Room: 109, 296
# Cone 1: 159, 208
# Cone 2: 296, 142
# Cone 3: 502, 539
# Cone 4: 244, 640
# Cone 5: 190, 326

# You can look at the visualization function in demo.py to see how to visualize the path

# These are the coordinates you have to go to in Gazebo
# Start Location (ERC Room): 12.994061, 14.233000
# Cone 1 (near Sandbox): 19.765875, 10.429128
# Cone 2 (NAB): 24.820259, -0.089209
# Cone 3 (VGH): -5.729289, -15.973051
# Cone 4 (SAC): -13.520048, 3.922464
# Cone 5 (BDome): 10.654515,8.028189
# Cones colors will be randomized

# There is a function to convert the obstacle_detection-> Maze-> points point_transform

import random
import rospy
from geometry_msgs.msg import PoseStamped, Path
import numpy as np
from obstacle_detection import Maze
_build_class_

rospy.init_node('path_planner')
pub = rospy.Publisher('/planned_path', Path, queue_size=10)

maze = Maze()

target_points = [[(159,208),(296,142),(502,539),(244,640),(190,326)] for i in range(15)]

switch = True
collection = [[(109,296)] for i in range(15)]
k = 0
while (switch):
    for i in range(15):
        for item in target_points[i]:
            if(maze.isValidPoint(item[0],item[1],collection[i][-1][0], collection[i][-1][1])):
                connection = maze.bresenham_line(item[0],item[1],((collection[i])[-1])[0], (((collection[i])[-1])[1]))
                collection[i].extend(connection)
                target_points[i].pop(target_points[i].index(item))
                
                
        if (len(target_points[i]) == 0):
            print("Route found")
            min_length = i
            maze.visualize_path(collection[i])
            switch = False
            break
        cond = False
        while(cond == False):
            x = collection[i][-1][0]
            y = collection[i][-1][1]
            rand_x = int(random.uniform(x-30, x+30))
            rand_y = int(random.uniform(y-30, y+30))
            if(maze.roads[rand_y, rand_x] == 255):
                if(maze.isValidPoint(collection[i][-1][0],collection[i][-1][1], rand_x, rand_y)):
                    cond=True          
        collection[i].append((rand_x, rand_y))
        points = maze.bresenham_line(collection[i][-1][0],collection[i][-1][1], rand_x, rand_y)
        collection[i].extend(points)
        k = k+1
        print(k)

gazebo_collection = list(map(maze.point_transform,collection[min_length]))

path_msg = Path()
path_msg.header.stamp = rospy.Time.now()
path_msg.header.frame_id = "map"

for col in gazebo_collection:
    pose_stamped = PoseStamped()
    pose_stamped.header.stamp = path_msg.header.stamp
    pose_stamped.header.frame_id = "map"
    pose_stamped.pose.position.x = col[0]
    pose_stamped.pose.position.y = col[1]

pub.publish(path_msg)