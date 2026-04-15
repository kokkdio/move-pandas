# Panda Move A to B

Simple ROS Noetic + MoveIt project to move a Franka Panda arm between two poses.

## Requirements
- Ubuntu 20.04 (Focal)
- ROS Noetic
- franka_ros
- panda_moveit_config

## Setup

```bash
cd ~/catkin_ws/src
git clone <your-repo>
cd ..
catkin_make
source devel/setup.bash

chmod +x setup/run.sh
cd panda_move_a_to_b/setup./run.sh  

export ROBOT_IP=<robot-ip>
roslaunch franka_control franka_control.launch robot_ip:=$ROBOT_IP
roslaunch panda_move_a_to_b moveit.launch
rosrun panda_move_a_to_b move_a_to_b.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
T1
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash
roscore


T2
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash
roslaunch panda_gazebo panda_world.launch

T3
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash
roslaunch panda_moveit_config panda_moveit.launch

T4
cd ~/catkin_ws/src
catkin_create_pkg my_panda_scripts rospy std_msgs moveit_commander geometry_msgs
cd my_panda_scripts
mkdir scripts
cd scripts
nano move_panda.py



cd ~/catkin_ws
catkin_make
source devel/setup.bash

rosrun my_panda_scripts move_panda.py


panda_move_a_to_b/
├── README.md
├── scripts/
│   └── move_a_to_b.py
├── launch/
│   └── moveit.launch
├── setup/
│   └── run.sh
└── .gitignore

