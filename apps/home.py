from app import app
import dash_table
import pandas as pd

import dash_core_components as dcc
import dash_html_components as html
import base64

#chargement image
image_filename5 = '/home/cecilia/Documents/brief/brief_emotions/emotion_dash/apps/ms-icon.png'
encoded_image5 = base64.b64encode(open(image_filename5, 'rb').read())



layout = html.Div(children=[
    html.Div(children=[
        html.H1(
            children='Roue des Emotions',
            style={
                'textAlign': 'center',
                'color' : '#7FDBFF'
                }
            )
        ]),

#image de la roue
    html.Div(children=[
        html.Img(style={'display':'block','margin':'auto','height':'400px','border-radius':'50%'},
            src='data:image/png;base64,{}'.format(encoded_image5.decode())
            )
        ]),

#text
    html.Div(children=[
        
        dcc.Markdown(
         '''Depuis quelques années, les dispositifs de communication médiatisée par ordinateur (CMO) sont massivement utilisés, aussi bien dans les activités professionnelles que personnelles. Ces dispositifs permettent à des participants distants physiquement de communiquer. La plupart implique une communication écrite médiatisée par ordinateur (CEMO) : forums de discussion, courrier électronique, messagerie instantanée. Les participants ne s’entendent pas et ne se voient pas mais peuvent communiquer par l’envoi de messages écrits, qui combinent, généralement, certaines caractéristiques des registres écrit et oral (Marcoccia, 2000a ; Marcoccia, Gauducheau, 2007 ; Riva, 2001).

Imaginez que vous souhaitez savoir ce qui se passe derrière votre écran d'ordinateur, quels sont vos contacts les plus actifs et quelle est leur personnalité (pas banal comme question !!). Vous allez alors vous lancer dans l’analyse de leur narration et tenter d’extraire quelle émotion se dégage de chacune des phrases.

Chez Simplon nous utilisons tous les jours des outils de discussion textuels et nous construisons nos relations sociales et professionnelles autour de ces dispositifs. Pour entretenir des rapports sociaux stables, sereins, de confiance et efficaces, au travers des outils de communication écrites, lorsqu'il n'est pas possible d'avoir la visio (avec caméra), il est nécessaire de détecter des éléments "clés" dans les channels de discussions / mails qui nous permettront de déceler de la colère, de la frustration, de la tristesse ou encore de la joie de la part d'un collègue ou d'un amis pour adapter nos relations sociales. En tant qu'expert en data science, nous allons vous demander de développer un modèle de machine learning permettant de classer les phrases suivant l'émotion principale qui en ressort.



Dans l'objectif d'enrichir notre prédictions nous souhaitons augmenter notre jeux de donneés. Vous devrez donc travailler dans un deuxième temps avec le jeux de données fournie, issue de data.world afin de :

Comparez d'une part si les résultats de classification sur votre premier jeu de 
données sont similaires avec le second. Commenter.
Combiner les deux jeux de données pour tenter d'améliorer vos résultats de prédiction.
Prédire les nouvelles émotions présentes dans ce jeu de données sur les message du premier, et observer si les résultats sont pertinents.




**Vous devrez ensuite présenter vos résultats sous la forme d'un dashboard multi-pages Dash.**


**La première page du Dashboard sera dédiée à l'analyse et au traitement des données.**

 Vous pourrez par exemple présenter les données "brut" sous la forme d'un tableau puis les données pré-traitées dans le même tableau avec un bouton ou menu déroulant permettant de passer d'un type de données à un autre (n'afficher qu'un échantillon des résultats, on dans une fenêtre "scrollable"). Sur cette première page de dashboard seront accessibles vos graphiques ayant trait à votre première analyse de données (histogramme, bubble chart, scatterplot etc), notamment


    1-L'histogramme représentant la fréquence d’apparition des mots (commenter)
    2-L'histogramme des émotions (commenter)



**Une deuxième page du Dashboard sera dédiée aux résultats issues des classifications.**
    Il vous est demandé de comparer les résultats, d'au moins 5 classifiers, présentés
    dans un tableau permettant de visualiser vos mesures. Sur cette page de dashboard
    pourra se trouver par exemple, des courbes de rappel de précision (permette de
    tracer la précision et le rappel pour différents seuils de probabilité), un
    rapport de classification (un rapport de classification visuel qui affiche la
    precision, le recall, le f1-score, support, ou encore une matrice de confusion ou 
    encore une graphique permettant de visualiser les mots les plus représentatif 
    associé à chaque émotions. Héberger le dashboard sur le cloud de visualisation de 
    données Héroku.
    (https://www.heroku.com/)







''')])            








])