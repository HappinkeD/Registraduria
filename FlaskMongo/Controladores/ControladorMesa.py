from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():
    #Constructor
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
    #Devuelve todos los documentos de la coleccion 
    def index(self):
        return self.repositorioMesa.finAll()
    #Crea documentos
    def create (self, infoMesa):
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)
    #Muestra documento
    def show(self, id):
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__
    #Actualizar un documento 
    def update(self, id, infoMesa):
        MesaActual = Mesa(self.repositorioMesa.findById(id))
        MesaActual.numero = infoMesa["numero"]
        MesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(MesaActual)
    #Borra un documento
    def delete(self, id):
        return self.repositorioMesa.delete(id)