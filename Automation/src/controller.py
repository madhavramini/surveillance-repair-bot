########################################################################################################

# Wassup! This is where your controller code goes for the Automation Task of the ERC Hackathon '24
#                                      ( Don't ) Lose Control!!!

########################################################################################################

import rospy
from geometry_msgs.msg import Twist, PoseStamped
from nav_msgs.msg import Odometry
import numpy as np

kp_dist=1
ki_dist=0.01
kd_dist=0.5

kp_ang=1
ki_ang=0.03
kd_ang=0.05

class PIDController:
    def _init_(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, error):
        self.integral += error
        derivative = error - self.prev_error
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output
    
rospy.init_node('pid_controller')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
odom_sub = rospy.Subscriber('/odom', Odometry, odom_callback)
path_sub = rospy.Subscriber('/planned_path', Path, path_callback)

linear_pid = PIDController(kp_dist, ki_dist, kd_dist)
angular_pid = PIDController(kp_ang, ki_ang, kd_ang)

    # Desired linear and angular velocities
desired_linear_vel = 0.2
desired_angular_vel = 0.0 

rate = rospy.Rate(10)  # 10 Hz

rn_linear_vel=odom_sub.twist.twist.linear.x
rn_angular_vel=odom_sub.twist.twist.angular.z

linear_output = linear_pid.update(desired_linear_vel, rn_linear_vel)
angular_output = angular_pid.update(desired_angular_vel, rn_angular_vel)
msg = Twist()
msg.linear.x = 0.2
msg.angular.z = 0.2
pub.publish(msg)
rate.sleep()
