import urllib.request
import sys
import os
import json

api_key = sys.argv[1]


if not os.path.exists("json_files"):
	os.mkdir("json_files")

response = urllib.request.urlopen('https://api.themoviedb.org/3/movie/latest?api_key=' + api_key)

json_response = json.load(response)

movie_count = int(json_response['id'])

print(movie_count)

# response = urllib.request.urlopen('https://api.themoviedb.org/3/movie/42728?api_key=' + api_key)

# print(response.read())

