from sys import path
from os import getcwd

path.append(getcwd()+'\\Singleton')

import PeliculaSingleton

peliculas = PeliculaSingleton.PeliculaSingleton.getInstance().listaPeliculas

def listar_pelicula(todo = False):
    for indice, pelicula in enumerate(peliculas):
        if todo:
            print(f"{indice+1}: {pelicula['nombre']}, {pelicula['ano']}, {pelicula['genero']}")
        else:
            print(f"{indice+1}: {pelicula['nombre']}")

def listar_actores(nombre):
    nombre = nombre.replace(' ', '').lower()
    for pelicula in peliculas:
        if pelicula['nombre'].replace(' ', '').lower() == nombre:
            print(f"Actores de {pelicula['nombre']}:")
            for actor in pelicula['actores']:
                print(actor, end=', ')

def filtro_actor(nombre_actor):
    nombre_actor = nombre_actor.replace(' ', '').lower()
    for pelicula in peliculas:
        for actor in pelicula['actores']:
            if actor.replace(' ', '').lower() == nombre_actor:
                print(f"{pelicula['nombre']}, {pelicula['ano']}, {pelicula['genero']}")

def filtro_ano(ano):
    ano = ano.replace(' ', '')
    for pelicula in peliculas:
        if pelicula['ano'].replace(' ', '') == ano:
            print(f"{pelicula['nombre']}, {pelicula['genero']}")

def filtro_genero(genero):
    genero = genero.replace(' ', '').lower()
    for pelicula in peliculas:
        if pelicula['genero'].replace(' ', '').lower() == genero:
            print(f"{pelicula['nombre']}, {pelicula['ano']}")