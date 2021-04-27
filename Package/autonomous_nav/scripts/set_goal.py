#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import euler_from_quaternion, quaternion_from_euler
# Callbacks definition
def active_cb(extra):
    rospy.loginfo("Goal pose being processed")

def feedback_cb(feedback):
    rospy.loginfo("Current location: "+str(feedback))

def done_cb(status, result):
    if status == 3:
        rospy.loginfo("Goal reached")
    if status == 2 or status == 8:
        rospy.loginfo("Goal cancelled")
    if status == 4:
        rospy.loginfo("Goal aborted")

# def get_rotation(msgs):
#     global roll, pitch, yall
#     orientation_q = msgs.target_pose.pose.orientation
#     orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
#     (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
#     print ("Yaw =",yaw)
    
rospy.init_node('send_goal')

navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
navclient.wait_for_server()

# Example of navigation goal
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.pose.position.x = rospy.get_param('/pose_x')
goal.target_pose.pose.position.y = rospy.get_param('/pose_y')
goal.target_pose.pose.position.z = rospy.get_param('/pose_z')
goal.target_pose.pose.orientation.x = rospy.get_param('/orie_x')
goal.target_pose.pose.orientation.y = rospy.get_param('/orie_y')
goal.target_pose.pose.orientation.z = rospy.get_param('/orie_z')
goal.target_pose.pose.orientation.w = rospy.get_param('/orie_w')

# goal.target_pose.pose.position.y = 0.764
# goal.target_pose.pose.position.z = 0.0
# goal.target_pose.pose.orientation.x = 0.0
# goal.target_pose.pose.orientation.y = 0.0
# goal.target_pose.pose.orientation.z = 0.662
# goal.target_pose.pose.orientation.w = 0.750
navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
finished = navclient.wait_for_result()

if not finished:
    rospy.logerr("Action server not available!")
else:
    rospy.loginfo ( navclient.get_result())
