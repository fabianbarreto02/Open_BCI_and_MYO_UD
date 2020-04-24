import pandas as pd
import plotly.graph_objects as go
import numpy as np




df = pd.read_csv('prueba.csv', delimiter=';')

containerEMG = []
for i in range(1,9):
    trace = (go.Scatter(y=df['CH%d '%i], showlegend=True, 
                        name = 'CH%d '%i))
    containerEMG.append(trace)
    

layout = go.Layout(title='Señales EMG capturadas',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=containerEMG, layout=layout)
fig.show()