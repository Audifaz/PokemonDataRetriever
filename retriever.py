#TODO storage local references to the images in the database
#TODO decentralize the main function

import requests
import json
import sqlite3
import os.path
from sqlite3 import Error
from databaseCreator import create_connection, getDatabasePath
import urllib.request

def retrievePokemons():
    #Retrive a JSON to 10 pokemons
    r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100')
    PreviewPokemons=r.json().get('results')
    Pokemons=list()
    #Get the complete Json for every Pokemon previously retrieved
    for x in PreviewPokemons:
        Pokemons.append((requests.get(x.get('url')).json()))
    return Pokemons

def insertPokemon(conn, Pokemon):
    task=[]
    task.append(Pokemon.get('name'))
    task.append(Pokemon.get('base_experience'))
    task.append(Pokemon.get('height'))
    task.append(Pokemon.get('types')[0].get('type').get('name'))
    task.append(Pokemon.get('abilities')[0].get('ability').get('name'))
    task.append(Pokemon.get('stats')[0].get('base_stat'))
    sql='''INSERT into pokemons(pokemonName,baseExperience,height,type,ability,health) VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, tuple(task))
    conn.commit()

def printPokemonDataFromJSON(Pokemon):
    print("Name " + Pokemon.get('name'))
    print("Base Experience "+ str(Pokemon.get('base_experience')))
    print("Height " + str(Pokemon.get('height')))
    print("Type " + Pokemon.get('types')[0].get('type').get('name'))
    print("Ability " + Pokemon.get('abilities')[0].get('ability').get('name'))
    print("Health " + str(Pokemon.get('stats')[0].get('base_stat')))
    print("-----------------------------------------------------------")

def downloadImages(Pokemon):
    img_url=(Pokemon.get('sprites').get('front_default'))
    save_name=".\Images\_front_default_" + Pokemon.get('name') +".jpg"
    urllib.request.urlretrieve(img_url,save_name)

def main():
    Pokemons=retrievePokemons()
    conn=create_connection(getDatabasePath())
    for x in Pokemons:
        #insertPokemon(conn,x)
        #printPokemonDataFromJSON(x)
        downloadImages(x)

if __name__ == "__main__":
    main()