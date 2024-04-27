import random

class Caca_palavra:
    def __init__ (self,palavra='',dificuldade=0):
        self.palavra = palavra
        self.dificuldade = dificuldade

    def entrada (self):
        self.palavra = input('qual a palavra:')
        self.tamanho = int(input('Dificuladade de 1 a 3: '))

    def analise (self): 
        if self.tamanho == 1 :
            tamanho_quadro = len(self.palavra)*2
        elif self.tamanho == 2 :
            tamanho_quadro = len(self.palavra)*3
        else :
            tamanho_quadro = len(self.palavra)*4

        return(tamanho_quadro)

    def contruir (self):
        self.tabela = []
        letras = 'abcdefghijklmnopqrstuvxwyz'
        tamanho_quadro = self.analise()
        n_colunas = tamanho_quadro*3
        i = 0
        for _ in range(tamanho_quadro): #linha
            linha = []
            for _ in range(n_colunas): #coluna 
                linha.append(random.choice(letras)) 
            if  i == 1:
                linha[2] = (self.palavra)
                linha = linha [:-2]
            self.tabela.append(linha)
            i = i + 1

    def mostrar (self):    
        for linha in self.tabela :
            print ("".join(linha))
            
                                                                            
x = Caca_palavra()
x.entrada ()
x.contruir ()
x.mostrar()


