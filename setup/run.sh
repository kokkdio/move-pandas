#!/bin/bash

# Source ROS properly
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash

echo "Starting MoveIt..."
roslaunch panda_move_a_to_b moveit.launch &
LAUNCH_PID=$!

# wait a bit for MoveIt to start
sleep 5

echo "Running motion script..."
rosrun panda_move_a_to_b move_a_to_b.py debug

wait $LAUNCH_PID
