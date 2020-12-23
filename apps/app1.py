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



#fichiers
emotion_f = pd.read_csv('/home/cecilia/Documents/brief/brief_emotions/emotion_dash/Emotion_final.csv')
df2 = emotion_f[:50]
emotion_t = pd.read_csv('/home/cecilia/Documents/brief/brief_emotions/emotion_dash/text_emotion.csv')
df4 = emotion_t[:50]
df_count_emotion = emotion_f.groupby(['Emotion']).size().reset_index(name='Count')
df = df_count_emotion



#definition des themes
colors = {
    'background': '#111111',#111111 fbf6f6  7FDBFF
    'text': '#fbf6f6'
}




#fig1
fig = px.histogram(df,x='Emotion', y= 'Count', labels={'x':'Emotions', 'y':'Nombre d\'apparition'})        
#, ascending = False) ##############################
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
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
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    
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

#1ere table
    html.Div([
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
#saut de ligne       
    html.Br(),

#2nd table
    html.Div([
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
        ]),

    html.Br(),
    html.Br(),


#Titre suite
    html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H2(
            children='Graphiques pour mise en évidence de corrélation',
            style={
                'textAlign': 'center',
                'color': colors['text']
                }
            )
        ]),

#titre 1er graph
    html.Div(style={'backgroundColor': colors['background']}, 
             children=html.Div(
             'Histogramme d\'apparition des émotions fichier 1',
         style={
        'textAlign': 'center',
        'color': colors['text']
    })
        ),

#1er graph
    dcc.Graph(
        id='example-graph-2',
        figure=fig
        
        ),
#text
    html.Div(children=[
        
        dcc.Markdown(
                       '''### Interprétation des Résultats (fichier 1)
            
            **1. l\'histogramme si dessus nous montre que l\'emotion la plus présente est 'happy' suivi de 'sadness'**

            **2. l'histogramme si dessous nous montre que les mots les plus présent dans le corpus est 'feel**'''
     )]),

#titre 2nd graph
html.Div(style={'backgroundColor': colors['background']}, 
             children=html.Div(
             'Histogramme de la répartition du vocabulaire',
         style={
        'textAlign': 'center',
        'color': colors['text']
    })
        ),

#2nd graph
    dcc.Graph(
        id='example-graph-3',
        figure=fig2
        
        )
    ])



