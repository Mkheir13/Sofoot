import streamlit as st
import pandas as pd
from mplsoccer.pitch import Pitch
import numpy as np
import matplotlib.pyplot as plt

import json
import csv

from matplotlib import pyplot as plt

# Load JSON data
with open('playersdata.json') as f:
    data = json.load(f)

df = pd.json_normalize(data,
                       meta=['playername',
                             ['data', 'statistics', 'rating'],
                             ['data', 'statistics', 'totalRating'],
                             ['data', 'statistics', 'countRating'],
                             ['data', 'statistics', 'goals'],
                             ['data', 'statistics', 'bigChancesCreated'],
                             ['data', 'statistics', 'bigChancesMissed'],
                             ['data', 'statistics', 'expectedAssists'],
                             ['data', 'statistics', 'goalsAssistsSum'],
                             ['data', 'statistics', 'accuratePasses'],
                             ['data', 'statistics', 'inaccuratePasses'],
                             ['data', 'statistics', 'totalPasses'],
                             ['data', 'statistics', 'accuratePassesPercentage'],
                             ['data', 'statistics', 'accurateOwnHalfPasses'],
                             ['data', 'statistics', 'accurateOppositionHalfPasses'],
                             ['data', 'statistics', 'accurateFinalThirdPasses'],
                             ['data', 'statistics', 'keyPasses'],
                             ['data', 'statistics', 'successfulDribbles'],
                             ['data', 'statistics', 'successfulDribblesPercentage'],
                             ['data', 'statistics', 'tackles'],
                             ['data', 'statistics', 'interceptions'],
                             ['data', 'statistics', 'yellowCards'],
                             ['data', 'statistics', 'directRedCards'],
                             ['data', 'statistics', 'redCards'],
                             ['data', 'statistics', 'accurateCrosses'],
                             ['data', 'statistics', 'accurateCrossesPercentage'],
                             ['data', 'statistics', 'totalShots'],
                             ['data', 'statistics', 'shotsOnTarget'],
                             ['data', 'statistics', 'shotsOffTarget'],
                             ['data', 'statistics', 'groundDuelsWon'],
                             ['data', 'statistics', 'groundDuelsWonPercentage'],
                             ['data', 'statistics', 'aerialDuelsWon'],
                             ['data', 'statistics', 'aerialDuelsWonPercentage'],
                             ['data', 'statistics', 'totalDuelsWon'],
                             ['data', 'statistics', 'totalDuelsWonPercentage'],
                             ['data', 'statistics', 'minutesPlayed'],
                             ['data', 'statistics', 'goalConversionPercentage'],
                             ['data', 'statistics', 'penaltiesTaken'],
                             ['data', 'statistics', 'penaltyGoals'],
                             ['data', 'statistics', 'penaltyWon'],
                             ['data', 'statistics', 'penaltyConceded'],
                             ['data', 'statistics', 'shotFromSetPiece'],
                             ['data', 'statistics', 'freeKickGoal'],
                             ['data', 'statistics', 'goalsFromInsideTheBox'],
                             ['data', 'statistics', 'goalsFromOutsideTheBox'],
                             ['data', 'statistics', 'shotsFromInsideTheBox'],
                             ['data', 'statistics', 'shotsFromOutsideTheBox'],
                             ['data', 'statistics', 'headedGoals'],
                             ['data', 'statistics', 'leftFootGoals'],
                             ['data', 'statistics', 'rightFootGoals'],
                             ['data', 'statistics', 'accurateLongBalls'],
                             ['data', 'statistics', 'accurateLongBallsPercentage'],
                             ['data', 'statistics', 'clearances'],
                             ['data', 'statistics', 'errorLeadToGoal'],
                             ['data', 'statistics', 'errorLeadToShot'],
                             ['data', 'statistics', 'dispossessed'],
                             ['data', 'statistics', 'possessionLost'],
                             ['data', 'statistics', 'possessionWonAttThird'],
                             ['data', 'statistics', 'totalChippedPasses'],
                             ['data', 'statistics', 'accurateChippedPasses'],
                             ['data', 'statistics', 'touches'],
                             ['data', 'statistics', 'wasFouled'],
                             ['data', 'statistics', 'fouls'],
                             ['data', 'statistics', 'hitWoodwork'],
                             ['data', 'statistics', 'ownGoals'],
                             ['data', 'statistics', 'dribbledPast'],
                             ['data', 'statistics', 'offsides'],
                             ['data', 'statistics', 'blockedShots'],
                             ['data', 'statistics', 'passToAssist'],
                             ['data', 'statistics', 'saves'],
                             ['data', 'statistics', 'cleanSheet'],
                             ['data', 'statistics', 'penaltyFaced'],
                             ['data', 'statistics', 'penaltySave'],
                             ['data', 'statistics', 'savedShotsFromInsideTheBox'],
                             ['data', 'statistics', 'savedShotsFromOutsideTheBox'],
                             ['data', 'statistics', 'goalsConcededInsideTheBox'],
                             ['data', 'statistics', 'goalsConcededOutsideTheBox'],
                             ['data', 'statistics', 'punches'],
                             ['data', 'statistics', 'runsOut'],
                             ['data', 'statistics', 'successfulRunsOut'],
                             ['data', 'statistics', 'highClaims'],
                             ['data', 'statistics', 'crossesNotClaimed'],
                             ['data', 'statistics', 'matchesStarted'],
                             ['data', 'statistics', 'penaltyConversion'],
                             ['data', 'statistics', 'setPieceConversion'],
                             ['data', 'statistics', 'totalAttemptAssist'],
                             ['data', 'statistics', 'totalContest'],
                             ['data', 'statistics', 'totalCross'],
                             ['data', 'statistics', 'duelLost'],
                             ['data', 'statistics', 'aerialLost'],
                             ['data', 'statistics', 'attemptPenaltyMiss'],
                             ['data', 'statistics', 'attemptPenaltyPost'],
                             ['data', 'statistics', 'attemptPenaltyTarget'],
                             ['data', 'statistics', 'totalLongBalls'],
                             ['data', 'statistics', 'goalsConceded'],
                             ['data', 'statistics', 'tacklesWon'],
                             ['data', 'statistics', 'tacklesWonPercentage'],
                             ['data', 'statistics', 'scoringFrequency'],
                             ['data', 'statistics', 'yellowRedCards'],
                             ['data', 'statistics', 'savesCaught'],
                             ['data', 'statistics', 'savesParried'],
                             ['data', 'statistics', 'totalOwnHalfPasses'],
                             ['data', 'statistics', 'totalOppositionHalfPasses'],
                             ['data', 'statistics', 'totwAppearances'],
                             ['data', 'statistics', 'expectedGoals'],
                             ['data', 'statistics', 'goalKicks'],
                             ['data', 'statistics', 'ballRecovery'],
                             ['data', 'statistics', 'id'],
                             ['data', 'statistics', 'assists'],
                             ['data', 'statistics', 'type'],
                             ['data', 'statistics', 'appearances'],
                             ['data', 'team', 'name'],
                             ['data', 'team', 'slug'],
                             ['data', 'team', 'shortName'],
                             ['data', 'team', 'gender'],
                             ['data', 'team', 'sport', 'name'],
                             ['data', 'team', 'sport', 'slug'],
                             ['data', 'team', 'sport', 'id'],
                             ['data', 'team', 'userCount'],
                             ['data', 'team', 'nameCode'],
                             ['data', 'team', 'disabled'],
                             ['data', 'team', 'national'],
                             ['data', 'team', 'type'],
                             ['data', 'team', 'id'],
                             ]
                       )

