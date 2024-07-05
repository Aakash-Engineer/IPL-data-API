import numpy as np
import pandas as pd

def player_basic_info(name):
      
    balls = pd.read_csv('static/balls.csv')   
    player_df = balls[(balls['batter'] == name) | (balls['bowler'] == name) | (balls['non_striker'] == name)]
    
    player_matches = balls[(balls['batter'] == name) | (balls['bowler'] == name) | (balls['non_striker'] == name)]['id'].nunique()
    player_type = player_df['batter_type'].values[0]
    player_nation = player_df['nationality'].values[0]
    
    return {'matches': player_matches, 'type': player_type, 'national': player_nation}

def player_names():
    balls = pd.read_csv('static/balls.csv')
    
    return balls['batter'].unique()


# Player btting performance
def player_batting_performance(name):
    balls = pd.read_csv('static/balls.csv')
    player_df = balls[(balls['batter'] == name) | (balls['bowler'] == name) | (balls['non_striker'] == name)]
    season_group = player_df.groupby('season')
    temp_df = pd.DataFrame()
    
    for season, group in season_group:
        
        player_matches = group['id'].nunique()
        player_runs = balls[(balls['batter'] == name) & (balls['season'] == season)]['batsman_runs'].sum()
        
        if player_matches:   
            player_average = player_runs / player_matches
        else:
            player_average = 0
            
        player_balls_played = group[group['batter'] == name]['extras_type'].isna().sum()
        
        if player_balls_played:
            player_strike_rate = (player_runs / player_balls_played)*100
        else:
            player_strike_rate = 0
        
        player_100 = (group[group['batter'] == name].groupby('id')['batsman_runs'].sum().values >=100).sum() 
        player_50 = (group[group['batter'] == name].groupby('id')['batsman_runs'].sum().values >=50).sum() 
        player_6 = (group[group['batter'] == name]['batsman_runs'] == 6).sum()
        player_4 = (group[group['batter'] == name]['batsman_runs'] == 4).sum()
        
        temp_dict = {
            'Season': [season],
            'Matches': [player_matches], 
            'Runs': [player_runs], 
            'Avg' : [player_average],
            'SR': [player_strike_rate], 
            '100': [player_100], 
            '50': [player_50], 
            '4': [player_6], 
            '6':[player_6]
        }
        
        temp_df = pd.concat([temp_df, pd.DataFrame(temp_dict)], ignore_index=True)
#         print(temp_df)
    
    return temp_df
    
    

def player_bowling_performance(name):
    
    balls = pd.read_csv('static/balls.csv')
    player_df = balls[(balls['batter'] == name) | (balls['bowler'] == name) | (balls['non_striker'] == name)]
    season_group = player_df.groupby('season')
    temp_df = pd.DataFrame()
    
    for season, group in season_group:
        bowler_temp_df = group[group['bowler'] == name]
        player_matches = group['id'].nunique()
        player_deliveries = bowler_temp_df['extras_type'].isna().sum() + (bowler_temp_df['extras_type'] == 'legbyes').sum() + (bowler_temp_df['extras_type'] == 'byes').sum()
        player_overs = player_deliveries //6 if player_deliveries !=0 else np.nan 
        player_wickets = (bowler_temp_df['is_wicket'] == 1).sum()
        player_runs = bowler_temp_df[bowler_temp_df['extras_type'].isna()]['total_runs'].sum() + bowler_temp_df[(bowler_temp_df['extras_type'] == 'wides') | (bowler_temp_df['extras_type'] == 'noballs')]['total_runs'].sum()
        player_econ = player_runs / player_overs if player_overs !=0 else np.nan
        player_sr = player_deliveries / player_wickets if player_wickets !=0 else np.nan
        player_avg = player_runs / player_wickets if player_wickets !=0 else np.nan
        
        temp_dict = {
            'Season':[season],
            'Matches': [player_matches], 
            'Overs': [player_overs], 
            'Runs': [player_runs], 
            'Wickets': [player_wickets], 
            'Econ': [player_econ], 
            'SR': [player_sr], 
            'Avg': [player_avg]
        }
        
        temp_df = pd.concat([temp_df, pd.DataFrame(temp_dict)], ignore_index=True)
        
    return temp_df.dropna(subset=['Overs'])