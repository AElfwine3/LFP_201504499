import os


def generar_grafica():
    with open("Grafica.dot",mode="w") as grafica:
        grafica.write("graph Datos{\n")
        grafica.write("}")
        grafica.close()
    os.system('dot -Tpng Grafica.dot -o datos.png')
    os.system("start datos.png")
