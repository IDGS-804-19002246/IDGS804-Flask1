from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/suma/",methods=['GET','POST'])
def suma():
    if request.method=='POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        res = 0
        if(request.form.get('op') == 'S'):
            res = num1 + num2
        if(request.form.get('op') == 'R'):
            res = num1 - num2
        if(request.form.get('op') == 'M'):
            res = num1 * num2
        if(request.form.get('op') == 'D'):
            res = num1 / num2

        return '<h2>El resultado es:{}</h2>'.format(str(int(res)))
    else:
        return '''
            <form action='/suma' method='POST'>

            <input type='radio' name='op' value='S' required checked    > Suma <br>
            <input type='radio' name='op' value='R'> Resta <br>
            <input type='radio' name='op' value='M'> Multiplicar <br>
            <input type='radio' name='op' value='D'> Divicion <br>

            <label>N1: </label>
            <input type='text' name='num1'/>
            <br><br>

            <label>N2: </label>
            <input type='text' name='num2'/>
            <br><br>

            <input type='submit' value='Calcular'/>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)
