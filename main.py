from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/resultant', methods=['POST'])
def resultado():
    peso = float(request.form['peso'].replace(",", "."))  # Corrigido aqui
    altura = float(request.form['altura'].replace(",", "."))

    imc = peso / altura ** 2

    if imc < 18.5:
        classificacao = 'Magreza'
    elif imc < 24.9:
        classificacao = 'Normal'
    elif imc < 29.9:
        classificacao = 'Sobrepeso'
    elif imc < 34.9:
        classificacao = 'Obesidade grau I'
    elif imc < 39.9:
        classificacao = 'Obesidade grau II'
    else:
        classificacao = 'Obesidade grau III'

    return render_template('resultado.html', imc=round(imc, 2), classificacao=classificacao)

if __name__ == '__main__':
    app.run(debug=True)
