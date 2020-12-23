import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table

from app import app
import dash_table
import pandas as pd


import plotly.express as px
import plotly.graph_objs as go

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer



from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


#fichiers
emotion_f = pd.read_csv('/home/cecilia/Documents/brief/brief_emotions/emotion_dash/Emotion_final.csv')
df2 = emotion_f[:50]
emotion_t = pd.read_csv('/home/cecilia/Documents/brief/brief_emotions/emotion_dash/text_emotion.csv')
df4 = emotion_t[:50]
df_count_emotion = emotion_f.groupby(['Emotion']).size().reset_index(name='Count')
df = df_count_emotion















layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1'),

        dcc.Tab(label='Tab two', value='tab-2'),
    ]),
    html.Div([(id='tabs-content', children=[
    
        dash_table.DataTable(
            data=df2.to_dict('records'),
            export_format='csv',
            columns=[{'id': c, 'name': c} for c in df2.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'height': 'center',
                'width': 'center',
                'whiteSpace': 'normal',
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white'
                }
            )
        ]),






])





@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])

