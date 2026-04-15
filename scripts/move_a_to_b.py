#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
from geometry_msgs.msg import Pose

def main():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("panda_move_a_to_b", anonymous=True)

    # Initialize robot + group
    robot = moveit_commander.RobotCommander()
    group = moveit_commander.MoveGroupCommander("panda_arm")

    # Set planning parameters
    group.set_planning_time(5)
    group.set_num_planning_attempts(5)

    # -------- Pose A --------
    pose_a = Pose()
    pose_a.position.x = 0.4
    pose_a.position.y = 0.0
    pose_a.position.z = 0.4
    pose_a.orientation.w = 1.0

    # -------- Pose B --------
    pose_b = Pose()
    pose_b.position.x = 0.4
    pose_b.position.y = 0.2
    pose_b.position.z = 0.4
    pose_b.orientation.w = 1.0

    rospy.loginfo("Moving to Pose A...")
    group.set_pose_target(pose_a)
    group.go(wait=True)
    group.stop()
    group.clear_pose_targets()

    rospy.sleep(2)

    rospy.loginfo("Moving to Pose B...")
    group.set_pose_target(pose_b)
    group.go(wait=True)
    group.stop()
    group.clear_pose_targets()

    rospy.loginfo("Done.")

if __name__ == "__main__":
    main()
