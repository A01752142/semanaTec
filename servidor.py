from crypt import methods
from distutils.log import debug, set_verbosity
from fileinput import filename
from unicodedata import name
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from joblib import load
import numpy as np
import os

#Cargar el modelo
dt = load('modelo.joblib')


#Generar el servidor en flask (Backend)

servidorweb =  Flask(__name__)

#Anotación 

@servidorweb.route("/test",methods = ['GET'])
def formulario():
    return render_template('pagina.html')

#Procesar datos a través del form
@servidorweb.route('/modeloIA',methods=["POST"])
def modeloForm():
    #Pricesar los datos de entrada
    contenido = request.form
    print(contenido)
    datosEntrada = np.array([9.00000, 0.40000,0.41000,2.00000,0.05800,15.00000,40.00000,0.99414,contenido['pH'],contenido['sulfatos'],contenido['alcohol']])
    #Utilizar el modelo 
    resultado = dt.predict(datosEntrada.reshape(1,-1))
    return jsonify({"Resultado":str(resultado[0])})

#Procesar datos de un arvhico 
@servidorweb.route("/modeloFile",methods=['POST'])
def modeloFile():
    f = request.files['file']
    filename=secure_filename(f.filename)
    path= os.path.join(os.getcwd(),filename)
    f.save(path)
    file = open(path,'r')
    for line in file:
        print(line)
    return jsonify({"Resultado":"datos recibidos"})


@servidorweb.route('/modelo',methods=["POST"])
def model():
    #Procesa datos de entrada(request)
    contenido= request.json
    print(contenido)
    return jsonify({"Resultado":"datos recibidos"})

if __name__ == '__main__':
    servidorweb.run(debug = False, host = '0.0.0.0',port = '8080')