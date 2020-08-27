cmake_minimum_required(VERSION 3.0.2)
project(pi_rover)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
  vnh5019_motor_controller
)

## Python Setup
catkin_python_setup()

## Declare things to be passed to dependent projects
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES pi_rover
#  CATKIN_DEPENDS geometry_msgs rospy vnh5019_motor_controller
#  DEPENDS system_lib
)

## Specify additional locations of header files
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

## Mark executable scripts (Python etc.) for installation
catkin_install_python(PROGRAMS
  nodes/pi_rover
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Mark other files for installation (e.g. launch and bag files, etc.)
install(FILES
  launch/pi_rover.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

