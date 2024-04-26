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
        tabela = []
        letras = 'abcdefghijklmnopqrstuvxwyz'
        tamanho_quadro = self.analise()
        posicao = random.randint(0, len(self.palavra) - 1)
        i = 0
        n = len(self.palavra) - posicao
        for _ in range(tamanho_quadro#linha#
                       ):
            linha = []
            for _ in range(tamanho_quadro#coluna#
                           ):
                linha.append(random.choice(letras)) 
                if i == posicao:
                    linha.append(self.palavra)
                i = i +1
            tabela.append(linha)
        for linha in tabela :
            print ("".join(linha))
            
                                                                            
x = Caca_palavra()
x.entrada ()
x.contruir ()


