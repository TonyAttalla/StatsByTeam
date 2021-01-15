from flask import Flask, jsonify
from flask_cors import CORS
import json
import requests
from flask import request
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs
import pandas as pd
import nbapy as nba
from bs4 import BeautifulSoup
from requests import get

# configuration
#DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/statsovertimeplayer', methods=['GET'])
def getStatsOverTimeByPlayer():
    playerName = str(request.args.get('playerName'))
    statName = str(request.args.get('statName'))
    chartData = dict()
    chartData["Years"] = list()
    chartData["stat"] = list()
    s = (get_stats(playerName, stat_type='PER_GAME', playoffs=False, career=False))
    stat = s[statName].values
    stat=stat.tolist()
    years = s['SEASON'].values
    for i in range(len(stat)):
        try:
            float(stat[i])
        except:
            stat[i] = '0.0'
    chartData["Years"] = years.tolist()
    chartData["stat"] = stat
    return(jsonify(chartData))


@app.route('/allteams', methods=['GET'])
def getTeamNamesBallDontLie():
    gridData = dict()
    gridData["Teams"] = list()
    url = "https://www.balldontlie.io/api/v1/teams"
    response = requests.request("GET", url)
    data = response.json()["data"]
    for team_data in data:
        team_name =  team_data["name"].lower()
        full_name = team_data["full_name"]
        if (team_name != "pelicans"):
            img_url ="../../public/teamIcons/" + team_name+ ".jpg"
            gridData["Teams"].append({"URL": img_url, "Name": team_name, "Short" : team_data["abbreviation"], "fullName": full_name})
        
    return jsonify(gridData)


@app.route('/roster', methods=['GET'])
def getRoster():
    teamname = str(request.args.get('teamName'))
    if (teamname == "CHA"):
        teamname = "CHO"
    if (teamname == "BKN"):
        teamname = "BRK"
    if (teamname == "PHX"):
        teamname = "PHO"
    year = str(2020)
    r = get("https://www.basketball-reference.com/teams/" + teamname + "/"+ year + ".html")
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
   
    return jsonify(df['Player'].values.tolist())

@app.route('/statsdropdown', methods=['GET'])
def getStatsDropDown():
    stats = (get_stats("Terence Davis", stat_type='PER_GAME', playoffs=False, career=False))
    return jsonify(stats.columns.values.tolist()[5:])
   
if __name__ == '__main__':
    #getStatsDropDown()
    app.run()
