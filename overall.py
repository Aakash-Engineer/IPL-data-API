import numpy as np
import pandas as pd


def batsman_data(season='Season', team='all', team_name='Team'):    
    balls = pd.read_csv('static/balls.csv')
    if season != 'Season':
        balls = balls[balls['season'] == int(season)]
        
    if team != 'Team':
        balls = balls[(balls['batting_team'] == team.lower())]
    batter_group = balls.groupby('batter')
    overall_batter_frame = pd.DataFrame(columns=['Player', 'Matches',  'Runs', 'Avg', 'SR', '100', '50', '4', '6'])

    extra_type_group = balls.groupby('extras_type')

    for player_name, group in batter_group:
        
        group['extras_type'] = group['extras_type'].fillna('fair')
        player_matches = group['id'].nunique()
        player_runs = group['batsman_runs'].sum()
        player_avg = player_runs / player_matches
        player_sixes = group[group['batsman_runs'] == 6].shape[0]
        player_fours = group[group['batsman_runs'] == 4].shape[0]
        player_100 = (group.groupby('id')['batsman_runs'].sum().values >= 100).sum()
        player_50 = (group.groupby('id')['batsman_runs'].sum().values >= 50).sum()
        
        # calculate strike rate
        total_delivery = 0
        if 'fair' in extra_type_group.groups:
            total_delivery += extra_type_group.get_group('fair').shape[0]
        if 'legbyes' in extra_type_group.groups:
            total_delivery += extra_type_group.get_group('legbyes').shape[0]
        if 'byes' in extra_type_group.groups:
            total_delivery += extra_type_group.get_group('byes').shape[0]
            
        player_strike_rate = (player_runs / total_delivery) * 100
        
        temp_dict ={
            'Player': [player_name], 
            'Matches': [player_matches], 
            'Runs': [player_runs], 
            'Avg': [player_avg], 
            'SR': [player_strike_rate], 
            '100': [player_100], 
            '50': [player_50], 
            '4': [player_fours], 
            '6': [player_sixes]
        } 
        
        overall_batter_frame = pd.concat([overall_batter_frame, pd.DataFrame(temp_dict)], ignore_index=True)
    return overall_batter_frame.sort_values('Runs', ascending=False)


def bowler_data(season='Season', team='all', team_name='Team'):
    balls = pd.read_csv('static/balls.csv')
    if season != 'Season':
        balls = balls[balls['season'] == int(season)]
        
    if team != 'Team':
        balls = balls[(balls['bowling_team'] == team.lower())]
    overall_bowler_frame = pd.DataFrame(columns=['Player', 'Matches', 'Overs', 'Runs', 'Wickets', 'Econ', 'SR', 'Bowling avg'])
    bowler_group = balls.groupby('bowler')

    for player_name, group in bowler_group:
        
        player_matches = group['id'].nunique()
        group['extras_type'] = group['extras_type'].fillna('fair')
        extra_type_group = group.groupby('extras_type')
        total_delivery = 0
        if 'fair' in extra_type_group.groups:
            total_delivery += extra_type_group.get_group('fair').shape[0]
        if 'legbyes' in extra_type_group.groups:
            total_delivery += extra_type_group.get_group('legbyes').shape[0]
        if 'byes' in extra_type_group.groups:
            total_delivery += extra_type_group.get_group('byes').shape[0] 
            
        player_overs = total_delivery // 6
        
        if not player_overs:
            player_overs = np.nan
        player_runs = 0
        if 'fair' in extra_type_group.groups:
            player_runs += extra_type_group.get_group('fair')['batsman_runs'].sum()
        if 'wides' in extra_type_group.groups:
            total_delivery += extra_type_group.get_group('wides')['batsman_runs'].sum()
        if 'noballs' in extra_type_group.groups:
            total_delivery += extra_type_group.get_group('noballs')['batsman_runs'].sum()
        
        player_wickets = group['is_wicket'].sum()
        if not player_wickets:
            player_wickets=np.nan
        player_bowling_avg = group['total_runs'].sum() / player_wickets 
        player_economy_rate = player_runs / player_overs
        player_strike_rate = total_delivery / player_wickets
        
        temp_dict = {
            'Player': [player_name], 
            'Matches': [player_matches], 
            'Overs' : [player_overs], 
            'Runs': [player_runs], 
            'Wickets':[player_wickets],
            'Econ': [player_economy_rate], 
            'SR': [player_strike_rate], 
            'Bowling avg': [player_bowling_avg]
        }
        
        overall_bowler_frame = pd.concat([overall_bowler_frame, pd.DataFrame(temp_dict)], ignore_index=True)
    return overall_bowler_frame.sort_values('Wickets', ascending=False)