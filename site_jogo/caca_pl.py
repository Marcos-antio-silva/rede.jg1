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
        n_colunas = tamanho_quadro*2
        posicao_linha = random.randint(0,tamanho_quadro)
        posicao_coluna = random.randint(0,tamanho_quadro)
        i = 0
        for _ in range(tamanho_quadro): #numero de linhas
            linha = []
            for _ in range(n_colunas): #numero de colunas 
                linha.append(random.choice(letras)) 
            if  i == posicao_coluna :
                linha[posicao_linha] = (self.palavra)
                linha = linha [:-(len(self.palavra)-1)]
            self.tabela.append(linha)
            i = i + 1


    def mostrar (self):    
        for linha in self.tabela :
            print ("".join(linha))
            
                                                                            
x = Caca_palavra()
x.entrada ()
x.contruir ()
x.mostrar()



