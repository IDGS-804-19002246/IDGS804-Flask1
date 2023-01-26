from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return 'Hola perros >:D'

if __name__ == '__main__':
    #Colocando 'debuj=True' se puede actualizar la pagina sin detener el servidor
    #Colocando 'port=3000' se cambia el puerto en el que corre la pagina, por defecto es 5000
    app.run(debug=True)
