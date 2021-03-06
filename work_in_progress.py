#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 12:03:53 2019

@author: atmsayfuddin
"""

3857 = meters
4326 = degree

# How to get the area of polygons (in square kilometer) [assuming the polygons are in degrees ]

# load the data
council_districts = gpd.read_file("council_districts.geojson")

# Change council_districts crs to epsg 3857
council_districts = council_districts.to_crs(epsg = 3857)

# Create area in square km
council_districts['area'] = council_districts.geometry.area/10**6

# how to get the center of a polygon
from shapely.geometry import Point
import geopandas as gpd
import pandas as pd

cal = gpd.read_file('CA_Counties_TIGER2016.shp')
la = cal[cal['NAME'] == 'Los Angeles']

# now add a column for the center of the polygon(s)
la['center'] = la.geometry.centroid

# loading hotel data 
hotel = pd.read_csv('dataset.csv')
hotel['geometry'] = hotel.apply(lambda x: Point((x.longitude, x.latitude)), axis = 1)

# Setting the coordinate reference system for the hotel data
hotel_geo = gpd.GeoDataFrame(hotel, crs = {'init':'epsg:4326'}, geometry = hotel.geometry)
hotel_geo = hotel_geo.to_crs({'init': 'epsg:3857'})
hotel_geo = hotel_geo[hotel_geo['city'] == 'Los Angeles']


