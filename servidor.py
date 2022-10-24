from crypt import methods
from distutils.log import debug, set_verbosity
from unicodedata import name
from flask import Flask, request, jsonify, render_template


#Generar el servidor en flask (Backend)

servidorweb =  Flask(__name__)

#Anotación 

@servidorweb.route("/test",methods = ['GET'])
def formulario():
    return render_template('pagina.html')

if __name__ == '__main__':
    servidorweb.run(debug = False, host = '0.0.0.0',port = '8080')