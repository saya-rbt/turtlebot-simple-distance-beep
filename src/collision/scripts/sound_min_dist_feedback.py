#!/usr/bin/env python
# Author: Saya
# License: MIT

import rospy
import numpy as np
from std_msgs.msg import String
from kobuki_msgs.msg import Sound

class SoundMinDistFeedback:
    def __init__(self):
        rospy.loginfo("beeper: launched!")
        self.pub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=1)
        rospy.Subscriber('/min_dist', String, self.callback)
        self.rateint = 1
        self.change_rate()
    
    def change_rate(self):
        while not rospy.is_shutdown():
            self.rate = rospy.Rate(self.rateint)
            self.rate.sleep()
            self.pub.publish(Sound(3))
            rospy.loginfo("beep! going to sleep.")

    def callback(self, data):
        min_dist_val = float(data.data)
        rospy.logdebug("val: " + str(min_dist_val))
        if min_dist_val > 1:
            self.rateint = 1
        elif min_dist_val < 1 and min_dist_val > 0.75:
            self.rateint = 2
        elif min_dist_val < 0.75 and min_dist_val > 0.5:
            self.rateint = 5
        elif min_dist_val < 0.5 and min_dist_val > 0:
            self.rateint = 10
    

if __name__ == '__main__':
    rospy.init_node('sound_min_dist_feedback', anonymous=True)
    c = SoundMinDistFeedback()
    rospy.spin()
