# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 18:41:44 2022

@author: student
"""

import pyrealsense2.pyrealsense2 as rs
import numpy as np
#import matplotlib.pyplot as plt
import cv2

pipeline = 0 #Do not delete this line
def set_min_distance(new_min_dist=0.0,new_max_dist=10.0):
        global pipeline
        pipeline= rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        profile = pipeline.start(config) # Start streaming
        sensor_dep = profile.get_device().first_depth_sensor()
        if sensor_dep.supports(rs.option.min_distance):
            print ("Trying to set min_distance")
            min_dist = sensor_dep.get_option(rs.option.min_distance)
            print("min_distance = %d" % min_dist)
            print("Setting min_distance to new value")
            min_dist = sensor_dep.set_option( rs.option.min_distance, new_min_dist)
            
            min_dist = sensor_dep.get_option(rs.option.min_distance)
            print("New min_distance = %d" % min_dist)
        if sensor_dep.supports(rs.option.max_distance):
            print ("Trying to set max_distance")
            max_dist = sensor_dep.set_option( rs.option.max_distance, new_max_dist)
        profile = pipeline.stop
        return pipeline
#Set global pipeline up
pipeline = set_min_distance()

def get_depth_frame():
        global pipeline
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()   
        return depth_frame
def find_distance(x,y,depth_frame):

    # Create a context object. This object owns the handles to all connected realsense devices
    depth = depth_frame.get_distance(x,y)
    print("(X,Y): ",x,y,str(depth),"Meters")   
    return(depth)


def colorize_lidar(depth_frame=None):
    if depth_frame ==None:
        depth_frame = get_depth_frame()
    colorizer = rs.colorizer(color_scheme=0)
    colorizer.set_option(rs.option.max_distance,16)
    colorized_depth = np.asanyarray(colorizer.colorize(depth_frame).get_data())
    
    im_gray=cv2.cvtColor(colorized_depth, cv2.COLOR_BGR2GRAY)
    #plt.imshow(im_gray)
    out=cv2.threshold(im_gray,1,255,cv2.THRESH_BINARY)
    #out=plt.imread(out)

    
    #img = out[1]
    #return out[1]
    return colorized_depth
def main(x,y):
    global pipeline

    depth_frame = get_depth_frame()
    distance = find_distance(x,y,depth_frame)
    #colorize_lidar(depth_frame) #This plots an output of the lidar so you can see it.
    return distance

#main(10,10)
#depth_frame = get_depth_frame()
#print(depth_frame.as_points())
#print(find_distance(300,300,depth_frame))