#!/usr/bin/env python
# Author: Saya
# License: MIT

import rospy
from std_msgs.msg import String
from kobuki_msgs.msg import BumperEvent
from kobuki_msgs.msg import Sound

class CollisionWarning:
    def __init__(self):
        rospy.loginfo("collision: launched!")
        self.pub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)
        rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, self.callback)

    def talker(self):
        self.pub.publish(Sound(5))

    def callback(self, data):
        if data.state == BumperEvent.PRESSED:
            rospy.loginfo('hit detected!')
            self.talker()
    

if __name__ == '__main__':
    rospy.init_node('collision_warning', anonymous=True)
    c = CollisionWarning()
    rospy.spin()
