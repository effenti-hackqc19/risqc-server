import pandas as pd
import sys

RISQZONES_FILE = 'datasets/vdq-zonesinondablesarisques.csv'
CONTROLLED_RISQ_ZONES = 'datasets/vdq-zonesinondablesreglementees.csv'
BORNES_FONTAINES = 'datasets/vdq-bornefontaine.csv'

df = pd.read_csv(RISQZONES_FILE)
df_cont = pd.read_csv(CONTROLLED_RISQ_ZONES)

def parse_polygon(poly_string):
    extracted_tuple = poly_string[10:-2]
    arr = extracted_tuple.split(',')
    arr_values = []
    for longlat in arr:
        coord = dict()
        coord['lng'] = longlat.split()[0]
        coord['lat'] = longlat.split()[1]
        arr_values.append(coord)
    return arr_values

def parse_bornes(bornes_string):
    extracted_tuple = bornes_string[5:-1]
    arr = extracted_tuple.split(',')
    arr_values = []
    for longlat in arr:
        coord = dict()
        coord['lng'] = longlat.split()[0]
        coord['lat'] = longlat.split()[1]
        arr_values.append(coord)
    return arr_values


dfs = pd.concat([df,df_cont], axis=0)
dfs_bornes['COORDONNEES']=dfs_bornes2.apply(lambda x:'Point(%s %s)' % (x['LONGITUDE'],x['LATITUDE']),axis=1)

dfs['GEOMETRIE'].apply(lambda x: parse_polygon(x))
dfs_bornes['COORDONNEES'].apply(lambda x: parse_bornes(x))