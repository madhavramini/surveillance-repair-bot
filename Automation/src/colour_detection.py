#!/usr/bin/env python3


########################################################################
#    Hi~ This is where your code to detect the color of the cone goes 
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣄⣀⣀⣠⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⢿⣿⣿⡿⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣶⣤⣤⣤⣤⣤⣤⣶⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⣀⣠⣤⡖⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢶⣤⣄⣀⠀⠀⠀⠀
# ⠀⠀⠀⠉⠙⠻⢿⣿⡀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢀⣿⡿⠟⠋⠉⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠢⠤⣤⣀⣈⣁⣀⣤⠤⠔⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#
#########################################################################

import cv2
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge

red_lower = (0, 100, 100)
red_upper = (10, 255, 255)
blue_lower = (100, 100, 100)
blue_upper = (140, 255, 255)

class ColourDetector:
    def __init__(self):
        rospy.init_node('colour_detector')
        self.image_sub = rospy.Subscriber('/camera/image_raw', Image, self.image_callback)
        self.task_status_pub = rospy.Publisher('task_status', String, queue_size=10)
        self.bridge = CvBridge()

    def image_callback(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")


        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        red_mask = cv2.inRange(hsv, red_lower, red_upper)
        blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
        mask = cv2.bitwise_or(red_mask, blue_mask)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        red = cv2.countNonZero(red_mask[y:y+h, x:x+w])
        blue = cv2.countNonZero(blue_mask[y:y+h, x:x+w])

        if red > blue:
            self.task_status_pub.publish("Red Cone: \"Error detected at site\"")
        else:
            self.task_status_pub.publish("Blue Cone: \"No error detected\"")

if __name__ == '__main__':
    colour_detector = ColourDetector()
    rospy.spin()
