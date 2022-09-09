#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Claire BUTAYE
"""
import dash 
import dash_bootstrap_components as dbc
from dash import html

# ---- Styles ----------------------------------------------------------------

row_style = {'marginTop': '1%',
             'backgroundColor':'lightgrey'}

card_style = {'height':'100%'}

# ---- Script of the page "Who" ----------------------------------------------

dash.register_page(__name__, 
                   path = '/', 
                   external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout composed of two rows of text and a link
layout = dbc.Container(children = [

    dbc.Row (id = 'topRow',
             children = [
                 dbc.Col (dbc.Card(
                                     dbc.CardBody([
                                         
                                         html.H2("World Health Organization (WHO)", 
                                                 style={'fontSize':'30px', 
                                                        'fontWeight':'lighter'}),
                                         html.Hr(),
                                                      
                                         html.H6('''
                    Founded in 1948, WHO is the United Nations agency that connects nations, 
                    partners and people to promote health, keep the world safe and serve the 
                    vulnerable – so everyone, everywhere can attain the highest level of health.
                    WHO leads global efforts to expand universal health coverage. They direct 
                    and coordinate the world’s response to health emergencies.
                        '''),
                        
                                         html.Br(),
                                        
                                         html.H6('''One prerequesite to these actions are the knowledge about
                                                what is happening around the world. For its achievement, The WHO agency requests 
                                                health related data from the participating nations, including mortality data.''')
                                                
                                        ]),
                                     color = 'white',
                                     style = card_style
                                     ),  
                         width = 12)
                 ],
             style = row_style),

    
    dbc.Row (id = 'middleRow',
             children = [
                 dbc.Col (dbc.Card(
                                     dbc.CardBody([
                                         
                                         html.H2("Mortality Database",
                                                 style={'fontSize':'30px', 
                                                        'fontWeight':'lighter'}),
                                         html.Hr(),
                                    
                                         html.H6('''The WHO Mortality Database is a compilation of mortality
                            data by country and area, year, sex, age and cause of death,
                            as transmitted annually by national authorities from their civil 
                            registration and vital statistics system. It comprises data 
                            since 1950 to date.''')]),
                            
                                     color = 'white',
                                     style = card_style
                                     ),  
                         width = 12)
                 ],
             style = row_style),
                                         
                                         
     dbc.Row (id = 'bottomRow',
             children = [
                 dbc.Col (dbc.Card(
                                     dbc.CardBody(
                                         
                                         [
                                             html.H2("Official website",
                                                   style={'fontSize':'30px', 
                                                          'fontWeight':'lighter'}),
                                    
                                             html.Hr(),
                                    
                                    
                                             html.A(href = 'https://www.who.int', 
                                                    children = ["World Health Organization official website"],
                                                    style={'fontSize':'20px',
                                                          'textDecoration':'none',
                                                          'color':'darkgrey'})
                                          ]
                                        ),
                                     color = 'white',
                                     style = {'height':'100%'}
                                     ),  
                         sm = 12,
                         md = 6),
                 
                 
                 ], style = row_style)
    
    
    ], className  ='vh-100')