# ROS Client
import rospy

# Messages and Services
from geometry_msgs.msg import Twist 
from vnh5019_serial_controller.msg import MixedCommand

# Standard Libraries
from time import sleep

# Publisher For Controlling Motors
motors = rospy.Publisher('vnh5019_motor_controller', MixedCommand, queue_size=10) 

def get_direction(data):
    global motors

    speed = 0
    if data.linear.x > 0:
        speed = 50
    elif data.linear.x < 0:
        speed = -50

    turn = 0
    if data.angular.z < 0:
        turn = 50
    elif data.angular.z > 0:
        turn = -50

    motors.publish(MixedCommand(speed=speed, turn=turn))


def setup():
    rospy.init_node("pi_rover")
    rospy.Subscriber("robot_twist", Twist, get_direction)


def loop():
    while not rospy.is_shutdown():
        rospy.spin()


def pi_rover():
    setup()
    loop()

