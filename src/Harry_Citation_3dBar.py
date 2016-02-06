# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:18:09 2016

@author: xilin
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
# Data generation
citation_dist = pd.read_csv("~/Projects/Motorola_Patent_Citations/data/Citation_distribution_all_Harry.csv")

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
xpos = citation_dist['pub_year'].tolist()
num_elements = len(xpos)

ypos = citation_dist['CitMonth'].tolist()
ypos1 = [0] * num_elements
#for i in range(0,num_elements):
#    yposelement = ypos[i].split('-')
#    ypos1[i] = float(yposelement[0]+'.'+yposelement[1])
for i in range(0, num_elements):
    monthStrings = ypos[i].split('-')
    monthCount = 12*(int(monthStrings[0]) - 2011) + int(monthStrings[1])
    ypos1[i] = monthCount


zpos = z = [0] * num_elements
dx = [0.35] * num_elements
#dx = np.ones(num_elements)
dy = [0.9] * num_elements
#dy = np.ones(num_elements)
dz = citation_dist['count'].tolist()

ax1.set_xlabel('Year of Publication')
ax1.set_ylabel('Month of Citation from 2011 to 2014')
#ax1.bar3d(xpos, ypos1, zpos, dx, dy, dz, color='#00ceaa')
ax1.bar3d(xpos, ypos1, zpos, dx, dy, dz, color = '#C4D4FF')
plt.show()
