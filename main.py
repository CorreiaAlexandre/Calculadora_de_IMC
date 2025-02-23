from flask import Flask, render_template, request
#Flask: A classe principal para criar a aplicação web.
#render_template: Uma função para carregar arquivos HTML (templates).
#request: Um objeto que permite acessar dados enviados pelo usuário (como os valores do formulário).

app = Flask(__name__) #Aqui uma instância da aplicação Flask. O __name__ é uma variável especial do Python que representa o nome do arquivo atual (calculadordeIMC.py). Isso ajuda o Flask a saber onde encontrar os arquivos relacionados (como a pasta templates).

@app.route("/") #Define uma rota para a URL raiz (ex.: http://127.0.0.1:5000/). Quando alguém acessa essa URL, a função index() é chamada.
def index(): #Uma função simples que retorna o conteúdo do arquivo index.html
    return render_template('index.html') #Carrega e exibe o arquivo index.html que está na pasta templates. Esse é o formulário onde o usuário insere peso e altura.

@app.route('/resultant', methods=['POST']) #Define uma rota para a URL /resultant (ex.: http://127.0.0.1:5000/resultant). O methods=['POST'] indica que essa rota só aceita requisições POST, que são enviadas quando o usuário submete o formulário.
def resultado():
    try: #Inicia um bloco de código que pode gerar erros. Aqui, tentamos converter os valores inseridos em números.
        peso = float(request.form['peso'].replace(",", ".")) #.replace(",", "."): Substitui vírgulas por pontos para que o Python entenda o número decimal (ex.: "76,8" vira "76.8").
        altura = float(request.form['altura'].replace(",", "."))
    except ValueError: #Se a conversão falhar (ex.: se o usuário digitar "abc" ou algo inválido), esse bloco é executado.
        return "Erro: Por favor, insira valores numéricos válidos (use vírgula ou ponto)." #Retorna uma mensagem de erro simples como texto no navegador, avisando que os valores não são numéricos válidos.

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
    #render_template('resultado.html', ...): Carrega o arquivo resultado.html e passa variáveis para ele.
    #imc=round(imc, 2): Arredonda o valor do IMC para 2 casas decimais (ex.: 24.489795 vira 24.49).
    #classificacao=classificacao: Passa a string de classificação (ex.: "Normal") para o template.
    #Essas variáveis (imc e classificacao) podem ser usadas no resultado.html com {{ imc }} e {{ classificacao }}.

if __name__ == '__main__':
    app.run(debug=True)
    #if __name__ == '__main__':: Verifica se o arquivo está sendo executado diretamente (não importado como módulo). Isso é uma prática comum em Python.
    #app.run(debug=True): Inicia o servidor web do Flask.
    #debug=True: Ativa o modo de depuração, que recarrega o servidor automaticamente ao alterar o código e mostra erros detalhados no navegador.
