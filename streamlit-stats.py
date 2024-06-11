import streamlit as st
import pandas as pd 

season_by_season_stats = pd.read_csv("player-totals.csv")

start_year = st.slider("Select the start year", 1974, 2023, 1974)
end_year = st.slider("Select the end year", 1974, 2024, 2024)

selected_years = season_by_season_stats[season_by_season_stats['season'].between(start_year,end_year)]

st.write(f'Compare season stats from {start_year}-{end_year} season')
options = st.multiselect(
     "Select three players to compare", selected_years['player'].drop_duplicates().tolist(), max_selections=3)

point_totals = selected_years[['season', 'player', 'pts']]

selected_players = point_totals[point_totals['player'].isin(options)]
selected_players['season'] = selected_players['season'].astype(str)

st.title(f'Points from {start_year}-{end_year} season')
st.line_chart(selected_players, x='season', y='pts', color='player')