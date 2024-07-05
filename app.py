import json
import player
import overall
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")
st.sidebar.title('IPL Data Analysis')
option = st.sidebar.selectbox('Select', ['overall', 'player', 'team'])

if option == 'overall':
    col = st.columns(3)
    season = col[0].selectbox('Season', ['Season', 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008])
    team = col[1].selectbox('Team', ['Team', 'Chennai super kings', 'Deccan chargers', 'Delhi capitals', 'Gujarat lions', 'Gujarat titans', 'Kochi tuskers kerala', 'Kolkata knight riders', 'Lucknow super giants', 'Mumbai indians', 'Pune warriors', 'Punjab kings', 'Rajasthan royals', 'Rising pune supergiant', 'Royal Challengers Bengaluru', 'Sunrisers hyderabad'])
    type = col[2].selectbox('Type', ['Batsman', 'Bowler'])
    btn = st.button('Search', use_container_width=True)
    
    if btn:
        if type == 'Batsman':
            df = overall.batsman_data(season=season, team=team)
        else:
            df = overall.bowler_data(season=season, team=team)
        
        st.dataframe(df, use_container_width=True, hide_index=True)
        
elif option == 'player':
    player_name = st.sidebar.selectbox('Player', np.sort(player.player_names()))
    btn = st.sidebar.button('Search', use_container_width=True)
    
    if btn:
        try:
            info = player.player_basic_info(player_name)
            player_df = player.player_batting_performance(player_name)
            st.header(player_name.capitalize())
            st.divider()
            col1, col2 = st.columns(2)
            with col1:
                st.metric('Matches played', info['matches'])
            with col2:
                st.metric('Type', info['type'].capitalize())
            
            col3, col4 = st.columns(2)
            with col3:
                st.metric('Nationality', info['national'].capitalize())
            # with col4:
            #     st.metric('Wickets', 100)
                
            st.divider()
            st.write('#### Batting Performance')
            st.dataframe(player.player_batting_performance(player_name), use_container_width=True, hide_index=True)
            
            col4, col5= st.columns(2)
            
            with col4:

                if not player_df.empty:
                    # Create the plot
                    fig, ax = plt.subplots()
                    ax.plot(player_df['Season'], player_df['Runs'], marker='o')
                    ax.set_xlabel('Season')
                    ax.set_ylabel('Runs')
                    # ax.set_title(f'Runs per Season for {player_name}')
                    ax.legend()
                    ax.grid(True)

                # Display the plot in Streamlit
                    st.pyplot(fig)
                else:
                    st.write(f"No data found for player {player_name}")
            with col5:
                fig, ax = plt.subplots()
                ax.plot(player_df['Season'], player_df['SR'], marker='o')
                ax.set_xlabel('Season')
                ax.set_ylabel('Strike rate')
                # ax.set_title(f'Runs per Season for {player_name}')
                ax.legend()
                ax.grid(True)

                # Display the plot in Streamlit
                st.pyplot(fig)
            col6, col7 = st.columns(2)
            with col6:
                fig, ax = plt.subplots()
                ax.plot(player_df['Season'], player_df['Avg'], marker='o')
                ax.set_xlabel('Season')
                ax.set_ylabel('Average')
                # ax.set_title(f'Runs per Season for {player_name}')
                ax.legend()
                ax.grid(True)

                # Display the plot in Streamlit
                st.pyplot(fig)
            with col7:
                fig, ax = plt.subplots()
                ax.plot(player_df['Season'], player_df['Matches'], marker='o')
                ax.set_xlabel('Season')
                ax.set_ylabel('Matches played')
                # ax.set_title(f'Runs per Season for {player_name}')
                ax.legend()
                ax.grid(True)

                # Display the plot in Streamlit
                st.pyplot(fig)
                
            st.divider()
            st.write('#### Bowling performance')
            player_bowling_data = player.player_bowling_performance(player_name)
            
            if not player_bowling_data.empty:
                st.dataframe(player_bowling_data, use_container_width=True, hide_index=True)
                
                col8, col9 = st.columns(2)
                
                with col8:
                    fig, ax = plt.subplots()
                    ax.plot(player_bowling_data['Season'], player_bowling_data['Overs'], marker='o')
                    ax.set_xlabel('Season')
                    ax.set_ylabel('Overs bowled')
                    # ax.set_title(f'Runs per Season for {player_name}')
                    ax.legend()
                    ax.grid(True)

                    # Display the plot in Streamlit
                    st.pyplot(fig)
                    
                with col9:
                    fig, ax = plt.subplots()
                    ax.plot(player_bowling_data['Season'], player_bowling_data['Runs'], marker='o')
                    ax.set_xlabel('Season')
                    ax.set_ylabel('Runs Conceded')
                    # ax.set_title(f'Runs per Season for {player_name}')
                    ax.legend()
                    ax.grid(True)

                    # Display the plot in Streamlit
                    st.pyplot(fig)
            else:
                st.write('##### No data')
            
                
        except Exception as e:
            st.error(e)
 
 
 
 
 
 
        
else:
    team_name = st.sidebar.selectbox('Team', ['CSK', 'MI', 'RCB', 'KKR', 'RR', 'KXIP', 'SRH', 'DC', 'PWI', 'GL', 'RPS', 'KTK', 'DD'])
    btn = st.sidebar.button('Search')
    
    if btn:
        st.title(team_name)
        # Add logic here to display team-specific data
