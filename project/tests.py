import pytest
import pandas as pd
import datatest as dt

@pytest.fixture(scope='module')
@dt.working_directory(_file_)
def df():
    return pd.read_csv('2021_stats.csv')


@pytest.mark.mandatory
def test_columns(df):
    dt.validate(
        df.columns,
        {'Unnamed: 0', 'Player','Pos','Age','Tm','G','GS','MP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS'},
    )

def test_player(df):
    dt.validate.regex(df['Player'], r'^[A-Z]')

def test_pos(df):
    dt.validate.regex(df['Pos'], r'^[A-Z]')

def test_age(df):
    dt.validate(df['Age'], int)

def test_tm(df):
    dt.validate.regex(df['Tm'], r'^[A-Z]')

def test_g(df):
    dt.validate(df['G'], int)

def test_gs(df):
    dt.validate(df['GS'], int)

def test_mp(df):
    dt.validate(df['MP'], float)

def test_fg(df):
    dt.validate(df['FG'], float)

def test_fga(df):
    dt.validate(df['FGA'], float)

def test_fgperc(df):
    dt.validate(df['FG%'], float)

def test_threep(df):
    dt.validate(df['3P'], float)

def test_threepattempt(df):
    dt.validate(df['3PA'], float)

def test_tov(df):
    dt.validate(df['3P%'], float)

def test_tov(df):
    dt.validate(df['2P'], float)

def test_twop(df):
    dt.validate(df['2PA'], float)


def test_twoppercent(df):
    dt.validate(df['2P%'], float)

def test_efg(df):
    dt.validate(df['eFG%'], float)

def test_tov(df):
    dt.validate(df['FT'], float)

def test_tov(df):
    dt.validate(df['FT%'], float)

def test_orb(df):
    dt.validate(df['ORB'], float)

def test_drb(df):
    dt.validate(df['DRB'], float)

def test_trb(df):
    dt.validate(df['TRB'], float)

def test_ast(df):
    dt.validate(df['AST'], float)

def test_stl(df):
    dt.validate(df['STL'], float)

def test_blk(df):
    dt.validate(df['BLK'], float)

def test_tov(df):
    dt.validate(df['TOV'], float)

def test_pf(df):
    dt.validate(df['PF'], float)

def test_pts(df):
    dt.validate(df['PTS'], float)