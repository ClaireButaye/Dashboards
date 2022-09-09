#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Claire BUTAYE
"""

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State
import base64

# ---- Styles ----------------------------------------------------------------

link_style = {'color':'black',
              'opacity':'50%',
              'backgroundColor':'f8f9fa',
              'textDecoration':'none',
              'fontSize':'15px'}

sidebar_style = {'marginTop':10,
                 'bottom':'5%',
                 'left':0,
                 'right':0,
                 'padding':'2rem 1rem',
                 'backgroundColor':'#f8f9fa'}

light_title = {'fontSize':'30px',
               'fontWeight':'lighter'}

# ---- Variables for layout --------------------------------------------------

light_logo=True

sidebar = html.Div( children = [dcc.Location(id='url', refresh=False),

                                html.H2("Sidebar",
                                        style = light_title) ,

                                html.Hr(),


                                html.H6("Informations about the data and its processing",
                                        style = {'fontSize':'12px'}),

                                dcc.Link(id = 'link_who',
                                         href = "/",
                                         children = "WHO",
                                         style = link_style),
                                html.Br(),
                                dcc.Link(id = 'link_dq',
                                         href = "/home/data_quality",
                                         children = "Data quality",
                                         style = link_style),
                                html.Br(),
                                dcc.Link(id = 'link_dc',
                                         href = "/home/data_cleaning",
                                         children = "Data cleaning",
                                         style = link_style),
                                html.Br(),
                                html.Hr(),
                                html.H6("Visualization",
                                        style = {'fontSize':'12px'}),
                                dcc.Link(id = 'link_map',
                                         href = "/visualization/map",
                                         children = "Worldwide Map",
                                         style = link_style),
                                html.Br(),
                                dcc.Link(id = 'link_graphs',
                                         href = "/visualization/graphs",
                                         children = "Graphs",
                                         style = link_style),
                                html.Br(),
                                ],

                                style = sidebar_style)


header = dbc.Row ( children = [

                                dbc.Col(html.H2("Worldwide Mortality Dashboard",
                                                style = {'color' : 'white',
                                                         'padding':'2vh'}),
                                        width = 9),



                                dbc.Col(html.A(id='gh-link',
                                               children=['View on GitHub'],
                                               href="https://github.com/ClaireButaye/Dashboards/tree/main/Mortality",
                                               style={'color': 'white' if light_logo else 'black',
                                                      'text-decoration':'none'}
                                               ),
                                        width = 2,
                                        style = {'padding':'2vh',
                                                 'marginTop':'1.5vh',
                                                 'textAlign':'right'}),


                                dbc.Col(html.Img(src='data:image/png;base64,{}'.format(
                                                    base64.b64encode(
                                                        open('./assets/GitHub-Mark-{}64px.png'.format(
                                                                'Light-' if light_logo else ''),
                                                            'rb').read()).decode())),
                                        width = 1,
                                        style = {'padding' : '1vh'}),

                            ])


# ---- Main script of the application ----------------------------------------

app = dash.Dash (__name__ ,
                 use_pages=(True),
                 external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.config.suppress_callback_exceptions=True # Necessary to run the graphs.py without an uncessary warning


# layout composed of 3 main elements : the header, the sidebar to navigate
# through the pages, and the pages content.
app.layout = dbc.Container ( children = [

    dbc.Row (header,
             style = {'backgroundColor' : 'black',
                      'height' : '10%'}),

    dbc.Row([
            dbc.Col (sidebar, width = 2, style = {'backgroundColor' : 'lightgrey'}),
            dbc.Col (dash.page_container, width = 10)
            ])

    ],
    style = {'backgroundColor' : 'lightgrey'},
    fluid = True)


# ---- Callbacks to highlight the current page in the sidebar ----------------

@app.callback(
    Output(component_id='link_who', component_property="style"),
    Input(component_id='url', component_property='pathname')
)


def bold_if_currently_who_page(pathname):
    if pathname == '/':
        return {'color':'black',
              'opacity':'50%',
              'backgroundColor':'f8f9fa',
              'textDecoration':'none',
              'fontSize':'15px',
              'font-weight': 'bold'}
    else : return link_style

@app.callback(
    Output(component_id='link_dq', component_property="style"),
    Input(component_id='url', component_property='pathname')
)


def bold_if_currently_dq_page(pathname):
    if pathname == '/home/data_quality':
        return {'color':'black',
              'opacity':'50%',
              'backgroundColor':'f8f9fa',
              'textDecoration':'none',
              'fontSize':'15px',
              'font-weight': 'bold'}
    else : return link_style

@app.callback(
    Output(component_id='link_dc', component_property="style"),
    Input(component_id='url', component_property='pathname')
)


def bold_if_currently_dc_page(pathname):
    if pathname == '/home/data_cleaning':
        return {'color':'black',
              'opacity':'50%',
              'backgroundColor':'f8f9fa',
              'textDecoration':'none',
              'fontSize':'15px',
              'font-weight': 'bold'}
    else : return link_style

@app.callback(
    Output(component_id='link_graphs', component_property="style"),
    Input(component_id='url', component_property='pathname')
)


def bold_if_currently_ds_page(pathname):
    if pathname == '/visualization/graphs':
        return {'color':'black',
              'opacity':'50%',
              'backgroundColor':'f8f9fa',
              'textDecoration':'none',
              'fontSize':'15px',
              'font-weight': 'bold'}
    else : return link_style

@app.callback(
    Output(component_id='link_map', component_property="style"),
    Input(component_id='url', component_property='pathname')
)


def bold_if_currently_ds_page(pathname):
    if pathname == '/visualization/map':
        return {'color':'black',
              'opacity':'50%',
              'backgroundColor':'f8f9fa',
              'textDecoration':'none',
              'fontSize':'15px',
              'font-weight': 'bold'}
    else : return link_style




if __name__ == '__main__' :
    app.run_server (debug = True)
