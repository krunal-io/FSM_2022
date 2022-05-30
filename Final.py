#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
PI = 3.1415926535897
value = 0
initialPos = 0

def initialValue(data) :
	global initialPos
	initialPos = data.x
	
def callback(data) :
	global initialPos
	pos = initialPos
	if data.theta == pos :
		rospy.signal_shutdown('finished')


def rotate():
    #Starts a new node
    rospy.init_node('robot_rotate', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    print("Let's rotate your robot")
    angle =3
    speed =2
    vel_msg.linear.x= speed
    vel_msg.angular.z = angle
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < 2.75*angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = (speed*(t1-t0))
        
    vel_msg.linear.x=0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()

rospy.Subscriber('/turtle1/pose', Pose, initialValue)
var_sub = rospy.Subscriber('/turtle1/pose', Pose, callback)	

if __name__ == '__main__':
    try:
        # Testing our function
        rotate()
    except rospy.ROSInterruptException:
        pass
