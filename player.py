import pandas as pd
from bokeh.io import curdoc
from bokeh.models import Tabs
from graf import lig_graf


data = pd.read_csv('C:/Users/s/Desktop/programing/football_player_data/2022-2023 Football Player Stats.csv')

tab_lige = lig_graf(data)

tabs = Tabs(tabs=[tab_lige])
curdoc().add_root(tabs)
