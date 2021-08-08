import unicodedata
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# URL page we will scraping (see image above)

url2 = "https://www.basketball-reference.com/friv/last_n_days.fcgi"

# utilizing urllib3's urlopen to open the website linked to the url

html2 = urlopen(url2)

# using beautiful soup 4 to parse the opened url's data into html

soup2 = BeautifulSoup(html2, features="html.parser")

# because the table's rows are not defined or given classes, we simply retrieve every row instead
# covert all of the rows and data into a list

rows = soup2.findAll('tr')[1:]
rows_data = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

# remove all empty rows in the data

count = 20
while (count < 400):
    rows_data.pop(count)
    count += 20

# retrieving list of all table headers

head2 = soup2.find(class_="thead")

# creating a raw string of all table header texts

headers_raw2 = [head2.text for item in head2][0]

# creating a list out of the string of headers

headers2 = headers_raw2.replace("\n", ",").split(",")[2:-1]

stats2 = pd.DataFrame(rows_data, columns = headers2)

def strip_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if unicodedata.category(c) != 'Mn')

names2 = []
for i in stats2["Player"]:

    #i = unicodedata.normalize('NFD', i).encode('ascii', 'ignore')
    names2.append(strip_accents(i))

stats2["Player"] = names2

for i in headers2[2:]:
    stats2[i] = pd.to_numeric(stats2[i])

# function to calculate a player's score based on their last 7 days of play

def last7(name):
    score = 0
    j = 0
    for i in stats2["Player"]:
        if name.lower() == i.lower():
            score = stats2.loc[j]["PTS"] + 1.2*stats2.loc[j]["TRB"] + 1.5*stats2.loc[j]["AST"] + 3*stats2.loc[j]["STL"] + 3*stats2.loc[j]["BLK"] - 1.5*stats2.loc[j]["TOV"]
        j+=1
    return score    
last7("nikola jokic")



