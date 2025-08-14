from flask import Flask, render_template, send_file
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import matplotlib.pyplot as plt
import os
from class_graph import Class_Graph
import json
from class_Data_Payment_Method import Data_Payment_Method

app = Flask(__name__, template_folder='templates')

# Carrega uma variável com os dados do json.
with open("vendas_exemplo.json") as file:
    data = json.load(file)

# Página inicial em Html
@app.route('/')
def index():
    return render_template('index.html')

# Página do relatório (HTML)
@app.route('/relatorio')
def relatorio():
    return render_template('relatorio.html')

if __name__ == '__main__':
    app.run(debug=True)

