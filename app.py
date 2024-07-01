import json
import overall
import numpy as np
import pandas as pd
import streamlit as st

st.sidebar.title('Menu')
option = st.sidebar.selectbox('Select', ['overall', 'player', 'team'])

if option == 'overall':
    # st.subheader('Overall IPL records')
    col = st.columns(3)
    season = col[0].selectbox('', ['Season', 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008])
    team = col[1].selectbox('', ['Team', 'Chennai super kings','Deccan chargers','Delhi capitals','Gujarat lions','Gujarat titans','Kochi tuskers kerala','Kolkata knight riders','Lucknow super giants','Mumbai indians','Pune warriors','Punjab kings','Rajasthan royals','Rising pune supergiant','Royal Challengers Bengaluru','Sunrisers hyderabad'])
    type = col[2].selectbox('', ['Batsman', 'bowler'])
    btn = st.button('Search', use_container_width=True)
    
    if btn:
        if type == 'Batsman':
            df = overall.batsman_data(season=season, team=team)
        else:
            df = overall.bowler_data(season=season, team=team)
        
            
        st.dataframe(df, use_container_width=True)
        
elif option == 'player':
    player_name = st.sidebar.selectbox('Player', ['Virat Kohli', 'MS Dhoni'])
    btn = st.sidebar.button('Search')
    
    if btn:
        st.title(player_name)
        # Add logic here to display player-specific data
        
else:
    team_name = st.sidebar.selectbox('Team', ['CSK', 'MI', 'RCB', 'KKR', 'RR', 'KXIP', 'SRH', 'DC', 'PWI', 'GL', 'RPS', 'KTK', 'DD'])
    btn = st.sidebar.button('Search')
    
    if btn:
        st.title(team_name)
        # Add logic here to display team-specific data
