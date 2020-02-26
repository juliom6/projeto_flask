from flask import Flask

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return '<h1>Primeiro deploy do projeto Flask da disciplina TecWeb 2C - Impacat!</h1>'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')