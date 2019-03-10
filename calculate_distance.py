from shapely.geometry import Polygon, Point
from dataloader import parse_polygon
import numpy as np
import mpu

TOP_MIN = 10
TOP_MIN_BORNE = 100

def compute_distance(point_coord, poly_def):
    point = Point(point_coord)
    poly = Polygon(poly_def)
    return poly.distance(point)

def compute_borne_distance(point_coord, point_X_def, point_Y_def):
    gps = (point_coord[0], point_coord[1])
    dis_point = (point_X_def, point_Y_def)    
    dist = round(mpu.haversine_distance(munich, berlin), 1)    
    return dist

def compute_distances(point_coord, polys_df):
    data_with_distances = np.array([])
    dist_arr_with_indices = np.array([])
    for index, row in polys_df.iterrows():
        row['GEOMETRIE'] = parse_polygon(row['GEOMETRIE'])
        dist = compute_distance(point_coord, row['GEOMETRIE'])
        dist_arr_with_indices.append(dist)
        row['dist'] = dist
        data_with_distances.append(row)
    min_indices = np.argpartition(dist_arr_with_indices, TOP_MIN)
    return np.take(data_with_distances, min_indices)

def compute_bornes_distances(point_coord, bornes_df):
    data_with_distances = np.array([])
    dist_arr_with_indices = np.array([])
    for index, row in bornes_df.iterrows():
        row['COORDONNEES'] = parse_bornes(row['COORDONNEES'])
        dist = compute_borne_distance(point_coord, row['LONGITUDE'], row['LATITUDE'])
        dist_arr_with_indices.append(dist)
        row['dist'] = dist
        data_with_distances.append(row)
    min_indices = np.argpartition(dist_arr_with_indices, TOP_MIN_BORNE)
    return np.take(data_with_distances, min_indices)