import urllib.request
import sys

api_key = sys.argv[1]

response = urllib.request.urlopen('https://api.themoviedb.org/3/movie/42728?api_key=' + api_key)

print(response.read())



# 