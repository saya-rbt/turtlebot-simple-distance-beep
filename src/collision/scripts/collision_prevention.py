#!/usr/bin/env python
# Author: Saya
# License: MIT

import rospy

from collision_warning import CollisionWarning
from min_dist_detection import MinDistDetection
from sound_min_dist_feedback import SoundMinDistFeedback

class CollisionPrevention:
	def __init__(self):
		rospy.init_node('collision_prevention', anonymous=True)
		rospy.loginfo("full: launching...")
		mdt = MinDistDetection()
		cw = CollisionWarning()
		smdf = SoundMinDistFeedback()
		rospy.loginfo("full: shutting down")

if __name__ == '__main__':
    c = CollisionPrevention()
    rospy.spin()