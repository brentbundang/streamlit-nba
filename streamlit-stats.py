import streamlit as st
import pandas as pd 

season_by_season_stats = pd.read_csv("player-totals.csv")

start_year = st.slider("Select the start year", 1974, 2023, 1974)
end_year = st.slider("Select the end year", 1974, 2024, 2024)

selected_years = season_by_season_stats[season_by_season_stats['season'].between(start_year,end_year)]

st.write(f'Compare season stats from {start_year}-{end_year}')
options = st.multiselect(
    "Select ten players to compare", selected_years['player'].drop_duplicates().tolist(), max_selections=10)

different_stat_categories = selected_years[["field_goals_made","field_goals_attempted","fg_percent","three_pointers_made","three_pointers_attempted","three_point_percentage","two_pointers_made","two_pointers_attempted","two_pointers_percentage","effective_fg_percent","ft_made","fta","ft_percent","orb","drb","trb","ast","stl","blk","tov","pf","pts"]]
stat = st.selectbox("Select a stat category", different_stat_categories.columns)

point_totals = selected_years[['season', 'player', stat]]

selected_players = point_totals[point_totals['player'].isin(options)]
selected_players['season'] = selected_players['season'].astype(str)

st.title(f'{stat} from {start_year}-{end_year} season')
st.line_chart(selected_players, x='season', y=stat, color='player')