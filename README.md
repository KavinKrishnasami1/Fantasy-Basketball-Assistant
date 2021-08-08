# Fantasy-Basketball-Assistant
In order to make the project, python3 must be installed, alongside a virtual environment which can be installed through window's Command prompt, or Mac's Terminal. It is not necessary, but recommended to install jupyter notebook inside of the virtual environment to run our program, and to install beautiful soup (bs4), pandas, and urllib3 as libraries we are using to create our program.

To run the test cases, run "python3 tests.py" in the terminal to compile the file. Afterwards, run "python3 -m pytest tests.py" to run the test cases.

To run the program, it is best to use jupyter notebook and convert all of the python files (.py) into .ipynb files, which are Jupyter's notebook documents. This is best because jupyter notebook can be installed from your virtual environment, along with our imports, bs4, pandas, and urllib3. Furthermore, in our code, we included lines such as %run web_scraping_nba_data.ipynb, which run the jupyter python file, allowing for us to use functions from that file and other objects, such as lists.

To use the application, it is only necessary to call any of the functions inside a line, and to run the program either as a script, or using Jupyter Notebook's "run" function. The resultant object, whether it is a pandas dataframe, a list, etc, will be displayed on the terminal, or through Jupyter's program, under the code block executed. For example, to use the function bestTeam(), we can simply call bestTeam(), and to run that function, and it will print out a dataframe with the best team at this current time. It is necessary to run all previous code blocks, as the function uses lists and functions from previous blocks, such as a dataframe of all players, etc.

Some functions require arguments or parameters, generally strings which are any of the headers. As a result, the headers can be printed at any time, and seen before using one of them in a function, be it in a sorting or search algorithm.

We have also created a Team class, in order to implement our function that compares two team's lineups. To create a team, simply running "team1 = Team()", will create a team with those 5 players as the team. Then, the function requires two different teams, and those teams can be passed as arguments to the function FaceOff(team1, team2), in order to display who is the better team.

