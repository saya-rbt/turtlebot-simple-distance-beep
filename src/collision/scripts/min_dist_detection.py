# Author: Saya
# License: MIT

import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

class MinDistDetection:
    def __init__(self):
        rospy.init_node('min_dist_detection', anonymous=True)
        rospy.loginfo("min_dist: launched!")
        self.pub = rospy.Publisher('/min_dist', String, queue_size=10)
        rospy.Subscriber('/scan', LaserScan, self.callback)

    def talker(self, val):
        self.pub.publish(val)

    def callback(self, data):
        min_dist_val = str(np.nanmin(data.ranges))
        rospy.loginfo(min_dist_val)
        self.talker(min_dist_val)
    

if __name__ == '__main__':
    c = MinDistDetection()
    rospy.spin()
