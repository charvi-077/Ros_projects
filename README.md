# ROS PROJECTS
This repository consistes of my ROS simulation Gazebo projects and presently consists only my latest simulation project on PX4 drone and will soon update it with my other past and future work.


## DRONE SIMULATION
(It is the work done by me and [@pranav083](https://github.com/pranav083))
### drone_sim PACKAGE
First , task includes the setting up of PX4 Gazebo simulator. For that we first tested the PX4 on the MAVLINK and then load the same on the Gazebo Simulator . Then we go through the implementation of  the same in the GAZEBO simulator using the ROS packages for MAVLINK and MAVROS .
Step 1 : Follow the instructions on the PX4 [official site](). and do the complete setup for mavlink and mavros on your pc .
Step 2 : Go to Firmware folder and source it with following commands :
######         source ~/catkin_ws/devel/setup.bash    # (optional)
######         source Tools/setup_gazebo.bash $(pwd) $(pwd)/build/px4_sitl_default
######         export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)
######         export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)/Tools/sitl_gazebo
Step 3 : Run command:  
###### roslaunch px4 mavros_posix_sitl.launch 

Further we build the drone_sim package that currently used for following tasks :
1. Subscribes to the /mavros/state
2. Publishes only to the UAV mode to /uav_mode using the two different message types
3. Calling the services for arming the UAV and takeoff 

#### Tree structure of the given package is :
.
├── CMakeLists.txt
├── package.xml
└── src
    ├── arming_call.py
    ├── mode_publisher.py
    └── state_subscriber.py

#### References 
https://dev.px4.io/master/en/
https://wiki.ros.org/mavros
https://wiki.ros.org/mavlink
