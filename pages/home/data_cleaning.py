#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Claire BUTAYE
"""

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input, callback


# ---- Styles ----------------------------------------------------------------

row_style = {'marginTop': '1%',
             'backgroundColor':'lightgrey'}

card_style = {'height':'100%'}

light_title = {'fontSize':'30px',
               'fontWeight':'lighter'}

link_style = {'color':'black',
              'opacity':'50%',
              'backgroundColor':'f8f9fa',
              'textDecoration':'none',
              'fontSize':'15px'}

# ---- Tabs' content ---------------------------------------------------------

# The first tab contains the explaination behind the filtering
tab1_content = html.Div([ html.H2("Data Filtering",
                                  style = light_title),

                          html.Hr(),
                          html.H6('''
                                  The data was downloaded under the xlsx or csv format,
                                  and the headers wree removed.

                                  The raw data has to be filtered for the map creation (accordingly to the
                                  following script) to only keep the rows
                                  corresponding to both genders and all age categories.
                                  The resulting csv files are in the directory asset/filtered_data.''')
        ])

# The second tab contains the exact code used to filter the data
tab2_content = html.Div([ html.H2("Source code",
                                  style = light_title),

                         html.Hr(),

                         dcc.Markdown('''

                            ```python

                            # Importation of the raw data
                            df = pd.read_csv('./assets/data/full_data/all_causes.csv')

                            # Filtering
                            df = df[df['Sex']=='All']
                            df = df[df['Age group code']=='Age_all']

                            # Writing the filtered data in new csv
                            from pathlib import Path

                            filepath = Path('./assets/filtered_data/all_causes_filtered.csv')
                            filepath.parent.mkdir(parents=True, exist_ok=True)
                            df.to_csv(filepath, index = False)

                             ```
                             ''',
                              style = {'border':'1px',
                                       'borderColor':'black'})])

# The third tab contains the links to the raw data
tab3_content = html.Div([

    html.H2("Raw data",
            style = light_title),

    html.Hr(),

    dcc.Link(href = 'https://platform.who.int/mortality',
             children = 'Link to the Mortality Database',
             style = link_style)

    ])

# ---- Script of the page "Data cleaning" ------------------------------------

dash.register_page(__name__,
                   path = '/home/data_cleaning',
                   external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout composed of 3 tabs of text
layout = dbc.Container([
                    dbc.Row(dbc.Col([
                       dcc.Tabs(id="tabs",
                                value='tab-1',
                                children=[
                                           dcc.Tab(label='Data Filtering', value='tab-1'),
                                           dcc.Tab(label='Code', value='tab-2'),
                                           dcc.Tab(label='Raw data', value='tab-3')]),

                       html.Div(id='tabs-content',
                                style = {'backgroundColor':'white',
                                         'padding':'2rem 1rem'})], width = 12),
                        style = row_style)

    ], className  ='vh-100')


# ---- Callback to update the content of the tab dynamically -----------------

@callback(Output('tabs-content', 'children'),
          Input('tabs', 'value'))

def render_tabs(tab):
    if tab == "tab-1" :
        return tab1_content

    elif tab == "tab-2" :
        return tab2_content

    elif tab == "tab-3" :
        return tab3_content
