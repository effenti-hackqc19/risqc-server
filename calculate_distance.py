from shapely.geometry import Polygon, Point
from dataloader import parse_polygon
import numpy as np

TOP_MIN = 10

def compute_distance(point_coord, poly_def):
    point = Point(point_coord)
    poly = Polygon(poly_def)
    return poly.distance(point)

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


#poly = Polygon([[25.774252, -80.190262], [18.466465, -66.118292], [32.321384, -64.75737], [25.774252, -80.190262]] )
#point = Point([26.254629577800088, -72.728515625] )

#poly.distance(point)