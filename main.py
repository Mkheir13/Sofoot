import streamlit as st
import pandas as pd
import json

from matplotlib import pyplot as plt

# Vérifiez si la variable de session 'selected_style' existe, sinon initialisez-la à "Physical"
if 'selected_style' not in st.session_state:
    st.session_state.selected_style = "Physical"

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

selected_player = df[(df['team.name'] == "Paris Saint-Germain") & (df['position'] == "F")]

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
    st.subheader("Club is playing in the following style:")
    championship_style = {
        "17": "Physical, Technical, Attacking, Talent",
        "8": "Technical, Possession, Attacking, Talent",
        "23": "Defending, Technical, Talent",
        "34": "Technical, Attacking, Talent",
        "35": "Technical, Attacking, Talent",
    }
    st.write(championship_style[str(team_id).split(".")[0]])

    st.selectbox("Select the mean", ["mean_same_positions", "mean_all_players"], key="mean")

container = st.container()

columns_for_playerdata, columns_for_pitch = st.columns([1, 5])

len_of_players = len(slected_player_for_the_club)

player_columns = st.columns(5)

style_counts = {}
for style in ["Physical", "Technical", "Mental", "Tactical", "Attacking", "Possession", "Defending", "Talent"]:
    count = 0
    for data in eval(style):
        value = selected_player[data].values[0]
        mean = df[(df['team.name'] == team_name) & (df['position'] == selected_position)][data].mean()
        if value >= mean:
            count += 1
    style_counts[style] = count

best_styles = [style for style, count in style_counts.items() if count > 4]

with container:
    with columns_for_playerdata:
        st.subheader("Mean of the physical attributes")
        style = st.selectbox("Select a style",
                             ["Physical", "Technical", "Mental", "Tactical", "Attacking", "Possession", "Defending",
                              "Talent"], key="style",
                             index=["Physical", "Technical", "Mental", "Tactical", "Attacking", "Possession",
                                    "Defending", "Talent"].index(st.session_state.selected_style))

        # Nouvelle boucle pour afficher les informations pour chaque joueur
        for player in slected_player_for_the_club[:5]:
            selected_player = df[(df['team.name'] == team_name) & (
                        df['playername'] == player)]  # Déplacez cette ligne à l'intérieur de la boucle
            with player_columns[slected_player_for_the_club.tolist().index(player)]:
                st.markdown(
                    f'<img src="https://api.sofascore.app/api/v1/player/{str(selected_player["playerid"].values[0]).split(".")[0]}/image" style="border-radius: 50%; border: 2px solid #0e1117;"/>',
                    unsafe_allow_html=True)
                st.subheader(player)

                attrs = positions[selected_position]

                for data in attrs:
                    value = selected_player[data].values[0]
                    st.write(f"{data}: {value:.0f}")
                st.subheader(style)
                st.subheader("if the value is red, it means that the player is below the average")
                for data in eval(style):
                    value = selected_player[data].values[0]
                    mean = df[(df['team.name'] == team_name) & (df['position'] == selected_position)][data].mean()
                    if value >= mean:
                        color = "green"
                    else:
                        color = "red"

                    st.write(f"<p style='color:{color};'>{data}: {value:.0f}</p>", unsafe_allow_html=True)
        # Calcul des meilleurs styles pour tous les joueurs
        style_counts = {style: 0 for style in
                        ["Physical", "Technical", "Mental", "Tactical", "Attacking", "Possession", "Defending",
                         "Talent"]}
        for player in slected_player_for_the_club:
            selected_player = df[(df['team.name'] == team_name) & (df['playername'] == player)]
            for style in ["Physical", "Technical", "Mental", "Tactical", "Attacking", "Possession", "Defending",
                          "Talent"]:
                count = 0
                for data in eval(style):
                    value = selected_player[data].values[0]
                    mean_same_positions = df[(df['position'] == selected_position)][data].mean()
                    mean_all_players = df[data].mean()
                    if st.session_state.mean == "mean_same_positions":
                        mean = mean_same_positions
                    else:
                        mean = mean_all_players
                    if value >= mean:
                        count += 1
                style_counts[style] += count
        best_styles = [style for style, count in style_counts.items() if count > 4]


container_for_charts = st.container()
with container_for_charts:
    columns_for_piechart, columns_for_barchart = st.columns([1, 1])
    with columns_for_piechart:
        st.subheader("Style distribution of the team according to " + st.session_state.mean)
        fig, ax = plt.subplots()
        ax.pie([style_counts[style] for style in best_styles], labels=best_styles, autopct='%1.1f%%')
        st.pyplot(fig)
    with columns_for_barchart:
        containers_in_barchart = st.container()
        with containers_in_barchart:
            st.subheader(f"Tendencies of {championship} according to the predominant style in {team_name}")
            style_counts_championship = {style: 0 for style in
                                     ["Physical", "Technical", "Mental", "Tactical", "Attacking", "Possession",
                                      "Defending", "Talent"]}
            for player in slected_player_for_the_club:
                selected_player = df[(df['team.name'] == team_name) & (df['playername'] == player)]
                for style in ["Physical", "Technical", "Mental", "Tactical", "Attacking", "Possession", "Defending",
                          "Talent"]:
                    count = 0
                    for data in eval(style):
                        value = selected_player[data].values[0]
                        mean_same_positions = df[(df['position'] == selected_position)][data].mean()
                        mean_all_players = df[data].mean()
                        if st.session_state.mean == "mean_same_positions":
                            mean = mean_same_positions
                        else:
                            mean = mean_all_players
                        if value >= mean:
                            count += 1
                    style_counts_championship[style] += count
            best_styles_championship = [style for style, count in style_counts_championship.items() if count > 4]
            st.bar_chart({style: style_counts_championship[style] for style in best_styles_championship})
            st.subheader("The predominant style in the championship is:")
            st.write(max(style_counts_championship, key=style_counts_championship.get))
            st.subheader("The predominant style in the team is:")
            st.write(max(style_counts, key=style_counts.get))









