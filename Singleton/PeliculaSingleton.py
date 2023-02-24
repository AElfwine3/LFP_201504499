class PeliculaSingleton:

    __instance = None

    @staticmethod
    def getInstance():
        if PeliculaSingleton.__instance == None:
            PeliculaSingleton()
        return PeliculaSingleton.__instance
    
    def __init__(self):
        if PeliculaSingleton.__instance != None:
            raise Exception("Ya existe una instancia!")
        else:
            self.listaPeliculas = []
            PeliculaSingleton.__instance = self