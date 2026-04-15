#!/bin/bash

# Source ROS
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash

# Launch MoveIt
echo "Starting MoveIt..."
roslaunch panda_move_a_to_b moveit.launch &
sleep 5

# Run motion script
echo "Running motion script..."
rosrun panda_move_a_to_b move_a_to_b.py
