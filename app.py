from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/portada')
def portada():
    return render_template('portada.html')

@app.route('/que-es')
def que_es():
    return render_template('que_es.html')

@app.route('/impacto-comunidad')
def impacto():
    return render_template('impacto.html')

@app.route('/soluciones')
def soluciones():
    return render_template('soluciones.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

if __name__ == '__main__':
    app.run(debug=True)