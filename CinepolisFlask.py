from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/cine/",methods=['GET','POST'])
def cine():
    if request.method=='POST':        
        nom = request.form.get('nom')
        can = int(request.form.get('can'))
        tag = request.form.get('tar')
        Nbol = int(request.form.get('Nbol'))
        fin = Nbol * 12
        
        if Nbol == 3 or Nbol == 4 or Nbol == 5:
            fin = fin * 0.9
        if Nbol > 5:
            fin = fin * 0.85

        if tag == 'S':
            fin = fin * 0.9
        
        if Nbol > (can*7):
            fin = '0'
            men = 'Una persona solo puede comprar maximo 7 boletos'
        else:
            men = 'ok'
        return render_template("cine.html",v = fin, m = men)

    else:
        can = 0
        men = 'ok'
        return render_template("cine.html",v = can, m = men)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


# http://127.0.0.1:5000