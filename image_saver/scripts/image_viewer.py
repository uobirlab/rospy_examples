#!/usr/bin/env python
import roslib
import rospy

# Import opencv
import cv

from sensor_msgs.msg import Image

from cv_bridge import CvBridge, CvBridgeError  # to convert sensor_msgs to OpenCV image

class RosImageSubscriber(object):
  def __init__(self):
    cv.NamedWindow("Image window", 1)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/image_raw",
                                      Image,
                                      self.image_cb)

  def image_cb(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
    except CvBridgeError, e:
      print e

    cv.ShowImage("Image window", cv_image)
    cv.WaitKey(10)


if __name__ == '__main__':
  rospy.init_node('python_image_subscriber', anonymous=True)
  subber = RosImageSubscriber()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"

  cv.DestroyAllWindows()

