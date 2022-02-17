import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import dash_alternative_viz as dav
from dash.dependencies import Input, Output

from plot import *

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

country_names = data["Country"].unique()
country_names.sort()


sidebar = html.Div(
    [
        html.Img(src="./assets/mds-hex-sticker-small.png", height="15%", style={"display":"block", "margin":"0 auto"}),
        # html.H1("UBC-MDS", className="display-1", style={'font-size':'25px', 'textAlign':'center'}),
        html.H1("Our Project Title", className="display-1", style={'font-size':'28px', 'textAlign':'center'}),
        html.Hr(),
        html.P(
            "Add some description, \r\nData Science Salaries Dashboard: This is the viz project of group 19", className="lead", 
            style={'font-size':'15px', 'textAlign':'center'}
        ),
        dbc.Nav(
            [
                dbc.NavLink("Page1", href="/", active="exact"),  ##exact mean when url is equal to href, then it is active
            ],
            vertical=True,
            pills=True,
        ),
        html.P(
            "Do we need add interaction here?", className="lead", style={'font-size':'15px', 'textAlign':'center'}
        ),
    ],
    style=SIDEBAR_STYLE,
)


content = dbc.Row(
    [
     dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        # dbc.CardHeader(id="h21", style={'font-size':'15px', 'textAlign':'left'}),
                        dcc.RangeSlider(id='xslider_1', min=0, max=2500000, value=[0, 2500000],
                                        marks={i: str(i) for i in range(0, 2_500_000, 400_000)}),
                        dbc.CardBody(dav.VegaLite(id="f11"))], style={'height':'45vh', 'overflow-x': 'scroll'})

                    ], width=6),
                
                dbc.Col([
                    dbc.Card([
                        # dbc.CardHeader(id="h22", style={'font-size':'15px', 'textAlign':'left'}),
                        dcc.RangeSlider(id='xslider_2', min=0, max=2500000, value=[0, 2500000],
                                        marks={i: str(i) for i in range(0, 2_500_000, 400_000)}),
                        dbc.CardBody(dav.VegaLite(id="f12")),
                    ], style={'height':'45vh', 'overflow-x': 'scroll'}), 
                ], width=6)
                ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        # dbc.CardHeader(id="h21", style={'font-size':'15px', 'textAlign':'left'}),
                        dcc.Dropdown(
                            id="select-country",
                            value="Canada",
                            options=[{"label": country, "value": country} for country in country_names]
                        ),
                        dbc.CardBody(dav.VegaLite(id="f21"))], style={'height':'45vh', 'overflow-x': 'scroll'})

                    ], width=6),
                
                dbc.Col([
                    dbc.Card([
                        # dbc.CardHeader(id="h22", style={'font-size':'15px', 'textAlign':'left'}),
                        dbc.CardBody(dav.VegaLite(id="f22", spec=plot_22())),
                    ], style={'height':'45vh', 'overflow-x': 'scroll'}), 
                ], width=6)
                ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        # dbc.CardHeader(id="h21", style={'font-size':'15px', 'textAlign':'left'}),
                        dbc.CardBody(dav.VegaLite(id="f31"))], style={'height':'31vh', 'overflow-x': 'scroll'})

                    ], width=6),
                
                dbc.Col([
                    dbc.Card([
                        # dbc.CardHeader(id="h22", style={'font-size':'15px', 'textAlign':'left'}),
                        dbc.CardBody(dav.VegaLite(id="f32")),
                    ], style={'height':'31vh', 'overflow-x': 'scroll'}), 
                ], width=6)
                ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        # dbc.CardHeader(id="h21", style={'font-size':'15px', 'textAlign':'left'}),
                        dbc.CardBody(dav.VegaLite(id="f41"))], style={'height':'31vh', 'overflow-x': 'scroll'})

                    ], width=6),
                
                dbc.Col([
                    dbc.Card([
                        # dbc.CardHeader(id="h22", style={'font-size':'15px', 'textAlign':'left'}),
                        dbc.CardBody(dav.VegaLite(id="f42")),
                    ], style={'height':'31vh', 'overflow-x': 'scroll'}), 
                ], width=6)
                ]),
     ])   
    ], style=CONTENT_STYLE)