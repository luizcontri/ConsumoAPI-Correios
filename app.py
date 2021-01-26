from flask import Flask, request, render_template, make_response
import json
import requests


app = Flask(__name__)

@app.route('/')
def display_gui():
    return render_template('index.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    try:
        cep = request.form['cep']
        URL = 'https://viacep.com.br/ws/'+cep+'/json/'
        endereco = requests.request('GET', URL)
        endereco = endereco.json()
        inexistente = False
    except:
        erro = 'CEP Inexistente'
        inexistente = True
        return render_template('index.html', erro = erro, inexistente = inexistente)
    try:
        rua = endereco["logradouro"]
    except:
        erro = 'CEP Inexistente'
        inexistente = True
        return render_template('index.html', erro = erro, inexistente = inexistente)
    bairro = endereco["bairro"]
    cidade = endereco["localidade"]
    estado = endereco["uf"]
    ddd = endereco["ddd"]
    return render_template('index.html',rua = rua, bairro = bairro, cidade = cidade, estado = estado, ddd = ddd)

if __name__ == '__main__':
    app.run(debug=True)
