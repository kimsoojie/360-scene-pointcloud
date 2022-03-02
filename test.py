import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import sys
import math
import cv2

#point cloud

color_raw = cv2.imread('pano_color.jpg')
depth_raw = cv2.imread('pano_depth.jpg',0)

color_raw = cv2.cvtColor(color_raw, cv2.COLOR_BGR2RGB)

h,w = np.shape(depth_raw)
da=2.0*math.pi/float(w)
db=1.0*math.pi/float(h)
a=0.0
b=-0.5*math.pi

points = []
colors = []
for i in range(0,h):
    for j in range(0,w):
        r = depth_raw[i,j] / 255.0
        
        c_0 = color_raw[i,j,0] / 255.0
        c_1 = color_raw[i,j,1] / 255.0
        c_2 = color_raw[i,j,2] / 255.0
        
        xx = r*math.cos(a)*math.cos(b)
        yy = r*math.sin(a)*math.cos(b)
        zz = r*math.sin(b)

        arr = [xx,yy,zz]
        color = [c_0,c_1,c_2]
        if int(r) != 1:
            points.append(arr)
            colors.append(color)
        a=a+da
    b=b+db

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors)

o3d.visualization.draw_geometries([pcd],
                                  zoom=0.5,
                                  front=[0.4257, 0.2125, 0.8795],
                                  lookat=[0,0,0],
                                  up=[0.0, 0.9768, 0.0])