# clean the column names

df.columns = df.columns.str.replace('data.statistics.', '')
df.columns = df.columns.str.replace('data.team.', 'team.')

# convert the columns to numeric

df = df.apply(pd.to_numeric, errors='ignore')

# set page wide

st.set_page_config(page_title="Football Players Data", layout="wide")

col1, col2, col3 = st.columns([0.3, 0.3, 0.4])

with col1:
    st.subheader("Search Team")
    # Add a search bar
    search = st.text_input("Search Team")

    # Rename column without dots
    df = df.rename(columns={"team.name": "team_name"})

    if search:
        df = df[df['team_name'].astype(str).str.contains(search)]

    if st.button('Search'):
        df = df[df['team_name'].astype(str).str.contains(search)]

    team_players = df['playername'].unique()

    pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)

    player_positions = np.array([[5, 40],  # goalkeeper
                                [25, 10], [20, 30], [20, 50], [25, 70],  # defenders
                                [40, 10], [40, 30], [40, 50], [40, 70],  # midfielders
                                [60, 30], [60, 50]]) # forwards

    fig, ax = pitch.draw(figsize=(20, 30))
    ax.scatter(player_positions[:, 0], player_positions[:, 1], s=200, color='none', edgecolor='none', zorder=1)

    # put the 10 first player names on the pitch and display the name vertically
    for i, txt in enumerate(team_players[:11]):
        ax.text(player_positions[i, 0], player_positions[i, 1], txt, color='black', fontsize=20, ha='center', va='center', zorder=2, rotation=-90)

    plt.show()

    st.pyplot(fig)


    selector = st.selectbox('Select a player', team_players)

    if selector:
        df = df[df['playername'].astype(str).str.contains(selector)]

        selected_player = df[df['playername'] == selector]

        # display the goal scored by the selected player

        st.write(f"{selector} has scored {selected_player['goals'].values[0]} goals")

        columns1, columns2, columns3 = st.columns(3)

        columns1.metric(" 🥅 Goals", selected_player['goals'].values[0])
        columns1.metric(" 📐 Assists", selected_player['assists'].values[0])

        columns2.metric(" 👟 Shots", selected_player['totalShots'].values[0])
        columns2.metric(" 🔁 Passes", selected_player['totalPasses'].values[0])

        columns3.metric("Big Chances Created", selected_player['bigChancesCreated'].values[0])
        columns3.metric("Big Chances Missed", selected_player['bigChancesMissed'].values[0])

        st.write(f" 🏃‍♂️ Minutes Played: {selected_player['minutesPlayed'].values[0]}")

# search player name and display the player data

with col2:
    st.subheader("Search Player")

    player_name = st.text_input("Search Player")

    if player_name:
        df = df[df['playername'].astype(str).str.contains(player_name)]

    # Display player stats
    if st.button('Show Player Stats'):

        # Filter data
        searched_player = [p for p in data if p['playername'].lower() == player_name.lower()]

        if searched_player:

            player = searched_player[0]

            stats = player['data']['statistics']

            st.subheader(f"Statistics for {player['playername']}")

            col1, col2, col3 = st.columns(3)

            col1.metric(" 🥅 Goals", stats.get('goals', 0))
            col1.metric(" 📐 Assists", stats.get('assists', 0))

            col2.metric(" 👟 Shots", stats.get('totalShots', 0))
            col2.metric(" 🔁 Passes", stats.get('totalPasses', 0))

            col3.metric("Big Chances Created", stats.get('bigChancesCreated', 0))
            col3.metric("Big Chances Missed", stats.get('bigChancesMissed', 0))

            st.write(f" 🏃‍♂️ Minutes Played: {stats.get('minutesPlayed', 0)}")

        else:
            st.write("No player found")
