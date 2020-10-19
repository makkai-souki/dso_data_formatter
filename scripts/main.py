#!/usr/bin/env python

import rospy
from dso_data_formatter.msg import odom_message
from dso_data_formatter.msg import points_message
import pandas as pd


def export_csv(df, filename='export.csv'):
    df.to_csv(filename, index=False, mode='a', header=False)


def odom_callback(odom_msg):
    timestamp = float(odom_msg.header.stamp.secs) + float(odom_msg.header.stamp.nsecs) / 1000000000
    # print timestamp
    df = pd.DataFrame([[float(odom_msg.pose.position.x), float(odom_msg.pose.position.y), float(odom_msg.pose.position.z), timestamp]])
    export_csv(df)
    

if __name__ == "__main__":
    pd.DataFrame([[0,0,0,0]]).to_csv('export.csv', index=False, header=False)
    rospy.init_node('dso_reader', anonymous=True)
    rospy.Subscriber('/test/vodom', odom_message, odom_callback)
    # rospy.Subscriber('/test/points', points_message, points_callback)
    rospy.spin()
