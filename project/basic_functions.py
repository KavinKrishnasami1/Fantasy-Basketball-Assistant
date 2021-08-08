%run web_scraping_nba_data.ipynb


# simple sorting method based on input header

def sortByDescending(stat):
    return stats.sort_values(stat, ascending=False)
def sortByAscending(stat):
    return stats.sort_values(stat, ascending=True)

sortByDescending("PTS")
sortByAscending("Age")

# function to search for all players with inputted name and display a table of all filtered players

def searchPlayer(name):
    j = 0
    searched_players = []
    for i in stats["Player"]:
        if name.lower() in i.lower():
            #print(stats.loc[j])
            searched_players.append(stats.loc[j])
        j+=1
    stats_for_searched = pd.DataFrame(searched_players, columns = headers)
    return stats_for_searched

searchPlayer("james")

