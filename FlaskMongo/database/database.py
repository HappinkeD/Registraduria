from pymongo import MongoClient
import json
import certifi

ca = certifi.where()

####################################
#Cargar el archivo de configuracion#
####################################
def loadConfigFile():
    with open('database/config.json') as f:
        data = json.load(f)
    return data

####################################
#        Funcion de conexion       #
####################################
def dbConnection ():
    dataConfig = loadConfigFile()
    try:
        #Conexion atlas#
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], tlsCAFile = ca)
        #conexion local#
        #client = MongoClient(dataConfig['MONGO_URI_LOCAL'], dataConfig['LOCAL_PORT'])
        db = client["bd-votaciones"]
    except ConnectionError:
        print("Error de conexion con la db")
    return db 