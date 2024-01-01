import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import json

# players_data = pd.read_json('./playersdata.json')

# # print(players_data['data'][0]['statistics']['rating']) #run python3 index.py to get players datas.
# print(players_data['data'][0].keys())

# rows = list(players_data['data'][0]['statistics'].keys())
# print(rows)

# columns = list(players_data['playername'])
# print(columns)
# ### Number of players retrieved ###

# rows = len(players_data.axes[0])
# columns = len(players_data.axes[1])

# print(f'Number of Rows: ', rows)
# print(f'Number of Columns: ', columns)

#################

with open('./playersdata.json') as f:
    players_data = json.load(f)

df = pd.json_normalize(players_data,
                            meta= 
                                [
                                    'playername',
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
                                    ['data', 'team', 'teamColors'],
                                    ['data', 'team', 'primary'],
                                    ['data', 'team', 'secondary'],
                                    ['data', 'team', 'text']
                                ]
                       )

df.columns = ['name', 'rating', 'totalRating', 'countRating', 'goals', 'bigChancesCreated', 'bigChancesMissed', 'expectedAssists', 'goalsAssistsSum', 'accuratePasses', 'inaccuratePasses', 'totalPasses', 'accuratePassesPercentage', 'accurateOwnHalfPasses', 'accurateOppositionHalfPasses', 'accurateFinalThirdPasses', 'keyPasses', 'successfulDribbles', 'successfulDribblesPercentage', 'tackles', 'interceptions', 'yellowCards', 'directRedCards', 'redCards', 'accurateCrosses', 'accurateCrossesPercentage', 'totalShots', 'shotsOnTarget', 'shotsOffTarget', 'groundDuelsWon', 'groundDuelsWonPercentage', 'aerialDuelsWon', 'aerialDuelsWonPercentage', 'totalDuelsWon', 'totalDuelsWonPercentage', 'minutesPlayed', 'goalConversionPercentage', 'penaltiesTaken', 'penaltyGoals', 'penaltyWon', 'penaltyConceded', 'shotFromSetPiece', 'freeKickGoal', 'goalsFromInsideTheBox', 'goalsFromOutsideTheBox', 'shotsFromInsideTheBox', 'shotsFromOutsideTheBox', 'headedGoals', 'leftFootGoals', 'rightFootGoals', 'accurateLongBalls', 'accurateLongBallsPercentage', 'clearances', 'errorLeadToGoal', 'errorLeadToShot', 'dispossessed', 'possessionLost', 'possessionWonAttThird', 'totalChippedPasses', 'accurateChippedPasses', 'touches', 'wasFouled', 'fouls', 'hitWoodwork', 'ownGoals', 'dribbledPast', 'offsides', 'blockedShots', 'passToAssist', 'saves', 'cleanSheet', 'penaltyFaced', 'penaltySave', 'savedShotsFromInsideTheBox', 'savedShotsFromOutsideTheBox', 'goalsConcededInsideTheBox', 'goalsConcededOutsideTheBox', 'punches', 'runsOut', 'successfulRunsOut', 'highClaims', 'crossesNotClaimed', 'matchesStarted', 'penaltyConversion', 'setPieceConversion', 'totalAttemptAssist', 'totalContest', 'totalCross', 'duelLost', 'aerialLost', 'attemptPenaltyMiss', 'attemptPenaltyPost', 'attemptPenaltyTarget', 'totalLongBalls', 'goalsConceded', 'tacklesWon', 'tacklesWonPercentage', 'scoringFrequency', 'yellowRedCards', 'savesCaught', 'savesParried', 'totalOwnHalfPasses', 'totalOppositionHalfPasses', 'totwAppearances', 'expectedGoals', 'goalKicks', 'ballRecovery', 'id', 'assists', 'type', 'appearances', 'team', 'slugTeam', 'shortName', 'gender', 'sport', 'sportSlug', 'sportId', 'userCount', 'nameCode', 'disabled', 'national', 'type', 'teamId', 'teamColorsPrimary', 'teamColorsSecondary', 'teamText', 'errorCode', 'errorMessage']


print(df)
