#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
plt.rc('font',family='Times New Roman',weight='normal')  
import numpy as np 
from netCDF4 import Dataset 
from gmplot import gmplot

fn='/Users/shaoqi/Desktop/NC_H08_20180920_0200_R21_FLDK.02401_02401.nc' 
fn_nc=Dataset(fn) 

lat=fn_nc.variables['latitude'][:].tolist()
lat_min = -20
lat_max = -30
row_min, row_max = lat.index(lat_min), lat.index(lat_max)

lon=fn_nc.variables['longitude'][:].tolist()
lon_min= 130
lon_max= 140 
col_min,col_max = lon.index(lon_min), lon.index(lon_max)

albedo_03 = fn_nc.variables['albedo_03'][:]
albedo_03 = albedo_03[row_min:row_max,:]
albedo_03 = albedo_03[:,col_min:col_max]

row, col = albedo_03.shape
plt.imshow(albedo_03)


# Place map
gmap = gmplot.GoogleMapPlotter(-30, 135, 5)


lat = np.arange(row)*(-0.05)-20
lon = np.arange(col)*(0.05)+130

for i in np.arange(row):
    for j in np.arange(col):
        
        golden_gate_park_lats, golden_gate_park_lons = zip(*[
                (lat[i]-0.025, lon[j]-0.025),
                (lat[i]-0.025, lon[j]+0.025),
                (lat[i]+0.025, lon[j]+0.025),
                (lat[i]+0.025, lon[j]-0.025),
                (lat[i]-0.025, lon[j]-0.025)])
    
        if albedo_03[i,j]<0.2:
            gmap.polygon(golden_gate_park_lats, golden_gate_park_lons,edge_color="red",edge_width=0.8,face_color="red")
        elif albedo_03[i,j]<0.4:
            gmap.polygon(golden_gate_park_lats, golden_gate_park_lons,edge_color="orange",edge_width=0.8,face_color="orange")
        elif albedo_03[i,j]<0.4:
            gmap.polygon(golden_gate_park_lats, golden_gate_park_lons,edge_color="yellow",edge_width=0.8,face_color="yellow")
        elif albedo_03[i,j]<0.6:
            gmap.polygon(golden_gate_park_lats, golden_gate_park_lons,edge_color="lime",edge_width=0.8,face_color="lime")
        elif albedo_03[i,j]<0.8:
            gmap.polygon(golden_gate_park_lats, golden_gate_park_lons,edge_color="green",edge_width=0.8,face_color="green")
        else:
            gmap.polygon(golden_gate_park_lats, golden_gate_park_lons,edge_color="blue",edge_width=0.8,face_color="blue")

# Draw
gmap.draw("my_map.html")

