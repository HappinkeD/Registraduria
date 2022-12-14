from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido

class ControladorPartido():
    #Constructor
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
    #Devuelve todos los documentos de la coleccion 
    def index(self):
        return self.repositorioPartido.finAll()
    #Crea documentos
    def create (self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)
    #Muestra documento
    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__
    #Actualizar un documento 
    def update(self, id, infoPartido):
        PartidoActual = Partido(self.repositorioPartido.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(PartidoActual)
    #Borra un documento
    def delete(self, id):
        return self.repositorioPartido.delete(id)