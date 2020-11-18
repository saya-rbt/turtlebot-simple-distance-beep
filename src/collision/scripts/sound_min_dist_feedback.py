#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
import numpy as np
from std_msgs.msg import String
from kobuki_msgs.msg import Sound

class SoundMinDistFeedback:
    def __init__(self):
        rospy.init_node('sound_min_dist_feedback', anonymous=True)
        rospy.loginfo("launched!")
        self.pub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=1)
        rospy.Subscriber('/min_dist', String, self.callback)
        self.rateint = 1
        self.change_rate()
    
    def change_rate(self):
        while not rospy.is_shutdown():
            self.rate = rospy.Rate(self.rateint)
            self.rate.sleep()
            self.pub.publish(Sound(3))
            rospy.loginfo("published! going to sleep.")

    def callback(self, data):
        min_dist_val = float(data.data)
        rospy.loginfo("val: " + str(min_dist_val))
        if min_dist_val > 1:
            self.rateint = 1
        elif min_dist_val < 1 and min_dist_val > 0.75:
            self.rateint = 2
        elif min_dist_val < 0.75 and min_dist_val > 0.5:
            self.rateint = 5
        elif min_dist_val < 0.5 and min_dist_val > 0:
            self.rateint = 10
    

if __name__ == '__main__':
    c = SoundMinDistFeedback()
    rospy.spin()
