from flask import Flask

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'Primeiro deploy do projeto Flask da disciplina TecWeb - Impacat!'

