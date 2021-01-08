#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n=0
m=0
s=0
r=0

def cb(message):
    global n
    global m
    global s
    global r
    a=b=c=d=0
    n = message.data
    s = n
    if n == 60:
        m = m + 100
        s = 0
    r = m + s

rospy.init_node('time')
sub = rospy.Subscriber('count_up',Int32,cb)
pub = rospy.Publisher('time',Int32,queue_size=1)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    pub.publish(r)
    rate.sleep()
