import streamlit as st
import pandas as pd
from mplsoccer.pitch import Pitch, VerticalPitch
import numpy as np
import matplotlib.pyplot as plt

import json

from matplotlib import pyplot as plt

with open('playersdata.json', encoding='utf-8') as f:
    data = json.load(f)

df = pd.json_normalize(data,
                       meta=['playername',
                             'position',
                             'playerid',
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
                             ['data', 'team', 'teamColors', 'primary'],
                             ]
                       )

df.columns = df.columns.str.replace('data.statistics.', '')
df.columns = df.columns.str.replace('data.team.', 'team.')

df = df.apply(pd.to_numeric, errors='ignore')

st.set_page_config(page_title="Football Players Data", layout="wide")

with st.sidebar:
    col1, col2 = st.columns(2)
    team_name = st.selectbox("Select a team", df['team.name'].unique())
    st.title("Data of " + team_name)
    team_id = df[df['team.name'] == team_name]['team.id'].values[0]
    st.image(f'https://api.sofascore.app/api/v1/team/{str(team_id).split(".")[0]}/image', width=200)
    slected_player_for_the_club = st.selectbox("Select a player",
                                               df[df['team.name'] == team_name]['playername'].unique())
    player_id = str(df[df['playername'] == slected_player_for_the_club]['playerid'].values[0]).split(".")[0]

container = st.container()

columns_for_playerdata, columns_for_pitch = st.columns([1, 1])

with columns_for_playerdata:
    st.title(slected_player_for_the_club)
    st.markdown(
        f'<img src="https://api.sofascore.app/api/v1/player/{player_id}/image" style="border: 2px solid black; border-radius: 20px;">',
        unsafe_allow_html=True)

    st.write("## Player Stats")

    columns1, columns2, columns3 = st.columns([0.3, 0.3, 0.3])

    columns1.metric(" 🥅 Goals",
                    str(df[df['playername'] == slected_player_for_the_club]['goals'].values[0]).split(".")[0])
    columns1.metric(" 📐 Assists",
                    str(df[df['playername'] == slected_player_for_the_club]['assists'].values[0]).split(".")[0])

    columns2.metric(" 👟 Shots",
                    str(df[df['playername'] == slected_player_for_the_club]['totalShots'].values[0]).split(".")[0])
    columns2.metric(" 🔁 Passes",
                    str(df[df['playername'] == slected_player_for_the_club]['totalPasses'].values[0]).split(".")[0])

    columns3.metric(" 🌟 Big Chances Created",
                    str(df[df['playername'] == slected_player_for_the_club]['bigChancesCreated'].values[0]).split(".")[
                        0])
    columns3.metric(" 💢 Big Chances Missed",
                    str(df[df['playername'] == slected_player_for_the_club]['bigChancesMissed'].values[0]).split(".")[
                        0])

with columns_for_pitch:






    # forwards = df[df['position'] == 'F']
    # midfielders = df[df['position'] == 'M']
    # defenders = df[df['position'] == 'D']
    # goalkeepers = df[df['position'] == 'G']
    #
    # fig, ax = plt.subplots(figsize=(10, 10))
    # fig.set_facecolor('white')
    # ax.patch.set_facecolor('#0e1117')
    #
    # pitch = VerticalPitch(pitch_type='tracab', pitch_length=104, pitch_width=68, half=False, axis=True, label=True,
    #                       pitch_color='#0e1117', line_color='white')
    # pitch.draw(ax=ax)
    #
    # team_players = df[df['team.name'] == team_name]['playername'].unique()
    # team_players_position = df[df['team.name'] == team_name]['position'].unique()
    #
    # Goalkeeper = [0, -4500]
    # Defenders = [[3000, -2800], [1600, -3600], [0, -2400], [-1600, -3600], [-3000, -2800]]
    # Midfielders = [[1600, -1700], [0, -1100], [-1600, -1700]]
    # Forwards = [[1700, -200], [-1700, -200]]
    #
    # player_positions = np.array(Forwards + Midfielders + Defenders + [Goalkeeper])
    #
    # for i, txt in enumerate(team_players[:11]):
    #     ax.text(player_positions[i, 0], player_positions[i, 1], txt, color='white', fontsize=10, ha='center', va='center',
    #             zorder=2, rotation=360)
    # plt.show()
    # st.pyplot(fig)



