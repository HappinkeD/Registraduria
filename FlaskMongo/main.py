from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS

from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorResultado import ControladorResultado

app = Flask(__name__)
cors = CORS(app)

###############################
##     Variables globales    ##
###############################
miControladorPartido = ControladorPartido()
miControladorMesa = ControladorMesa()
miControladorCandidato = ControladorCandidato()
miControladorResultado = ControladorResultado()

###############################
##      PROBAR SERVICIO      ##
###############################
@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "Server running..."
    return jsonify(json)

###############################
###    ENDPOINT PARTIDOS   ####
###############################
@app.route("/partidos", methods=["GET"])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos", methods=["POST"])
def crearPartidos():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id_partido>", methods=["GET"])
def getpartidos(id_partido):
    json = miControladorPartido.show(id_partido)
    return jsonify(json)

@app.route("/partidos/<string:id_partido>", methods=["PUT"])
def modificarPartidos(id_partido):
    data = request.get_json()
    json = miControladorPartido.update(id_partido, data)
    return jsonify(json)

@app.route("/partidos/<string:id_partido>", methods=["DELETE"])
def eliminarPartidos(id_partido):
    json = miControladorPartido.delete(id_partido)
    return jsonify(json)
###############################
###     ENDPOINT MESAS     ####
###############################
@app.route("/mesas", methods=["GET"])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas", methods=["POST"])
def crearMesas():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=["GET"])
def getmesas(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=["PUT"])
def modificarMesas(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=["DELETE"])
def eliminarMesas(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)
###############################
###  ENDPOINT CANDIDATOS   ####
###############################
@app.route("/candidatos", methods=["GET"])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos", methods=["POST"])
def crearCandidatos():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id_candidato>", methods=["GET"])
def getcandidatos(id_candidato):
    json = miControladorCandidato.show(id_candidato)
    return jsonify(json)

@app.route("/candidatos/<string:id_candidato>", methods=["PUT"])
def modificarCandidato(id_candidato):
    data = request.get_json()
    json = miControladorCandidato.update(id_candidato, data)
    return jsonify(json)

@app.route("/candidatos/<string:id_candidato>", methods=["DELETE"])
def eliminarCandidatos(id_candidato):
    json = miControladorCandidato.delete(id_candidato)
    return jsonify(json)

@app.route("/candidatos/<string:id_candidato>/partidos/<string:id_partido>", methods=["PUT"])
def asignarPartidoCandidato(id_candidato, id_partido):
    json = miControladorCandidato.asignarCandidato(id_candidato, id_partido)
    return jsonify(json)
###############################
###  ENDPOINT RESULTADOS   ####
###############################
#Obtener todos resultados 
@app.route("/resultados", methods=["GET"])
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)

#Añadir Resultado a una mesa
@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=["POST"])
def crearResultado(id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.create(data, id_mesa, id_candidato)
    return jsonify(json)

#Obtener Resultado especifico
@app.route("/resultados/<string:id>", methods=["GET"])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)

#Modificar Resultado
@app.route("/resultados/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=["PUT"])
def modificarResultado(id_resultado, id_mesa, id_candidato):
    data = {}
    json = miControladorResultado.update(id_resultado, data, id_mesa, id_candidato)
    return jsonify(json)

#Eliminar Resultado
@app.route("/resultados/<string:id>", methods=["DELETE"])
def borrarResultado(id):
    json = miControladorResultado.delete(id) 
    return jsonify(json) 

#Buscar Candidatos votados en una mesa
@app.route("/resultados/mesa/<string:id_mesa>", methods=["GET"])
def votosMesa(id_mesa):
    json = miControladorResultado.getListarCandidatoMesa(id_mesa)
    return jsonify(json)

#Buscar candidato en las mesas
@app.route("/resultados/mesas/<string:id_candidato>", methods=["GET"])
def inscritosMesa(id_candidato):
    json = miControladorResultado.getListarCandidatosInscritosEnMesa(id_candidato)
    return jsonify(json) 

#Buscar Mayor cedula
@app.route("/resultados/maxdocument", methods=["GET"])
def getMaxDocument():
    json = miControladorResultado.getMayorCedula()
    return jsonify(json)

if __name__ == "__main__":
    app.run(debug=False, port=9000)
