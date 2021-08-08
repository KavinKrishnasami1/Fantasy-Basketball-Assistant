%run web_scraping_nba_data.ipynb
%run web_scraping_last_seven.ipynb

# creating a new dataframe and headers given the same stats, including the fantasy score of a player

fantasy_players = []
j = 0
for i in stats["Player"]:
    player = []
    player.append(stats.loc[j]["Player"])
    player.append(fantasyScore(stats.loc[j]["Player"]))
    player.append(last7(stats.loc[j]["Player"]))
    player.append(last7(stats.loc[j]["Player"]) - fantasyScore(stats.loc[j]["Player"]))
    player.append(totalScore(stats.loc[j]["Player"]))
    player.append(stats.loc[j]["Pos"])
    player.append(stats.loc[j]["Tm"])
    player.append(stats.loc[j]["G"])
    player.append(stats.loc[j]["PTS"])
    player.append(stats.loc[j]["TRB"])
    player.append(stats.loc[j]["AST"])
    player.append(stats.loc[j]["STL"])
    player.append(stats.loc[j]["BLK"])
    player.append(stats.loc[j]["TOV"])
    fantasy_players.append(player)
    j+=1

fantasy_headers = ['Player', 'Score Per Game', 'Score Per Game (Last 7 Days)', 'Trend(Last 7 Days)', 'Total', 'Pos', 'Tm', 'G', 'PTS', 'TRB', 'AST', 'STL', 'BLK', 'TOV']
fantasy_stats = pd.DataFrame(fantasy_players, columns = fantasy_headers)
fantasy_stats

# similar to before, we are converting all numbers to be numerical values, rather than strings

for i in fantasy_headers[7:]:
    fantasy_stats[i] = pd.to_numeric(fantasy_stats[i])
fantasy_sorted_by_total = fantasy_stats.sort_values('Score Per Game', ascending=False)
fantasy_sorted_by_total

