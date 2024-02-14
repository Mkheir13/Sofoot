import streamlit as st
import pandas as pd
from mplsoccer.pitch import Pitch, VerticalPitch
import numpy as np
import matplotlib.pyplot as plt

import json

from matplotlib import pyplot as plt

with open('playersdata.json', encoding='utf-8') as f:
    data = json.load(f)

with open('championship_tendances.json', encoding='utf-8') as f:
    data_tendances = json.load(f)

df = pd.json_normalize(data, max_level=2)

df.columns = df.columns.str.replace('data.statistics.', '')
df.columns = df.columns.str.replace('data.team.', 'team.')

df = df.apply(pd.to_numeric, errors='ignore')

ct = pd.json_normalize(data_tendances, max_level=2)

st.set_page_config(page_title="Football Players Data", layout="wide")

ForwardsDisplay = ["goals", "scoringFrequency", "goalConversionPercentage", "assists", "keyPasses", "wasFouled",
                   "appearances", "totalOppositionHalfPasses", "appearances"]
MidfieldersDisplay = ["totalDuelsWon", "touches", "totalShots", "interceptions", "successfulDribblesPercentage",
                      "accuratePassesPercentage",
                      "shotsFromOutsideTheBox"]
DefendersDisplay = ["totalDuelsWonPercentage", "ballRecovery", "tacklesWonPercentage", "aerialDuelsWonPercentage",
                    "totalOppositionHalfPasses",
                    "accuratePassesPercentage"]
GoalkeepersDisplay = ["saves", "penaltySave", "cleanSheet", "goalsConceded", "goalsConcededInsideTheBox", "savesCaught",
                      "savesParried", "errorLeadToGoal"]

Physical = ["groundDuelsWonPercentage", "aerialDuelsWonPercentage", "tackles", "interceptions", "ballRecovery",
            "wasFouled",
            "successfulDribbles",
            "minutesPlayed", "headedGoals"]

Technical = ["accuratePasses", "successfulDribbles", "keyPasses", "shotsOnTarget", "accurateCrosses",
             "touches", "accurateLongBalls"]

Mental = ["matchesStarted", "yellowCards", "scoringFrequency", "goalsAssistsSum",
          "penaltyConversion"]

Tactical = ["interceptions", "accurateFinalThirdPasses", "keyPasses", "possessionWonAttThird",
            "expectedAssists"]

Attacking = ["goals", "expectedGoals", "shotsOnTarget", "successfulDribbles", "keyPasses",
             "accurateCrosses"]

Possession = ["accuratePasses", "possessionLost", "touches", "accurateLongBalls",
              "ballRecovery"]

Defending = ["tackles", "interceptions", "groundDuelsWon", "aerialDuelsWon",
             "blockedShots"]

Talent = ["goals", "expectedGoals", "successfulDribbles", "keyPasses",
          "wasFouled"]

positions = {
                    "F": ForwardsDisplay,
                    "M": MidfieldersDisplay,
                    "D": DefendersDisplay,
                    "G": GoalkeepersDisplay
                }

with st.sidebar:
    col1, col2 = st.columns(2)
    team_name = st.selectbox("Select a team", df['team.name'].unique())
    st.title("Data of " + team_name)
    team_id = df[df['team.name'] == team_name]['team.id'].values[0]
    st.image(f'https://api.sofascore.app/api/v1/team/{str(team_id).split(".")[0]}/image', width=200)
    selected_position = st.selectbox("Select a position", df['position'].unique())
    # select the player based on the team and the position
    slected_player_for_the_club = df[(df['team.name'] == team_name) & (df['position'] == selected_position)][
        'playername'].unique()

    st.title("Championship Tendances")
    championships_dict = {
        "17": "Premier League",
        "8": "La Liga",
        "23": "Serie A",
        "34": "Ligue 1",
        "35": "Bundesliga",
    }
    team_id = df[df['team.name'] == team_name]['tournament'].values[0]

    championship = championships_dict[str(team_id).split(".")[0]]
    st.subheader(f"Championship : {championship}")

container = st.container()

columns_for_playerdata, columns_for_pitch = st.columns([1, 5])

len_of_players = len(slected_player_for_the_club)

player_columns = st.columns(5)

with container:
    with columns_for_playerdata:
        st.subheader("Mean of the physical attributes")
        style = st.selectbox("Select a style",
                             ["Physical", "Technical", "Mental", "Tactical", "Attacking", "Possession", "Defending",
                              "Talent"])
        for data in eval(style):
            mean = df[(df['team.name'] == team_name) & (df['position'] == selected_position)][data].mean()
        for player in slected_player_for_the_club[:5]:
            with player_columns[slected_player_for_the_club.tolist().index(player)]:
                st.markdown(
                    f'<img src="https://api.sofascore.app/api/v1/player/{str(df[df["playername"] == player]["playerid"].values[0]).split(".")[0]}/image" style="border-radius: 50%; border: 2px solid #0e1117;"/>',
                    unsafe_allow_html=True)
                selected_player = df[(df['team.name'] == team_name) & (df['playername'] == player)]
                st.subheader(player)

                attrs = positions[selected_position]

                for data in attrs:
                    value = selected_player[data].values[0]

                    st.write(f"{data}: {value:.0f}")
                st.subheader(style)
                for data in eval(style):
                    value = selected_player[data].values[0]
                    mean = df[(df['team.name'] == team_name) & (df['position'] == selected_position)][data].mean()
                    if value >= mean:
                        color = "green"
                    else:
                        color = "red"
                    st.write(f"<p style='color:{color};'>{data}: {value:.0f}</p>", unsafe_allow_html=True)
