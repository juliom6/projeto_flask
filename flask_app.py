from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return '<h1>Primeiro deploy do projeto Flask da disciplina TecWeb 2C - Impacat!</h1>'

# Nossa pagina de de inicio
@app.route('/inicio')
def inicio():
	return render_template('inicio.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')