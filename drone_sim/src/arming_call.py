#!/usr/bin/env python

import rospy
from mavros_msgs.srv import CommandBool

rospy.init_node('arming_call')
rospy.wait_for_service('/mavros/cmd/arming')

arming_request = rospy.ServiceProxy('/mavros/cmd/arming',CommandBool)

value = 1

arming_response = arming_request(value)

print (arming_response.success)