# with st.container():
#     st.title("Goals Players Data for Forwards : 2023/2024 Season")
#
# col1, col2 = st.columns(2)
#
# player_name_for_comparaison = ""
# player_name_for_comparaison2 = ""
# stats = {}
#
# colors_first_player = df['team.teamColors.primary'].unique()
# colors_second_player = "black"
#
# # select all players with the position of forward
# forwards = df[df['position'] == 'F']
# # select all players with the position of midfielder
# midfielders = df[df['position'] == 'M']
# # select all players with the position of defender
# defenders = df[df['position'] == 'D']
# # select all players with the position of goalkeeper
# goalkeepers = df[df['position'] == 'G']
#
# # team name
# team_name = df['team.name'].values[0]
#
# with st.sidebar:
#     st.title("Football Players Data")
#     st.subheader("Search for players and teams")
#     st.write("Search for players and teams and compare their statistics")
#     st.write("Data from: [Sofa-score](https://www.sofascore.com)")
#
# with col1:
#     st.subheader("Search Team")
#
#     search = st.text_input("Search Team")
#
#     df = df.rename(columns={"team.name": "team_name"})
#
#     if search:
#         team_name = df[df['team_name'].astype(str).str.contains(search)]
#
#     if st.button('Search'):
#         df = df[df['team_name'].astype(str).str.contains(search)]
#
#     team_players = df['playername'].unique()
#
#     pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
#
#     Goalkeeper = [5, 40]
#     Defenders = [[25, 10], [20, 30], [20, 50], [25, 70]]
#     Midfielders = [[40, 10], [40, 30], [40, 50], [40, 70]]
#     Forwards = [[60, 30], [60, 50]]
#
#     player_positions = np.array(Forwards + Midfielders + Defenders + [Goalkeeper])
#     fig, ax = pitch.draw(figsize=(20, 30))
#
#     for i, txt in enumerate(team_players[:11]):
#         ax.text(player_positions[i, 0], player_positions[i, 1], txt, color='black', fontsize=20, ha='center',
#                 va='center', zorder=2, rotation=-90)
#
#     ax.set_ylim(0, 80)
#     plt.show()
#     st.pyplot(fig)
#     st.image(f'https://api.sofascore.app/api/v1/team/{str(df["team.id"].values[0]).split(".")[0]}/image', width=200)
#
#     selector = st.selectbox('Select a player', team_players)
#
#     if selector:
#         df = df[df['playername'].astype(str).str.contains(selector)]
#
#         selected_player = df[df['playername'] == selector]
#         # stock player name
#         player_name_for_comparaison = selected_player['playername'].values[0]
#
#         st.subheader(f"{selector} has scored {selected_player['goals'].values[0]} goals")
#
#         columns1, columns2, columns3 = st.columns(3)
#
#         columns1.metric(" 🥅 Goals", selected_player['goals'].values[0])
#         columns1.metric(" 📐 Assists", selected_player['assists'].values[0])
#
#         columns2.metric(" 👟 Shots", selected_player['totalShots'].values[0])
#         columns2.metric(" 🔁 Passes", selected_player['totalPasses'].values[0])
#
#         columns3.metric("Big Chances Created", selected_player['bigChancesCreated'].values[0])
#         columns3.metric("Big Chances Missed", selected_player['bigChancesMissed'].values[0])
#
#         st.write(f" 🏃‍♂️ Minutes Played: {selected_player['minutesPlayed'].values[0]}")
#
# with col2:
#     st.subheader("Search Player")
#
#     player_name = st.text_input("Search Player")
#
#     if player_name:
#         df = df[df['playername'].astype(str).str.contains(player_name)]
#
#     if st.button('Show Player Stats'):
#
#         searched_player = [p for p in data if p['playername'].lower() == player_name.lower()]
#
#         if searched_player:
#
#             player = searched_player[0]
#             # stock player name
#             player_name_for_comparaison2 = player['playername']
#
#             stats = player['data']['statistics']
#             colors_second_player = player['data']['team']['teamColors']['primary']
#
#             st.subheader(f"Statistics for {player['playername']}")
#
#             col1, col2, col3 = st.columns(3)
#
#             col1.metric(" 🥅 Goals", stats.get('goals', 0))
#             col1.metric(" 📐 Assists", stats.get('assists', 0))
#
#             col2.metric(" 👟 Shots", stats.get('totalShots', 0))
#             col2.metric(" 🔁 Passes", stats.get('totalPasses', 0))
#
#             col3.metric("Big Chances Created", stats.get('bigChancesCreated', 0))
#             col3.metric("Big Chances Missed", stats.get('bigChancesMissed', 0))
#
#             st.write(f" 🏃‍♂️ Minutes Played: {stats.get('minutesPlayed', 0)}")
#
#         else:
#             st.write("No player found")
#
# with st.container():
#     st.subheader("Player Goals Comparaison")
#
#     col1, col2, col3, col4 = st.columns(4)
#     if player_name_for_comparaison and player_name_for_comparaison2:
#         st.write(f"Comparing {player_name_for_comparaison} and {player_name_for_comparaison2}")
#
#     with col1:
#         # sns for goals
#         fig, ax = plt.subplots()
#         # show the color of the team for each player
#         ax.bar([player_name_for_comparaison, player_name_for_comparaison2],
#                [selected_player['goals'].values[0], stats.get('goals', 0)],
#                color=[colors_first_player[0], colors_second_player])
#         ax.set_xlabel('Players')
#         ax.set_ylabel('Goals')
#         st.pyplot(fig)
#
#     with col2:
#         # nuage de points pour les buts pour tires effectués pour tous les joueurs de la meme position
#         fig, ax = plt.subplots()
#         ax.scatter(forwards['totalShots'], forwards['goals'], color='blue', label='Forwards')
#
#         ax.scatter([selected_player['totalShots'].values[0], stats.get('totalShots', 0)],
#                    [selected_player['goals'].values[0], stats.get('goals', 0)],
#                    color=[colors_first_player[0], colors_second_player], label='Selected Players')
#         forwards_with_better_conversion_rate = forwards[
#             forwards['goalConversionPercentage'] > selected_player['goalConversionPercentage'].values[0]]
#         ax.scatter(forwards_with_better_conversion_rate['totalShots'], forwards_with_better_conversion_rate['goals'],
#                    color='green',
#                    label='Forwards with better conversion rate')
#         ax.set_xlabel('Total Shots')
#         ax.set_ylabel('Goals')
#         ax.legend()
#         st.pyplot(fig)
#
#     with col3:
#         # sns for most clubs with the most players with a better goal conversion rate
#         fig, ax = plt.subplots()
#         forwards_with_better_conversion_rate.sort_values(by='goalConversionPercentage', ascending=False)[
#             'team.name'].value_counts().head(10).plot(kind='bar', color='blue')
#         ax.set_xlabel('Teams')
#         ax.set_ylabel('Number of players')
#         st.pyplot(fig)
#
#     # write the name of the forwards that have a better goal conversion rate than the selected player
#     forwards_with_better_conversion_rate = forwards[
#         forwards['goalConversionPercentage'] > selected_player['goalConversionPercentage'].values[0]]
#     st.write("Forwards with a better goal conversion rate than the selected player")
#
#     # goal conversion rate of the selected player
#     st.subheader(
#         f"Goal conversion rate of {player_name_for_comparaison}: {selected_player['goalConversionPercentage'].values[0]}")
#
#     # display the goal conversion from the most to the least
#     st.subheader(
#         f"Goal conversion rate from the most to the least that have a better goal conversion rate than {player_name_for_comparaison}:")
#     st.write(forwards_with_better_conversion_rate[
#                  ['playername', 'goalConversionPercentage', 'goals', 'totalShots', 'minutesPlayed', 'penaltiesTaken',
#                   'penaltyGoals', f'team.name']])
