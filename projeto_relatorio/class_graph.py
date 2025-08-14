from matplotlib import pyplot as plt
import os

class Class_Graph():
    def __init__(self, data, data_subtitle, description, title):
        self.data = data
        self.data_subtitle = data_subtitle
        self.description = description
        self.title = title
    def graph_pie(self):
        plt.figure(figsize=(7, 7))
        plt.pie(self.data, labels= self.data_subtitle , autopct='%.2f')
        plt.xlabel(self.description)
        plt.title(self.title)
        path_graph = os.path.join("graph_results","graph_pie_results")
        plt.savefig(path_graph)
        plt.close()

class Class_Graph_column():
        def __init__(self, data, data_subtitle, title):
            self.data = data
            self.data_subtitle = data_subtitle
            self.title = title
        def graph_column(self):
            plt.figure(figsize=(7,7))
            plt.bar(self.data,self.data_subtitle)
            plt.title(self.title)
            path_graph = os.path.join("graph_results", "grapie_column_results")
            plt.savefig(path_graph)
            plt.close()

#data = [511, 223, 423, 54]
#data_subtitle = ["a", "b" ,"c" ,"d"]
#description = "Vendas"
#title = "Title"
#graph_name = "ronaldo"

#graph_01 = Class_Graph(data, data_subtitle, description, title)
#graph_01.Graph_Pie()

