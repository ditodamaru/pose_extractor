#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64, Int8
from geometry_msgs.msg import PoseStamped, Twist
from tracking_pid.msg import traj_point  # Replace with the actual package name and message type

def callback(data):
    # Log that a message has been received
    rospy.loginfo("Received a message on /trajectory")    

    # Extract the PoseStamped message
    pose_stamped = data.pose

    # Publish the PoseStamped message to /copy_trajectory topic
    pose_pub.publish(pose_stamped)

    # Log that the message has been successfully published
    rospy.loginfo("Published PoseStamped message to /copy_trajectory")

if __name__ == '__main__':
    rospy.init_node('trajectory_to_pose', anonymous=True)

    # Log that the node has started
    rospy.loginfo("trajectory_to_pose node started")

    # Define the subscriber
    rospy.Subscriber('/trajectory', traj_point, callback)

    # Define the publisher
    pose_pub = rospy.Publisher('/copy_trajectory', PoseStamped, queue_size=10)

    # Keep the node running
    rospy.spin()
