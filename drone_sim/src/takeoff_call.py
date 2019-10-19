#!/usr/bin/env python

import rospy
from mavros_msgs.srv import CommandBool

rospy.init_node('takeoff_call')
rospy.wait_for_service('/mavros/cmd/takeoff
')

takeff_request = rospy.ServiceProxy('/mavros/cmd/takeoff
',CommandBool)

value = 1

takeoff_response = takeoff_request(value)

print (takeoff_response.success)
~                               
