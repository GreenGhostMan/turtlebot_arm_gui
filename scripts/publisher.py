#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import Float64 as f64

class general_publisher:
	def __init__(self,name):
		"""ghostman"""
		self.joint_list = ['shoulder_pan_joint','shoulder_lift_joint','elbow_flex_joint','wrist_flex_joint','gripper_joint']
		self.name = name        	
		self.topic_1 = "/arm_"+self.joint_list[0]+"/command"
		self.topic_2 = "/arm_"+self.joint_list[1]+"/command"
		self.topic_3 = "/arm_"+self.joint_list[2]+"/command"
		self.topic_4 = "/arm_"+self.joint_list[3]+"/command"
		self.topic_5 = self.joint_list[4]+"/command" # gripper_joint

		self.param_1 = self.joint_list[0]+"/degree"
		self.param_2 = self.joint_list[1]+"/degree"
		self.param_3 = self.joint_list[2]+"/degree"
		self.param_4 = self.joint_list[3]+"/degree"
		self.param_5 = self.joint_list[4]+"/degree"

		rospy.init_node(self.name)

		self.rate = rospy.Rate(20) #10hz
		self.pub_1 = rospy.Publisher(self.topic_1,f64,queue_size=10)
		self.pub_2 = rospy.Publisher(self.topic_2,f64,queue_size=10)
		self.pub_3 = rospy.Publisher(self.topic_3,f64,queue_size=10)
		self.pub_4 = rospy.Publisher(self.topic_4,f64,queue_size=10)
		self.pub_5 = rospy.Publisher(self.topic_5,f64,queue_size=10)

		msg_1 = f64()
		msg_2 = f64()
		msg_3 = f64()
		msg_4 = f64()
		msg_5 = f64()		

		while not rospy.is_shutdown():
			self.degree_1 = rospy.get_param(self.param_1,default=150 )
			self.degree_2 = rospy.get_param(self.param_2,default=150 )
			self.degree_3 = rospy.get_param(self.param_3,default=150 )
			self.degree_4 = rospy.get_param(self.param_4,default=150 )
			self.degree_5 = rospy.get_param(self.param_5,default=50 )

			msg_1.data = self.deg_to_rad(self.degree_1)
			msg_2.data = self.deg_to_rad(self.degree_2)
			msg_3.data = self.deg_to_rad(self.degree_3)
			msg_4.data = self.deg_to_rad(self.degree_4)
			msg_5.data = self.gripper_remap(self.degree_5)

			self.pub_1.publish(msg_1)
			self.pub_2.publish(msg_2)
			self.pub_3.publish(msg_3)
			self.pub_4.publish(msg_4)
			self.pub_5.publish(msg_5)

			self.rate.sleep()

	def deg_to_rad(self,x):
		# remap (0,300 to -150,150)
		y = x - 150
		# deg to radian
		return 0.017453278*y
	def gripper_remap(self,x):
		# remap and change radian (0,100 to 0.5,-0.5)
		y = (-0.01*x) +0.5
		return y

def main(args):
	gp = general_publisher("general_publisher")	
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print "Shutting down"

if __name__ =="__main__":
	main(sys.argv)