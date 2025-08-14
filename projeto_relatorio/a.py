from class_graph import Class_Graph
from class_Data_Payment_Method import Data_Payment_Method
import json
with open("vendas_exemplo.json") as file:
    file_json = json.load(file)
a = Data_Payment_Method(file_json)
b = a.Verify_Data()
data_pie_subtitle = ("Cartão de Credito","Cartão de Debito","Pix","Boleto","Dinheiro")
print(b)

graph_01 = Class_Graph(b, data_pie_subtitle, 'Mais usadas', 'Formas de pagamento')
graph_01.graph_pie()
