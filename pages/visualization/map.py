#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Claire BUTAYE
"""
import pandas as pd
import plotly.express as px

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output


# ---- Styles ----------------------------------------------------------------

row_style = {'marginTop': '1%',
             'backgroundColor':'lightgrey',}

# ---- Data ------------------------------------------------------------------

df_filtered  = pd.read_csv('./assets/data/filtered_data/all_causes_filtered.csv')
df_comm_filtered = pd.read_csv('./assets/data/filtered_data/Communicable, maternal, perinatal and nutritional conditions_filtered.csv',
                      index_col = False)
df_non_comm_filtered = pd.read_csv('./assets/data/filtered_data/Noncommunicable diseases_filtered.csv', index_col = False)
df_inj_filtered  = pd.read_csv('./assets/data/filtered_data/Injuries_filtered.csv', index_col = False)
df_unknown_filtered  = pd.read_csv('./assets/data/filtered_data/Ill-defined diseases_filtered.csv', index_col = False)

# List of the region names used for the dropdown
list_RN = df_filtered ['Region Name'].unique().tolist()
list_RN.append('World')

# List of the major cause categories for the dropdown
list_causes = ['All causes',
               'Communicable, maternal, perinatal and nutritional conditions',
               'Noncommunicable diseases',
               'Injuries',
               'Ill-defined diseases']

# Dictionnary allowing us to select the good dataframe according to the cause selected
dict_causes = {'All causes': df_filtered,
               'Communicable, maternal, perinatal and nutritional conditions':df_comm_filtered,
               'Noncommunicable diseases':df_non_comm_filtered,
               'Injuries':df_inj_filtered,
               'Ill-defined diseases':df_unknown_filtered}

# ---- Script of the page "World" ---------------------------------------------

dash.register_page(__name__,
                   path = '/visualization/map',
                   external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout constitued of two rows superposed,
#respectivelly with a dropdown and its associated map
layout = dbc.Container(

    [

     # Dropdown
      dbc.Row (id = 'topRow',
               children = [dbc.Col(
                                  dbc.Card(
                                           dbc.CardBody([dcc.Dropdown(id = 'animated_map_dropdown_regions',
                                                              options=[{'label': x, 'value': x} for x in list_RN],
                                                              value = 'World'),
                                                       html.Br(),
                                                       dcc.Dropdown(id = 'animated_map_dropdown_causes',
                                                              options=[{'label': x, 'value': x} for x in list_causes],
                                                              value = 'All causes')]),
                                           color = 'white'
                                          ),
                           width = 12)
                           ],
                style = row_style),

        # Map
        dbc.Row (id = 'bottomRow',
                 children = [dbc.Col
                                     (dbc.Card(
                                                dbc.CardBody(dcc.Graph(id = "Animated_map")),
                                                color = 'white'),
                                      width = 12)
                              ],
                              style = row_style)


    ],
    className  ='vh-100')


# ---- Callback to filter the map by world region, and causes ----------------

@callback(
    Output(component_id="Animated_map", component_property="figure"),
    [Input(component_id="animated_map_dropdown_regions",  component_property="value"),
     Input(component_id="animated_map_dropdown_causes",  component_property="value")]
)

def display_selected_region(region_name, causes):

    # Filtering by cause and determination of the according scale
    # (The scale varies a lot depending of the cause, a new min and max has to
    # be determined to see the differences beteween countries)
    df_filtered = dict_causes[causes]
    min_df = df_filtered ['Age-standardized death rate per 100 000 standard population'].min()
    max_df = df_filtered ['Age-standardized death rate per 100 000 standard population'].max()
    df_filtered  = df_filtered .sort_values(by = ['Year', 'Country Name'], ascending = True)


    # Filtering by region
    if region_name == 'World':
        fig_animated_map_mortality = px.choropleth(df_filtered,
                                                 locations="Country Code",
                                                 hover_name=("Country Name"),
                                                 color = 'Age-standardized death rate per 100 000 standard population',
                                                 color_continuous_scale = 'Reds',
                                                 animation_frame = 'Year',
                                                 range_color = (min_df, max_df)
                                                 )
        fig_animated_map_mortality.update_layout(title_text = "Mortality Rates reported to the WHO through the years")
        return fig_animated_map_mortality

    elif region_name == 'Europe':
         df_region = df_filtered [df_filtered ['Region Name']==region_name]
         fig_animated_map_mortality = px.choropleth(df_filtered,
                                                    scope = 'europe',
                                                 locations="Country Code",
                                                 hover_name=("Country Name"),
                                                 color = 'Age-standardized death rate per 100 000 standard population',
                                                 color_continuous_scale = 'Reds',
                                                 animation_frame = 'Year',
                                                 range_color = (min_df, max_df)
                                                 )
         fig_animated_map_mortality.update_layout(title_text = "Mortality Rates reported to the WHO through the years")
         return fig_animated_map_mortality

    elif region_name == 'Asia':
        df_region = df_filtered [df_filtered ['Region Name']==region_name]
        fig_animated_map_mortality = px.choropleth(df_region,
                                                 scope = 'asia',
                                                 locations="Country Code",
                                                 hover_name=("Country Name"),
                                                 color = 'Age-standardized death rate per 100 000 standard population',
                                                 color_continuous_scale = 'Reds',
                                                 animation_frame = 'Year',
                                                 range_color = (min_df, max_df)
                                                 )
        fig_animated_map_mortality.update_layout(title_text = "Mortality Rates reported to the WHO through the years")
        return fig_animated_map_mortality

    elif region_name == 'Africa':
        df_region = df_filtered [df_filtered ['Region Name']==region_name]
        fig_animated_map_mortality = px.choropleth(df_region,
                                                 scope = 'africa',
                                                 locations="Country Code",
                                                 hover_name=("Country Name"),
                                                 color = 'Death rate per 100 000 population',
                                                 color_continuous_scale = 'Reds',
                                                 animation_frame = 'Year',
                                                 range_color = (min_df, max_df)
                                                 )
        fig_animated_map_mortality.update_layout(title_text = "Mortality Rates reported to the WHO through the years")
        return fig_animated_map_mortality

    elif region_name == 'Central and South America':
        df_region = df_filtered [df_filtered ['Region Name']==region_name]
        fig_animated_map_mortality = px.choropleth(df_region,
                                                 scope = 'south america',
                                                 locations="Country Code",
                                                 hover_name=("Country Name"),
                                                 color = 'Age-standardized death rate per 100 000 standard population',
                                                 color_continuous_scale = 'Reds',
                                                 animation_frame = 'Year',
                                                 range_color = (min_df, max_df)
                                                 )
        fig_animated_map_mortality.update_layout(title_text = "Mortality Rates reported to the WHO through the years")
        return fig_animated_map_mortality

    elif region_name == 'North America and the Caribbean':
        df_region = df_filtered [df_filtered ['Region Name']==region_name]
        fig_animated_map_mortality = px.choropleth(df_region,
                                                 scope = 'north america',
                                                 locations="Country Code",
                                                 hover_name=("Country Name"),
                                                 color = 'Age-standardized death rate per 100 000 standard population',
                                                 color_continuous_scale = 'Reds',
                                                 animation_frame = 'Year',
                                                 range_color = (min_df, max_df)
                                                 )
        fig_animated_map_mortality.update_layout(title_text = "Mortality Rates reported to the WHO through the years")
        return fig_animated_map_mortality

    elif region_name == 'Oceania':

        df_region = df_filtered [df_filtered ['Region Name']==region_name]
        fig_animated_map_mortality = px.choropleth(df_region,
                                                 locations="Country Code",
                                                 hover_name=("Country Name"),
                                                 color = 'Age-standardized death rate per 100 000 standard population',
                                                 color_continuous_scale = 'Reds',
                                                 animation_frame = 'Year',
                                                 range_color = (min_df, max_df)
                                                 )
        fig_animated_map_mortality.update_layout(title_text = "Mortality Rates reported to the WHO through the years")
        return fig_animated_map_mortality
