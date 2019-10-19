#!/usr/bin/env python
'''
 #Method 1 of publishing the mode ,where msg type is STATE
import rospy
from mavros_msgs.msg import State

def callback(data):
  global pub_data
  rospy.loginfo(data.mode)
  pub_data=data # in this the time stamp will also publish
# pub_data=State # in this no time stamp will be publish
  pub_data.connected=0
  pub_data.armed=0
  pub_data.guided=0
  pub_data.mode=data.mode
  pub_data.system_status=0
  pub.publish(pub_data)
  


def mavros_state_subscriber():
   global pub
   rospy.init_node('mav_uav',anonymous=False)
   pub = rospy.Publisher("/uav_mode", State)
   sub = rospy.Subscriber("/mavros/state",State,callback)
   rospy.spin()

if __name__ == '__main__':
  while not rospy.is_shutdown():
    mavros_state_subscriber()
'''

#########################################################################
#Method 2 of publishing the mode ,where Msg type is String

import rospy
from std_msgs.msg import String
from mavros_msgs.msg import State


def callback(state_data):
   uav_mode = state_data.mode
   pub.publish(uav_mode)    
   rospy.loginfo(uav_mode)
def main():
  global pub
  rospy.init_node('mav_uav')
  pub=rospy.Publisher("/uav_mode",String,queue_size=10)
  rate = rospy.Rate(2)

  while not rospy.is_shutdown():
    sub = rospy.Subscriber("/mavros/state",State,callback)  
    rate.sleep()
if __name__ == '__main__':
  main()
