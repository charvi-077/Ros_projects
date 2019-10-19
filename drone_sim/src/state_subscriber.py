#!/usr/bin/env python

import rospy
from mavros_msgs.msg import State

def callback(data):
  rospy.loginfo(data)



def mavros_state_subscriber():
   rospy.init_node('state_subscriber',anonymous=False)
   rospy.Subscriber("/mavros/state",State,callback)
   rospy.spin()





if __name__ == '__main__':
  while not rospy.is_shutdown():
    mavros_state_subscriber()
