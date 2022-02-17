import pandas as pd
import altair as alt

import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import dash_alternative_viz as dav
from dash.dependencies import Input, Output

import sys
sys.path.append("./app")
from layout import *
from plot import *

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP, '/css/button.css'])

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    content 
])

# @app.callback(
#     Output(component_id='f21', component_property='spec'),
#     Output(component_id='f22', component_property='spec'),
#     [Input('url', 'pathname')]
# )
# def plot_21_22(pathname):
#     return html.Div([
#         html.H3('You are on page {}'.format(pathname))
#     ])

@app.callback(
    Output(component_id='f11', component_property='spec'),
    [Input('xslider_1', 'value')]
)
def update(xmax):
    return plot_11(xmax)


@app.callback(
    Output(component_id='f12', component_property='spec'),
    [Input('xslider_2', 'value')]
)
def update(xmax):
    return plot_12(xmax)

@app.callback(
    Output(component_id='f21', component_property='spec'),
    [Input('select-country', 'value')]
)
def update(xmax):
    return plot_21(xmax)


if __name__ == '__main__':
    app.run_server(debug=True)