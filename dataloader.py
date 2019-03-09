import pandas as pd

RISQZONES_FILE = 'datasets/vdq-zonesinondablesarisques.csv'
CONTROLLED_RISQ_ZONES = 'datasets/vdq-zonesinondablesreglementees.csv'

df = pd.read_csv(RISQZONES_FILE)
df_cont = pd.read_csv(CONTROLLED_RISQ_ZONES)

dfs = pd.concat([df,df_cont], axis=0)
