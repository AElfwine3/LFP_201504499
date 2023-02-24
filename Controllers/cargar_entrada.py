import tkinter as tk
from tkinter import filedialog
from sys import path
from os import getcwd

path.append(getcwd()+'\\use-cases')

import agregar_pelicula


def cargar_archivo():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    if not file_path.endswith('.lfp'):
        print('No es un archivo valido')
    else:
        crear_agregar_pelicula = agregar_pelicula.AgregarPelicula()
        with open(file_path, 'r') as file:
            for line in file:
                datos = [dato.strip() for dato in line.rstrip().split(';')]
                pelicula = {
                    'nombre': datos[0],
                    'actores': datos[1].split(','),
                    'ano': datos[2],
                    'genero': datos[3]
                }
                crear_agregar_pelicula.agregar_pelicula(pelicula)
    print('Archivo cargado con exito!!!')