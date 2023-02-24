from sys import path
from os import getcwd

path.append(getcwd()+'\\Pelicula')
path.append(getcwd()+'\\Singleton')

import Pelicula
import PeliculaSingleton

class AgregarPelicula:

    def __init__(self):
        self.peliculas = PeliculaSingleton.PeliculaSingleton.getInstance().listaPeliculas
        # self.peliculas = []

    def agregar_pelicula(self, datos: dict):
        pelicula = Pelicula.Pelicula(datos['nombre'], datos['actores'], datos['ano'], datos['genero'])
        for peli in self.peliculas:
            if peli['nombre'] == pelicula.nombre:
                self.peliculas.remove(peli)
                break
        self.peliculas.append(pelicula.get_objeto_pelicula())
    
    def get_peliculas(self):
        print(self.peliculas)
        return self.peliculas
        