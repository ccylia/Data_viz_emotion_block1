#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from app import app
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import base64

df = pd.read_csv('/home/cecilia/Documents/brief/brief_dash_université/université_dash_l/timesData.csv') 


#chargement des images
image_filename = '/home/cecilia/Documents/brief/brief_emotions/emotion_dash/apps/#countvectorizer, tfidf, stopwords, lematization et stemization.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

image_filename1 = '/home/cecilia/Documents/brief/brief_emotions/emotion_dash/apps/#countvectorizer et stopwords.png'
encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())

image_filename2 = '/home/cecilia/Documents/brief/brief_emotions/emotion_dash/apps/#countvectorizer et le modèle.png'
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())

image_filename3 = '/home/cecilia/Documents/brief/brief_emotions/emotion_dash/apps/precision_recall.png'
encoded_image3 = base64.b64encode(open(image_filename3, 'rb').read())

image_filename4 = '/home/cecilia/Documents/brief/brief_emotions/emotion_dash/apps/roc.png'
encoded_image4 = base64.b64encode(open(image_filename4, 'rb').read())



##################################################################



##################################################################

#titre en tete
layout = html.Div(children=[
    html.Div(children=[
        html.H1(
            children='Résultats des classifieurs fichier 1',
            style={
                'textAlign': 'center',
                }
            )
        ]),
#titre 1er recap classifier
    html.Div(children=[
        html.H3(
            children='countvectorizer, tfidf, stopwords, lematization et stemization',
            style={
                'textAlign': 'center'
                #style="text-align: center"  textAlign
                }
            )
        ]),   

#1er recap classifier
    html.Div(children=[
        html.Img(style={'display':'block','margin':'auto'},
            src='data:image/png;base64,{}'.format(encoded_image.decode()),

            )


        ]),

#titre 2nd recap classifier
    html.Div(children=[
        html.H3(
            children='countvectorizer et stopwords',
            style={
                'textAlign': 'center',
                }
            )
        ]),   
#2nd recap classifier
    html.Div(children=[
        html.Img(style={'display':'block','margin':'auto'},
            src='data:image/png;base64,{}'.format(encoded_image1.decode()),
            
            )
        ]),


#titre 3ieme recap classifier
    html.Div(children=[
        html.H3(
            children='countvectorizer et le modèle',
            style={
                'textAlign': 'center',
                }
            )
        ]),   

#3ieme recap classifier
    html.Div(children=[
        html.Img(style={'display':'block','margin':'auto'},
            src='data:image/png;base64,{}'.format(encoded_image2.decode())
            )
        ]),   

#text
    html.Div(children=[
        
        dcc.Markdown(
                       '''### Interprétation des Résultats
           
            1. countvectorizer, tfidf, stopwords, lematization et stemization
               le f1 score qui tend le plus vers 1 est celui du svm lineaire en pondéré il est encore plus élévé ce qui nous montre qu une amelioration est possible.

            2. countvectorizer et le modèle
                le f1 score qui tend le plus vers 1 est celui du svm lineaire mais en ponderant le modèle logit devient plus performant.

            3. countvectorizer et stopwords
                les résultat sont identique à celui du dessus sauf pour le  'decision_tree' qui obtient une très légère difference en faveur du  précédent.
           
            
            '''
     )]),

#titre courbe precision et recall
    html.Div(children=[
        html.H3(
            children='Courbe Recall et Precision',
            style={
                'textAlign': 'center',
                }
            )
        ]),   

#photo courbe precicion et recall
    html.Div(children=[
        html.Img(style={'display':'block','margin':'auto'},
            src='data:image/png;base64,{}'.format(encoded_image3.decode())
            )
        ]),   

#titre courbe roc
    html.Div(children=[
        html.H3(
            children='Courbe Roc',
            style={
                'textAlign': 'center',
                }
            )
        ]),   

#photo courbe roc
      html.Div(children=[
        html.Img(style={'display':'block','margin':'auto'},
            src='data:image/png;base64,{}'.format(encoded_image4.decode())
            )
        ]),
#text
    html.Div(children=[
        
        dcc.Markdown(
                       '''### Interprétation des Résultats courbe roc et precision,recall pour le logit du 1er tableau des classifieurs.
            
            1.  roc: 
                le classificateur commence sa prédiction sans faut positif mais au fur et à mesure de l'entrainement du modèle la courbe tend vers du toujours  'positif'. 

            2. precision et recall:
                Le rappel est défini par le nombre d'émotions pertinentes retrouvées au regard du nombre d'émotions pertinentes que possède la base de données.

                La précision est le nombre d'émotions pertinentes retrouvées rapporté au nombre d'émotions total proposé pour une requête donnée.

                on constate que les courbes tendent vers (1,1) avec une certaines difficulté pour la 'surprise'.

            
            '''
     )])


    #dcc.Graph(
     #   id='example-graph-3',
      #  figure=fig
       # )

    ])




