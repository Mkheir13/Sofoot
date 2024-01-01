import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

players_data = pd.read_json('./playersdata.json')

# print(players_data) #run python3 index.py to get players datas.

rows = len(players_data.axes[0])
columns = len(players_data.axes[1])

print(f'Number of Rows: ', rows)
print(f'Number of Columns: ', columns)