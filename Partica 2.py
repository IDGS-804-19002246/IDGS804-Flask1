from flask import Flask
from flask import request
import math

app = Flask(__name__)

@app.route("/P2/",methods=['GET','POST'])
def suma():
    if request.method=='POST':
        X1 = int(request.form.get('X1'))
        X2 = int(request.form.get('X2'))

        Y1 = int(request.form.get('Y1'))
        Y2 = int(request.form.get('Y2'))
        
        H = int(X2 - X1)
        V = int(Y2 - Y1)
        dis = math.sqrt( H**2 + V**2 )

        return '<h2>La distancia es de:{}</h2>'.format(str(dis))
    else:
        return '''
            <form action='/P2/' method='POST'>

            <label>Dame las coordenadas del 1° punto</label>
            <br>
            <label>X</label>
            <input type='text' name='X1'/>

            <label>Y</label>
            <input type='text' name='Y1'/>
            <br><br>

            <label>Dame las coordenadas del 2° punto</label>
            <br>
            <label>X</label>
            <input type='text' name='X2'/>
            <label>Y</label>
            <input type='text' name='Y2'/>

            <input type='submit' value='Calcular distancia'/>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)
