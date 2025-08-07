from flask import Flask, render_template, send_file
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__, template_folder='templates')

# Dados da empresa
empresa = {
    "nome": "Empresa Exemplo S/A",
    "cnpj": "12.345.678/0001-99",
    "endereco": "Rua Exemplo, 123 - Cidade/UF"
}

# 🔁 Função centralizada de dados
def criar_dados():
    dados = {
        "Produto": ["A", "B", "C", "D", "E", "F"],
        "Vendas":  [100, 150, 80, 120, 90, 60]
    }
    return pd.DataFrame(dados)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Página do relatório (HTML)
@app.route('/relatorio')
def relatorio():
    df = criar_dados()
    graph_01 = Class_Graph(data, data_subtitle, description, title)

# Geração do relatório em PDF
@app.route('/gerar-relatorio')
def gerar_relatorio():
    df = criar_dados()

    # Criar gráfico    
    graph_01 = Class_Graph(data, data_subtitle, description, title)

    # Gerar HTML e PDF
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('relatorio.html')
    html_renderizado = template.render(dados=df.to_html(index=False), empresa=empresa)
    HTML(string=html_renderizado, base_url=os.getcwd()).write_pdf("relatorio.pdf")

    return send_file("relatorio.pdf", as_attachment=True)

# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True)
