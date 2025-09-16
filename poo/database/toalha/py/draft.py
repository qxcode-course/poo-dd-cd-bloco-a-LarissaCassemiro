# Criar a classe toalha com cor, tamanho e umidade
# Iniciar cor e tamanho com parâmetros definidos e umidade = 0

class Towel:
    def __init__(self, color: str, size: str): #Constuctor 
        self.color = color #atribut 
        self.size = size #atribut
        self.wetness = 0 #atribut


        def __str__ (self):
            return f"color:{self.color}, size{self.size}, wetness{self.wetness}"

#referencia
towel = Towel("blue", "G") #object
towel_2 = Towel ("green", "P") #object 
outra = towel
towel.color = "white"
print(towel.color)
print(towel.size)
print(towel.wetness)
