#TODO retrieve data through http get request method
#TODO retrieve images through http get request method
#TODO storage data in Database
#TODO storage images in subfolders
#TODO storage local references to the images in the database
import requests
import json

def main():
    #Retrive a JSON to 10 pokemons
    r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10')
    PreviewPokemons=r.json().get('results')
    Pokemons=list()
    #Get the complete Json for every Pokemon previously retrieved
    for x in PreviewPokemons:
        Pokemons.append((requests.get(x.get('url')).json()))
    
    for x in Pokemons:
        print(x.get('name'))
        print(x.get('base_experience'))

if __name__ == "__main__":
    main()