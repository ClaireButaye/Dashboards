#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Claire BUTAYE
"""
import pandas as pd
import dash 
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px

# ---- Styles ----------------------------------------------------------------

light_title = {'fontSize':'30px', 
               'fontWeight':'lighter'}

# ---- Data ------------------------------------------------------------------

# Importation of the raw data files
df = pd.read_csv('./assets/data/full_data/all_causes.csv')
df_comm = pd.read_csv('./assets/data/full_data/Communicable, maternal, perinatal and nutritional conditions_8th septembre 2022.csv',
                      index_col = False)
df_non_comm = pd.read_csv('./assets/data/full_data/Noncommunicable diseases_8th septembre 2022.csv', index_col = False)
df_inj = pd.read_csv('./assets/data/full_data/Injuries_8th septembre 2022.csv', index_col = False)
df_unknown = pd.read_csv('./assets/data/full_data/Ill-defined diseases_8th septembre 2022.csv', index_col = False)


# ---- Variables linked to the data  -----------------------------------------

# List of the region names
list_RN = df ['Region Name'].unique().tolist()
list_RN.append('World')

# List of the country names
list_CN = df ['Country Name'].unique().tolist()
list_CN.append('All')

# List of the age groups
list_age_groups = df ['Age Group'].unique().tolist()

# List of the major cause categories for the dropdown
list_causes = ['All causes', 
               'Communicable, maternal, perinatal and nutritional conditions',
               'Noncommunicable diseases',
               'Injuries',
               'Ill-defined diseases']

# Dictionnary allowing us to select the good dataframe according to the cause selected
dict_causes = {'All causes': df, 
               'Communicable, maternal, perinatal and nutritional conditions':df_comm,
               'Noncommunicable diseases':df_non_comm,
               'Injuries':df_inj,
               'Ill-defined diseases':df_unknown}


# ---- Tab's content and associated control panels  --------------------------

tab1_content =  dcc.Graph(id = 'graph_line_causes_age')

tab2_content= dcc.Graph(id = 'graph_line_causes_years')


controllers1 = children = [html.H2('Control', 
                                    style = light_title),
                    
                            html.Hr(),
                            html.Label('World Regions'),
                            dcc.Dropdown(id = 'dropdown_region',
                                          options=[{'label': x, 'value': x} for x in list_RN],
                                          value = 'World'),
                            html.Br(),
                            html.Label('Countries'),
                            dcc.Dropdown (
                                
                                id = 'dropdown_country',
                                options =[{'label': x, 'value': x} for x in list_CN],
                                value = 'All',
                                
                                style = {'marginTop':'1%'}
                                
                                
                            ),
                            html.Br(),
                            html.Label('Genders'),
                            dcc.Dropdown (
                                
                                id = 'dropdown_gender',
                                options =[{'label': 'Male', 'value': 'Male'},
                                          {'label': 'Female', 'value': 'Female'},
                                          {'label': 'All', 'value': 'All'}],
                                value = 'All',
                                
                                style = {'marginTop':'1%'}
                            ),
                            html.Br(),
                            html.Label('Death causes'),
                            dcc.Dropdown(id = 'dropdown_causes',
                                         options=[{'label': x, 'value': x} for x in list_causes],
                                         value = 'All causes',
                                
                                        style = {'marginTop':'1%'}),
                             html.Br(),
                             html.Label('Years'),
                             dcc.Slider(
                    
                                    min = min(df['Year']),
                                    max = max(df['Year']),
                                    value = min(df['Year']),
                                    step = 1,
                                  
                                    tooltip = { 'always_visible': True },
                                    marks = {min(df['Year']):str(min(df['Year'])), 
                                             max(df['Year']):str(max(df['Year']))},
                                    id = 'slider_years',
                                    updatemode = 'drag')]
                          
controllers2 = children = [html.H2('Control', 
                                    style = light_title),
                    
                            html.Hr(),
                            html.Br(),
                            html.Label('World Regions'),
                            dcc.Dropdown(id = 'dropdown_region',
                                          options=[{'label': x, 'value': x} for x in list_RN],
                                          value = 'World'),
                            
                            html.Br(),
                            html.Label('Countries'),
                            dcc.Dropdown (
                                
                                id = 'dropdown_country',
                                options =[{'label': x, 'value': x} for x in list_CN],
                                value = 'All',
                                
                                style = {'marginTop':'1%'}
                                
                                
                            ),
                            
                            html.Br(),
                            html.Label('Genders'),
                            dcc.Dropdown (
                                
                                id = 'dropdown_gender',
                                options =[{'label': 'Male', 'value': 'Male'},
                                          {'label': 'Female', 'value': 'Female'},
                                          {'label': 'All', 'value': 'All'}],
                                value = 'All',
                                
                                style = {'marginTop':'1%'}
                            ),
                            
                            html.Br(),
                            html.Label('Death causes'),
                            dcc.Dropdown(id = 'dropdown_causes',
                                         options=[{'label': x, 'value': x} for x in list_causes],
                                         value = 'All causes',
                                
                                        style = {'marginTop':'1%'}),
                            
                            html.Br(),
                            html.Label('Age Groups'),
                             dcc.Dropdown(id = 'dropdown_age',
                                             options=[{'label': x, 'value': x} for x in list_age_groups],
                                             value = '[All]',
                                    
                                            style = {'marginTop':'1%'})]

            
# ---- Script of the page "Graphs" -------------------------------------------

dash.register_page(__name__,
                   path = '/visualization/graphs')

# Layout composed of two type of graphs controlled by panels (dropdowns, slider)
layout = dbc.Container([
    
    dbc.Row([
        
        # Control panels
        dbc.Col (id = 'controllers', 
                 width = 3,
                 style = {'backgroundColor':'white',
                                      'padding':'2rem 1rem',
                                      'marginTop':'1%',
                                      'marginBottom':'2%',
                                      'marginRight':'2%',
                                      'alignText':'left',
                                      'height':'50%'}),

    
    
       # Graphs tabs
        dbc.Col([   dcc.Tabs(id="tabs_line", 
                             value='tab-1', 
                             children=[dcc.Tab(label='Graph age', value='tab-1'),
                                        dcc.Tab(label='Graph years', value='tab-2')]),
                                           
                     html.Div(id='tabs-content_line',
                              style = {'backgroundColor':'white',
                                        'padding':'2rem 1rem'})
                       
                      
        
        ], width = 8,
           style = {'backgroundColor':'white',
                    'padding':'1rem 1rem',
                    'marginTop':'1%',
                     'alignText':'right'}),

    ], style={'backgroundColor':'lightgrey'})
    
    
    
    ], className = 'vh-100')



# ---- Callbacks to update the content the control panel dynamically ---------

# Limit the country options to the one contanied in the selected region
@callback(Output('dropdown_country', 'options'),
          Input('dropdown_region', 'value'))

def change_country_options(region_name):
    df_ = dict_causes['All causes']
    
    if region_name != 'World':
        df_ = df_ [df_ ['Region Name']==region_name]
        
    list_CN = df_ ['Country Name'].unique().tolist()
    list_CN.append('All')
    return [{'label': x, 'value': x} for x in list_CN]


# Each country shared its data for different years
# we update the years slider to only have years where data is present
@callback(Output('slider_years', 'min'),
          Output('slider_years', 'max'),
          Output('slider_years', 'marks'),
          Input('dropdown_region', 'value'),
          Input('dropdown_country', 'value'))

def change_slider_range(region_name, country_name):
    df = dict_causes['All causes']
    if region_name != 'World':
        df = df[df['Region Name']==region_name]
    if country_name != 'All':
        df = df [df['Country Name']==country_name]
    return min(df['Year']), max(df['Year']), {min(df['Year']):str(min(df['Year'])), max(df['Year']):str(max(df['Year']))}




# ---- Callback to update the content of the tab dynamically -----------------

@callback(Output('tabs-content_line', 'children'),
          Output('controllers', 'children'),
          Input('tabs_line', 'value'))

def render_tabs(tab):
    if tab == "tab-1" :
        return tab1_content, controllers1
    
    elif tab == "tab-2" :
        return tab2_content, controllers2
    
    
# ---- Callback to update the graphs depending on the options chosen ---------


# First graph, DR in function of age group
@callback(
   Output('graph_line_causes_age', 'figure'),
   Input('dropdown_region', 'value'),
   Input('dropdown_country', 'value'),
   Input('dropdown_gender', 'value'),
   Input('dropdown_causes', 'value'),
   Input('slider_years', 'value') 
   )

def tab1_graph(region, country, gender, causes, year):
    df = dict_causes[causes]
    df = df [df ['Sex']==gender]
    df = df [df ['Year']==year]
    df = df [df ['Age Group']!= '[Unknown]']
    df = df [df ['Age Group']!= '[All]']
    
    if country != 'All':
        df = df [df ['Country Name']==country]
        
    elif country == 'All' and region != 'World' :
        df = df [df ['Region Name']==region]
        df.groupby('Age Group').mean()
        
    
    df  = df .sort_values(by = ['Age group code'], ascending = True)
    
    figure = px.line(df, 
                     x="Age Group", 
                     y="Death rate per 100 000 population", 
                     color = 'Region Name',
                     title='Death rate per 100 000 population depending of the age group')

    return figure

# Second graph, DR in function of years
@callback(
   Output('graph_line_causes_years', 'figure'),
   Input('dropdown_region', 'value'),
   Input('dropdown_country', 'value'),
   Input('dropdown_gender', 'value'),
   Input('dropdown_causes', 'value'),
   Input('dropdown_age', 'value') 
   )

def tab2_graph(region, country, gender, causes, age):
    df = dict_causes[causes]
    df = df [df ['Sex']==gender]
    df = df [df ['Age Group']!= '[Unknown]']
    df = df [df ['Age Group']== age]
    
    if country != 'All':
        df = df [df ['Country Name']==country]
        
    elif country == 'All' and region != 'World' :
        df = df [df ['Region Name']==region]
        df.groupby('Age Group').mean()
        
    
    
    figure = px.line(df, 
                     x="Year", 
                     y="Death rate per 100 000 population", 
                     color = 'Region Name',
                     title='Death rate per 100 000 population through the years')
    return figure