#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#page d'acceuil


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64

from app import app
from apps import app1, app2, home, test


colors = {
    'background': '#111111',#111111 fbf6f6  7FDBFF
    'text': '#ed16e6'
}









#liens vers les pages
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Link('Page d\'acceuil', href='/'),
    html.Br(),
    dcc.Link('Page 1', href='/apps/app1'),
    html.Br(),
    dcc.Link('Page 2', href='/apps/app2'),
    html.Br(),
    dcc.Link('test', href='/apps/test'),
    html.Br(),


    # content will be rendered in this element
    html.Div(id='page-content'),
    html.Div(children=[
        html.H1(
            children='',
            style={
                'textAlign': 'center',
                'color': colors['background']
                }
            )
        ])
    



        ])








@app.callback(Output('page-content',
              'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' :
        return home.layout
    elif pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/test':
            return test.layout   
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)



