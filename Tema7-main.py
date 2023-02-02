from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/operasbas")
def operasbas():
    return render_template("operasbas.html")


@app.route("/res",methods=['GET','POST'])
def res():
    n1 = request.form.get('txtNum1')
    n2 = request.form.get('txtNum2')
    res = int(n1)* int(n2)
    return render_template("res.html", r=res, n1=n1, n2=n2)

if __name__ == '__main__':
    app.run(debug=True, port=3000)


# http://127.0.0.1:5000