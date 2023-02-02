from flask import Flask,render_template
app = Flask(__name__)

@app.route("/datos")
def datos():
    nombre = 'juan'
    lis = ['uno','dos','tres','cuatro']
    return render_template("datos.html",nombre=nombre,lista=lis)

if __name__ == '__main__':
    app.run(debug=True, port=3000)


# http://127.0.0.1:5000