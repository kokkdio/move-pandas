# move-pandas
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
