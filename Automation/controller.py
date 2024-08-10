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

global current_linear_vel, current_angular_vel

linear_output = linear_pid.update(desired_linear_vel, current_linear_vel)
angular_output = angular_pid.update(desired_angular_vel, current_angular_vel)
msg = Twist()
msg.linear.x = 0.2
msg.angular.z = 0.2
pub.publish(msg)
rate.sleep()

def odom_callback(data):
    global current_linear_vel, current_angular_vel
    current_linear_vel = data.twist.twist.linear.x
    current_angular_vel = data.twist.twist.angular.z

'''def follow_path(bot_path):
    robot_x, robot_y, robot_theta = 0.0, 0.0, 0.0
    pid = PIDController(Kp=1.0, Ki=0.1, Kd=0.01)

    for point in bot_path:
        target_x, target_y = point
        error_x = target_x - robot_x
        error_y = target_y - robot_y
        total_error = (error_x * 2 + error_y * 2) ** 0.5

        steering_angle = pid.compute(total_error)

        # Update robot's position and heading (apply steering_angle)
        # Your robot's kinematics and dynamics come into play here!

        print(f"Steering angle: {steering_angle:.2f} degrees")'''