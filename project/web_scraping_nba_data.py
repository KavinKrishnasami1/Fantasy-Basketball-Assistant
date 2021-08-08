#!/usr/bin/env python
# coding: utf-8

# In[9]:

import unicodedata
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

# NBA season we will be analyzing

year = 2021

# URL page we will scraping 

url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

# utilizing urllib3's urlopen to open the website linked to the url

html = urlopen(url)

# using beautiful soup 4 to parse the opened url's data into html

soup = BeautifulSoup(html, features="html.parser")

# retrieving html element, sorted by class

table = soup.find_all(class_="full_table")

# retrieving list of all table headers

head = soup.find(class_="thead")
#print(head)

# creating a raw string of all table header texts

headers_raw = [head.text for item in head][0]

#print(headers_raw)

# creating a list out of the string of headers

headers = headers_raw.replace("\n", ",").split(",")[2:-1]
#print(headers)

# creating list of all players based on previously created table

players = []

for i in range(len(table)):
    player = []
    for td in table[i].find_all("td"):
        player.append(td.text)

    players.append(player)

#players

# creating initial database/frame of all players with all stats sorted by scraped headers

stats = pd.DataFrame(players, columns = headers)


# stripping accents from all characters in player's names. 
# this is necessary because these characters aren't registered as ASCII characters, and python can't print them out properly

# this is also necessary for searching, because most users won't be able to type special characters, or recognizing them


def strip_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if unicodedata.category(c) != 'Mn')

names = []
for i in stats["Player"]:
    
    #i = unicodedata.normalize('NFD', i).encode('ascii', 'ignore')
    names.append(strip_accents(i))

stats["Player"] = names
#stats

# changing all numbers in the table to be registered as numeric values, rather than strings
# fixes the issue when sorting, 9.9 would be considered greater than 30, etc.

for i in headers[5:]:
    stats[i] = pd.to_numeric(stats[i])
#stats["PTS"] = pd.to_numeric(stats["PTS"])
sorted_by_points = stats.sort_values('PTS', ascending=False)
#sorted_by_points

# creating functions to calculate a player's fantasy value/score based on their current statistics per game

def fantasyScore(name):
    score = 0
    j = 0
    for i in stats["Player"]:
        if name.lower() == i.lower():
            score = stats.loc[j]["PTS"] + 1.2*stats.loc[j]["TRB"] + 1.5*stats.loc[j]["AST"] + 3*stats.loc[j]["STL"] + 3*stats.loc[j]["BLK"] - 1.5*stats.loc[j]["TOV"]
        j+=1
    return score

def totalScore(name):
    score = 0
    j = 0
    for i in stats["Player"]:
        if name.lower() == i.lower():
            score = float(stats.loc[j]["G"]) * fantasyScore(name)
        j+=1
    return score

#print(fantasyScore("James Harden"))
totalScore("James Harden")

# SQL DATABASE
#stats.to_sql('players', con=engine)
#engine.execute("SELECT * FROM players").fetchall()



stats.to_csv('2021_stats.csv', header=True)
