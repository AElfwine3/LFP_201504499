from sys import path
from os import getcwd
import msvcrt

path.append(getcwd()+'\\Controllers')
path.append(getcwd()+'\\use-cases')

import cargar_entrada, crear_grafica, listar_pelicula

def gestion_peliculas():
    while True:
        print()
        print("1. Mostrar Peliculas ")
        print("2. Mostrar Actores")
        print("3. Regresar")
        print()
        
        subopcion = input("Ingresa una opcion: ")
        print()

        if subopcion == "1":
            print("Catalogo de peliculas disponibles:")
            print()
            listar_pelicula.listar_pelicula(True)
            print()
        elif subopcion == "2":
            listar_pelicula.listar_pelicula()
            print()
            actor = input("Selecciona una pelicula: ")
            print()
            listar_pelicula.listar_actores(actor)
            print()
        elif subopcion == "3":
            print("Regresando al menu principal")
            break
        else:
            print("Por favor elige una opcion del menu.")
        
def filtrar():
    while True:
        print()
        print("1. Filtrar por actor")
        print("2. Filtrar por año")
        print("3. Filtrar por género")
        print("4. Regresar")
        print()
        
        subopcion = input("Ingresa una opcion: ")
        print()

        if subopcion == "1":
            print("Filtrar por actor")
            print()
            actor = input("Buscar un actor: ")
            print()
            listar_pelicula.filtro_actor(actor)
        elif subopcion == "2":
            print("Filtrar por año")
            print()
            ano = input("Indica un año: ")
            print()
            listar_pelicula.filtro_ano(ano)
        elif subopcion == "3":
            print("Filtrar por genero")
            print()
            genero = input("Buscar un genero: ")
            print()
            listar_pelicula.filtro_genero(genero)
        elif subopcion == "4":
            print("Regresando al menu principal")
            break
        else:
            print("Por favor elige una opcion del menu.")


print("Lenguajes Formales y de Programacion B-")
print("Elvin Leonel Mayen Carrillo")
print("201504499")
msvcrt.getch()
while True:
    print()
    print("Elige una opcion por favor:")
    print()
    print("1. Cargar archivo de entrada: ")
    print("2. Gestionar peliculas")
    print("3. Filtrado")
    print("4. Grafica")
    print("5. Salir")
    print()

    opcion = input("Ingresa una opcion: ")
    print()

    if opcion == "1":
        print("Cargando archivo de entrada: ")
        print()
        cargar_entrada.cargar_archivo()
    elif opcion == "2":
        print("Gestiona tus Peliculas:")
        gestion_peliculas()
    elif opcion == "3":
        print("Filtros:")
        filtrar()
    elif opcion == "4":
        print("Crear Grafica")
        crear_grafica.generar_grafica()
    elif opcion == "5":
        print("Adios!")
        break
    else:
        print("Por favor elige una opcion del menu.")
