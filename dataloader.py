import pandas as pd
import sys

RISQZONES_FILE = 'datasets/vdq-zonesinondablesarisques.csv'
CONTROLLED_RISQ_ZONES = 'datasets/vdq-zonesinondablesreglementees.csv'

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

dfs = pd.concat([df,df_cont], axis=0)
dfs['GEOMETRIE'].apply(lambda x: parse_polygon(x))
