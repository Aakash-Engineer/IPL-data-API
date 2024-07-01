import pandas as pd

df1 = pd.read_csv('static/overall_batter_data.csv')
df2 = pd.read_csv('static/overall_bowler_data.csv')
df1.drop(columns=['Unnamed: 0'], inplace=True)
df2.drop(columns=['Unnamed: 0'], inplace=True)

df1.to_csv('static/overall_batter_data.csv', index=False)
df2.to_csv('static/overall_bowler_data.csv', index=False)