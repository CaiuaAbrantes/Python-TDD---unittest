import requests #type: ignore

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False


    def obter_todos_dados(self):
        resposta = requests.get('')

        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'
        
        
        else:
            self.dados_obtidos = False
            return 'ERRO 404'