import json
import pandas as pd
import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("json_files/*.json"):
	f = open(one_file_name, "r")
	json_data = json.load(f)
	df = df.append({
		'adult':json_data['adult'],
		'backdrop_path':json_data['backdrop_path'],
		'belongs_to_collection':json_data['belongs_to_collection'],
		'budget':json_data['budget'],
		'genres':json_data['genres'],
		'homepage':json_data['homepage'],
		'id':json_data['id'],
		'imdb_id':json_data['imdb_id'],
		'original_language':json_data['original_language'],
		'original_title':json_data['original_title'],
		'overview':json_data['overview'],
		'popularity':json_data['popularity'],
		'poster_path':json_data['poster_path'],
		'production_companies':json_data['production_companies'],
		'production_countries':json_data['production_countries'],
		'release_date':json_data['release_date'],
		'revenue':json_data['revenue'],
		'runtime':json_data['runtime'],
		'spoken_languages':json_data['spoken_languages'],
		'status':json_data['status'],
		'tagline':json_data['tagline'],
		'title':json_data['title'],
		'video':json_data['video'],
		'vote_average':json_data['vote_average'],
		'vote_count':json_data['vote_count']
		}, ignore_index=True)

df.to_csv("parsed_files/tmdb_dataset.csv")

