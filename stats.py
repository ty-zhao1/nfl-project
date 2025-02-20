import requests

#rapid-api

# # use all nfl players by team ID, example is here
url = "https://nfl-api-data.p.rapidapi.com/nfl-player-listing/v1/data"

querystring = {"id":"22"} # repeat from 0 to 31

headers = {
	"x-rapidapi-key": "470de29086msh9c226f9de1ed3eep12569djsnb5317edc8903",
	"x-rapidapi-host": "nfl-api-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

# then use get nfl player stats by player ID, example is here
# url = "https://nfl-api-data.p.rapidapi.com/nfl-ath-statistics"

# querystring = {"year":"2023","id":"14876"}

# headers = {
# 	"x-rapidapi-key": "470de29086msh9c226f9de1ed3eep12569djsnb5317edc8903",
# 	"x-rapidapi-host": "nfl-api-data.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())