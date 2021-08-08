%run dataframe_creation.ipynb

# function that creates the best lineup based on each position and who has the higest fantasy score in their respective role
# some players can be registered as multiple positions

def bestTeam():
    players = []
    center = 0
    power_forward = 0
    small_forward = 0
    point_guard = 0 
    shooting_guard = 0
    
    j = 0
    for i in fantasy_sorted_by_total["Score Per Game"]:
        #print(i)
        if ('C' in fantasy_sorted_by_total.loc[j]["Pos"]):
            if (fantasy_sorted_by_total.loc[j]["Score Per Game"] > center):
                center = fantasy_sorted_by_total.loc[j]["Score Per Game"] 
                best_center = fantasy_sorted_by_total.loc[j]
        elif ('PF' in fantasy_sorted_by_total.loc[j]["Pos"]):
            if (fantasy_sorted_by_total.loc[j]["Score Per Game"] > power_forward):
                power_forward = fantasy_sorted_by_total.loc[j]["Score Per Game"]
                best_pf = fantasy_sorted_by_total.loc[j]
        elif ('SF' in fantasy_sorted_by_total.loc[j]["Pos"]):
            if (fantasy_sorted_by_total.loc[j]["Score Per Game"] > small_forward):
                small_forward = fantasy_sorted_by_total.loc[j]["Score Per Game"]
                best_sf = fantasy_sorted_by_total.loc[j]
        elif ('PG' in fantasy_sorted_by_total.loc[j]["Pos"]):
            if (fantasy_sorted_by_total.loc[j]["Score Per Game"] > point_guard):
                point_guard = fantasy_sorted_by_total.loc[j]["Score Per Game"]
                best_pg = fantasy_sorted_by_total.loc[j]
        elif ('SG' in fantasy_sorted_by_total.loc[j]["Pos"]):
            if (fantasy_sorted_by_total.loc[j]["Score Per Game"] > shooting_guard):
                shooting_guard = fantasy_sorted_by_total.loc[j]["Score Per Game"]
                best_sg = fantasy_sorted_by_total.loc[j]
        j+=1
    players.append(best_center)
    players.append(best_pf)
    players.append(best_sf)
    players.append(best_pg)
    players.append(best_sg)
    best_team = pd.DataFrame(players, columns = fantasy_headers)
    return best_team

# you can simply call bestTeam() in order to generate a dataframe showing the best lineup you can create at this current time
bestTeam()

# sort by a player's fantasy related statistics

def fantasySortByDescending(stat):
    return fantasy_stats.sort_values(stat, ascending=False)
def fantasySortByAscending(stat):
    return fantasy_stats.sort_values(stat, ascending=True)

# call either function, ascending or descending depending on what you want, on any header/element in fantasy_stats
fantasySortByDescending("Total").head(20)

# class Team which is composed of 5 players

class Team:
    
    
    #constructor
    
    def __init__(self, n1, n2, n3, n4, n5):
        self.team_players = []
        self.team_players.append(n1)
        self.team_players.append(n2)
        self.team_players.append(n3)
        self.team_players.append(n4)
        self.team_players.append(n5)
    
    #remove a player on your team
    def removePlayer(self, name):
        self.team_players.remove(name)
        
    #add a player to your team
    def addPlayer(self, name):
        self.team_players.append(name)
        
    #display a dataframe showing your team and their fantasy scores
    def myTeam(self):
        j = 0
        searched_players = []
        for i in self.team_players:
            for k in fantasy_stats["Player"]:
                #print(i)
                if k.lower() in i.lower():
                    #print(stats.loc[j])
                    searched_players.append(fantasy_stats.loc[j])
                j+=1
            j = 0
            
        searched = pd.DataFrame(searched_players, columns = fantasy_headers)
        return searched


t1 = Team("james harden", "lebron james", "kevin durant", "nikola jokic", "stephen curry")
t1.removePlayer("lebron james")
t1.addPlayer("giannis antetokounmpo")
t1.myTeam()

t2 = Team("bradley beal", "lebron james", "kyrie irving", "russell westbrook", "anthony davis")
t2.myTeam()

# given two different teams, displays whose team is better than the other

def FaceOff(team1, team2):
    team1_score = 0
    for i in team1.team_players:
        team1_score += fantasyScore(i)
    
    team2_score = 0
    for i in team2.team_players:
        team2_score += fantasyScore(i)
    
    if (team1_score > team2_score):
        return "Team 1 is better! The team's score is better than Team 2's by: " + str(round(team1_score - team2_score, 2))
    elif (team1_score < team2_score):
        return "Team 2 is better! The team's score is better than Team 1's by: " + str(round(team2_score - team1_score, 2))
    else:
        return "Your teams have exactly the same score as each other!"
        
FaceOff(t1, t2)



