import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px


def graph_date(dates):
    with open('drought_data.pkl', 'rb') as pickle_in:
        dr_st = pickle.load(pickle_in)
    drought_y = dr_st[dr_st['ValidEnd']==dates]
    fig = px.choropleth(drought_y,locations='state',
                        locationmode='USA-states',
                        color='DSCI',hover_data=[ "avg_tmax",'avg_tmin', "total_avg_prcp_mm",'area_d0','area_d1','area_d2','area_d3','area_d4'],
                        title=f'National drought average {dates}',
                        labels={'DSCI':'DSCI rate'},
                        range_color=(0, 500),width=800, height=800,
                        scope='usa')
    fig.show()

st.title('Drought monitor')

st.write('Use the sidebar to select a page to view.')

page = st.sidebar.selectbox(
    'Pae',
    ('About','Map Drought')
)

if page == 'About':
    st.subheader('About this project')
    st.write('''
        A drought can be generally understood as "a period of abnormally dry weather that goes on for long enough to have an impact on water supplies, farming, livestock operations, energy production and other activities"(Fountain, 2021). Droughts begin with less than normal precipitation which varies depending on the region. At the root of droughts are warmer temperatures and changing precipitation patterns, which are linked to emissions of carbon dioxide and other greenhouse gases into the atmosphere, where they trap the sun's heat(Fountain,2021). Excessive heat from climate change leads to winter snowpack melting faster affecting the availability of water throughout the year(Fountain,2021).
    ''')


elif page == 'Map Drought':
    # header
    with open('drought_data.pkl', 'rb') as pickle_in:
        dr_st = pickle.load(pickle_in)

    st.subheader('Exploratory Data Analysis')
    option = st.selectbox(
     'What year would you like to select?',
     (2001, 2002, 2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021))
    if st.button('graphic'):
        with open('drought1.pkl', 'rb') as pickle_in:
            pipe = pickle.load(pickle_in)
        drought_y = pipe[pipe['ValidEnd']==option]
        fig = px.choropleth(drought_y,locations='state',
                        locationmode='USA-states',
                        color='DSCI',hover_data=[ "avg_tmax",'avg_tmin', "total_avg_prcp_mm",'area_d0','area_d1','area_d2','area_d3','area_d4'],
                        title=f'National drought average {option}',
                        labels={'DSCI':'DSCI rate'},
                        range_color=(0, 500),width=800, height=800,
                        scope='usa')
        fig.show()
        #graph_years(option)

    option2 = st.selectbox(
     'What date would you like to select?',dr_st['ValidEnd'])
     
    if st.button('graphic2'):
        #st.subheader('Which date do you like to predict?')
        graph_date(option2)
    

    




