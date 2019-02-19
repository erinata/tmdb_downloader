import json


f = open("json_files/tmdb583249.json", "r")
json_data = json.load(f)
print(json_data['id'])


