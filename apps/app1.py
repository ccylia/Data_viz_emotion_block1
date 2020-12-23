#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app
import dash_table
import pandas as pd

import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import plotly.graph_objs as go

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from dash.dependencies import Input, Output




#fichiers
emotion_f = pd.read_csv('/home/cecilia/Documents/brief/brief_emotions/emotion_dash/Emotion_final.csv')
df2 = emotion_f[:50]

emotion_t = pd.read_csv('/home/cecilia/Documents/brief/brief_emotions/emotion_dash/text_emotion.csv')
df4 = emotion_t[:50]


df_count_emotion = emotion_f.groupby(['Emotion']).size().reset_index(name='Count')
df = df_count_emotion

df_count_emotion2 = emotion_t.groupby(['sentiment']).size().reset_index(name='Count')
df5=df_count_emotion2




#definition des themes
colors = {
    'background': '#111111',#111111 fbf6f6  7FDBFF
    'text': '#fbf6f6',
    'bar' : '#f90d0d',
    'gris':'rgb(30, 30, 30)',
    'blanc': '#fefdfd',
}




#fig1
fig = px.histogram(df,x='Emotion', y= 'Count', labels={'x':'Emotions', 'y':'Nombre d\'apparition'})        
                                #, ascending = False) ##############################
fig.update_layout(
    plot_bgcolor=colors['blanc'],
    paper_bgcolor=colors['blanc'],
    font_color=colors['background']
)


#fig2
d = emotion_f.Text
vec = CountVectorizer(stop_words='english')
X=vec.fit_transform(d)
words = vec.get_feature_names()
wsum = np.array(X.sum(0))[0]
ix = wsum.argsort()[::-1]
wrank = wsum[ix] 
labels = [words[i] for i in ix]
def subsample(x, end, step=400):
    return np.hstack((x[:30], x[30:end:step]))
freq = subsample(wrank,30)


fig2 = px.bar(x=subsample(labels, 30),y = freq, labels={'x':'Mots', 'y':'Répartition'})
fig2.update_layout(
    plot_bgcolor=colors['blanc'],
    paper_bgcolor=colors['blanc'],
    font_color=colors['background']
    
)
#fig4
fig4 = px.histogram(df5,x='sentiment', y= 'Count', labels={'x':'sentiment', 'y':'Nombre d\'apparition'})        
                                 #, ascending = False) ##############################
fig4.update_layout(
    plot_bgcolor=colors['blanc'],
    paper_bgcolor=colors['blanc'],
    font_color=colors['background']
)

#fig9
d2 = emotion_t.content
vec = CountVectorizer(stop_words='english')
X2=vec.fit_transform(d2)
words2 = vec.get_feature_names()
wsum = np.array(X.sum(0))[0]
ix = wsum.argsort()[::-1]
wrank = wsum[ix] 
labels = [words2[i] for i in ix]
def subsample(x, end, step=400):
    return np.hstack((x[:30], x[30:end:step]))
freq2 = subsample(wrank,30)

fig9 = px.bar(x=subsample(labels, 30),y = freq2, labels={'x':'Mots', 'y':'Répartition'})
fig9.update_layout(
    plot_bgcolor=colors['blanc'],
    paper_bgcolor=colors['blanc'],
    font_color=colors['background']
    
)








# titre en tete
layout = html.Div(children=[
    html.Div(children=[
        html.H1(
            children='Emotions',
            style={
                'textAlign': 'center',
                }
            )
        ]),
# titre 2nd
    html.Div( children=html.Div(
        '50 premières lignes des deux fichiers',
         style={
        'textAlign': 'center',
    })
        ),
#tabs
    html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Fichier 1', value='tab-1'),
        dcc.Tab(label='Fichier 2', value='tab-2'),
    ]),
    html.Div(id='tabs-content'),

    ]),

    html.Br(),
    html.Br(),
    html.Br(),

#Titre suite
    html.Div(style={'backgroundColor': colors['blanc']}, children=[
        html.H2(
            children='Graphiques pour mise en évidence de corrélation',
            style={
                'textAlign': 'center',
                'color': colors['background']
                }
            )
        ]),

#titre 1er graph fichier 1
    html.Div(style={'backgroundColor': colors['blanc']}, 
             children=html.Div(
             'Histogramme d\'apparition des émotions fichier 1',
         style={
        'textAlign': 'center',
        'color': colors['background']
    })
        ),

#1er graph fichier 1
    dcc.Graph(
        id='example-graph-2',
        figure=fig
        
        ),

     html.Br(),

#titre 1er graph fichier 2
    html.Div(style={'backgroundColor': colors['blanc']}, 
             children=html.Div(
             'Histogramme d\'apparition des émotions fichier 2',
         style={
        'textAlign': 'center',
        'color': colors['background']
    })
        ),

#1er graph fichier 2
    dcc.Graph(
        id='example-graph-4',
        figure=fig4
        
        ),   
#text
    html.Div(children=[
        
        dcc.Markdown(
                       '''### Interprétation des Résultats (fichier 1)
            
            1. Le graphique
             si dessus nous montre que les émotions les plus représentées sont 'happy' et 'sadness'.

            2. Le graphique de répartition du vocabulaire  nous montre que les mots les plus présent dans le corpus sont 'feel, feeling' et 'like'. '''
     )]),

    html.Br(),

#titre 2nd graph fichier 1
    html.Div(style={'backgroundColor': colors['blanc']}, 
             children=html.Div(
             'Histogramme de la répartition du vocabulaire fichier 1',
         style={
        'textAlign': 'center',
        'color': colors['background']
    })
        ),

#2nd graph fichier 1
    dcc.Graph(
        id='example-graph-3',
        figure=fig2
        
        ),

    html.Br(),

#titre 2nd graph fichier 2
    html.Div(style={'backgroundColor': colors['blanc']}, 
             children=html.Div(
             'Histogramme de la répartition du vocabulaire fichier 2',
         style={
        'textAlign': 'center',
        'color': colors['background']
    })
        ),

#2nd graph fichier 2
    dcc.Graph(
        id='example-graph-9',
        figure=fig9
        
        ),

#text
    html.Div(children=[
        
        dcc.Markdown(
                       '''### Interprétation des Résultats (fichier 2)
            
            1. Le graphique si dessus nous montre que les émotions les plus représentées sont 'worry' et 'neutral'.

            2. Le graphique de répartition du vocabulaire  nous montre que les mots les plus présent dans le corpus sont 'blinky' et 'bliss'. '''
     )]),



    ])



@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
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
        ])
    elif tab == 'tab-2':
        return html.Div([
            dash_table.DataTable(
            data=df4.to_dict('records'),
            export_format='csv',
            columns=[{'id': c, 'name': c} for c in df4.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'height': 'auto',
                'width': 'auto',
                'whiteSpace': 'normal',
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white'
                }
            )
        ])