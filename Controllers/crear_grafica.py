import os
from sys import path


path.append(os.getcwd()+'\\Singleton')

import PeliculaSingleton

peliculas = PeliculaSingleton.PeliculaSingleton.getInstance().listaPeliculas


def generar_grafica():
    with open("Grafica.dot",mode="w") as grafica:
        grafica.write('digraph Peliculas{\n')
        grafica.write('fontname="Helvetica,Arial,sans-serif"\n')
        grafica.write('node [fontname="Helvetica,Arial,sans-serif"]\n')
        grafica.write('subgraph cluster {\n')
        grafica.write('graph [style="invis"]\n')
        grafica.write('subgraph cluster_pelis {\n')
        grafica.write('graph [style="invis"]\n')
        for indice, pelicula in enumerate(peliculas):
            grafica.write('node [fillcolor="yellow:magenta" style=filled gradientangle=270 shape="record"] subgraph structs {\n')
            grafica.write(f'struct{indice} [label="{{ {pelicula["nombre"]} | {{ {pelicula["ano"]} | {pelicula["genero"]} }} }}"]\n')
            grafica.write('};\n')
        grafica.write('}\n')
        grafica.write('subgraph cluster_actores {\n')
        grafica.write('graph [style="invis"]\n')
        for pelicula in peliculas:
            for actor in pelicula['actores']:
                grafica.write(f'node [fillcolor="yellow:green" style=filled gradientangle=270] "{actor}";\n')
        grafica.write('}\n')
        grafica.write('}\n')

        for indice, pelicula in enumerate(peliculas):
            for actor in pelicula['actores']:
                grafica.write(f'struct{indice} -> "{actor}";\n')

        grafica.write('}\n')
        grafica.close()
    os.system('dot -Tpng Grafica.dot -o datos.png')
    os.system("start datos.png")
