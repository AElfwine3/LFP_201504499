class Pelicula:
    def __init__(self, nombre: str, actores: list, ano: int, genero: str):
        self.nombre = nombre
        self.actores = actores
        self.ano = ano
        self.genero = genero
    
    def get_objeto_pelicula(self):
        return {
            'nombre': self.nombre,
            'actores': self.actores,
            'ano': self.ano,
            'genero': self.genero
        }