import requests
import pandas as pd
import os
from datetime import datetime

#############
apikey = os.environ['APIKEY']
url = "https://api-nba-v1.p.rapidapi.com/standings"
apihost = "api-nba-v1.p.rapidapi.com"
league = "standard"
season ="2022"
readme_file = "README.md"
#############
querystring = {"league":league , "season": season}

headers = {
	"X-RapidAPI-Key": apikey,
	"X-RapidAPI-Host": apihost
}

response = requests.request("GET", url, headers=headers, params=querystring)
standings = response.json()["response"]


# Create a dictionary to store data for each division
conference_data = {"east": [], "west": []}

# Loop through standings and append data to division_data dictionary
for team in standings:

    conference = team["conference"]["name"]
    division = team["division"]["name"]
    name = team["team"]["name"]
    wins = team["win"]["total"]
    losses = team["loss"]["total"]
    Last10Games = str(team["win"]["lastTen"])+'W'+str(team["loss"]["lastTen"])+'L'
    
    conference_data[conference].append({
        "Team": name, "W": wins, "L": losses, "Last10Games": Last10Games})
    
east_df = pd.DataFrame(conference_data["east"]).sort_values("W", ascending=False).head(8)
west_df = pd.DataFrame(conference_data["west"]).sort_values("W", ascending=False).head(8)
east_md = east_df.to_markdown(index=False)
west_md = west_df.to_markdown(index=False)

# Update the README file with the new tables and the last update date
last_update_date = datetime.now().strftime("%Y-%m-%d")

with open(readme_file, "a") as f:
    f.write(f"\n\n### NBA Standings (Last updated on {last_update_date})\n\n")
    f.write("#### Eastern Conference\n\n")
    f.write(east_md)
    f.write("\n\n#### Western Conference\n\n")
    f.write(west_md)