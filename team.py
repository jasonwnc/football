# import urllib library
from urllib.request import urlopen

import json

# store the URL in url as 
# parameter for urlopen
#this will grab all of the football teams and drop them into a JSON data files
url = "http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams"

# store the response of URL
response = urlopen(url)

# storing the JSON response 
# from url in data
data_json = json.loads(response.read())

  
# print the json response
#print(data_json)

with open("football_file.json", "w") as write_file:
    json.dump(data_json, write_file)