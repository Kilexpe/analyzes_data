import json
with open("vendas_exemplo.json") as file:
    file_json = json.load(file)
#exemplo: (data[b]['valor'])

class Data_Payment_Method:

    def __init__(self, file_json):
        self.file_json = file_json

    # Essa função Contabiliza as formas de pagamento utilizadas (somente as selecionadas no if) .
    def Verify_Data(self):
        self.cont_CC = 0
        self.cont_CD = 0
        self.cont_P = 0
        self.cont_B = 0
        self.cont_D = 0
        index = 0
        for c in self.file_json:
            if self.file_json[index]['forma_pagamento'] == 'Cartao de Credito':
                self.cont_CC = self.cont_CC + 1
            if self.file_json[index]['forma_pagamento'] == 'Cartao de Debito':
                self.cont_CD = self.cont_CD + 1
            if self.file_json[index]['forma_pagamento'] == 'Pix':
                self.cont_P = self.cont_P + 1
            if self.file_json[index]['forma_pagamento'] == 'Boleto':
                self.cont_B = self.cont_B + 1
            if self.file_json[index]['forma_pagamento'] == 'Dinheiro':
                self.cont_D = self.cont_D + 1
            index = index + 1
        cont_list = [self.cont_CC, self.cont_CD, self.cont_P, self.cont_B, self.cont_D]
        return(cont_list)
    def Data_subtitles(self):
        data_pie_subtitle = ("Cartão de Credito", "Cartão de Debito", "Pix", "Boleto", "Dinheiro")
        return(data_pie_subtitle)
