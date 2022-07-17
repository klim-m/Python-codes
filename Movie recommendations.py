
import copy 
import json
import requests

def get_movies_from_tastedive(word):
    base_url = "https://tastedive.com/api/similar"
    params_dict = {}			#empty dict
    params_dict["q"] = word	    #assigns key as code q and value as word
    params_dict["max"] = "5"    #returns a max of 5 movies
    params_dict["type"] = "movie"   #defines type of output to be movies only 
    info_url = requests.get(base_url, params = params_dict)
    print(info_url.url)
    api_info = json.loads(info_url.text)
    #print(type(api_info))
    pretty_print = json.dumps(api_info, indent = 2)
    #print(pretty_print)
    first_level = api_info['Similar']['Results']
    #print(first_level)
    movie_names =  [sublist['Name'] for sublist in first_level]
    return movie_names


def get_movie_data(movie):
    base_url = 'http://www.omdbapi.com/'
    api_key = "499b7e"
    param = {}
    param['t'] = movie
    param['r'] = "json"
    param['apikey']= api_key
    #print(param)
    omdb_api = requests.get(base_url, params = param)
    omdb_info = json.loads(omdb_api.text)
    return omdb_info

def movieResults(movie):
    movie_metadata = get_movie_data(movie)
    duration = movie_metadata['Runtime']
    imdbRating = movie_metadata['imdbRating']
    gross = movie_metadata["BoxOffice"]
    title_year = movie_metadata["Year"]
    message = "Movie: {} ,Title Year: {} , Duration: {} , imdb: {} , gross: {} ".format(movie, title_year, duration, imdbRating, gross)
    return message

def message():
    movie = input("Please enter movie name")
    message = "Recommendations for {} are {}".format(movie, get_movies_from_tastedive(movie))
    message2 = ("Data for {} is {}".format(movie, movieResults(movie)))
    final_message = message + message2
    return final_message

message()
