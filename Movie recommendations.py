
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


movie = input("Please enter movie name")
print("Recommendations for {} are {}".format(movie, get_movies_from_tastedive(movie)))