#Objetivo dessa atividade é implementar um animal que passa pelas diversas fases de crescimento até a morte.

#- Descrição
# - O animal tem uma espécie `species`, um estágio `age` de vida e um barulho `sound` que ele faz.
# - O construtor do animal
#    - Recebe a espécie e o barulho e inicia o estágio com 0. 
#  - O toString do animal deve retornar a representação do animal no formato
#    - `{species}:{age}:{sound}`.
#  - Os estágios pelos quais o animal passa são:
#    - 0: Filhote
#    - 1: Criança
#    - 2: Adulto
#    - 3: Idoso
#    - 4: Morto
# - Ao envelhecer no método `ageBy`, o animal avança estágios na sua vida de acordo com o parâmetro `increment`.
#    - Ao morrer ou tentar envelhecer após a morte do aninal, deve ser exibida a mensagem de aviso:
#      - `warning: {species} morreu`.
#      - Como essa é uma mensagem de erro, você pode imprimir diretamente no método `ageBy`.
#  - Ao fazer barulho, o animal emite o som característico da sua espécie, com as seguintes restrições:
#    - Se for filhote, emite um "---".
#    - Se estiver morto, emite um "RIP".
#    - Como não são mensagens de erro, o barulho do animal deve ser retornado no método `makeSound` e impresso na `main`.

## Guide

# - Implemente a sua classe se orientando pela descrição, pelo UML(se houver) e pelos testes cadastrados.
# - Começe analisando os testes e entendendo tudo que seu código precisa fazer.
# - Começe analisando os testes e entendendo tudo que seu código precisa fazer.
# - Começe analisando os testes e entendendo tudo que seu código precisa fazer.
# - Começe analisando os testes e entendendo tudo que seu código precisa fazer.
# - Depois que tiver uma ideia do que vai implementar, se deixe guiar pelos testes, implementando apenas o que é pedido para passar em cada teste.
# - Passe para o próximo teste até implementar tudo que é pedido.

class Animal:
    def __init__(self, species:str, sound: str):
        self.species = species
        self.sound = sound
        self.age: str = 0

    def noise(self):
        if self.age == 0:
            print("---")

        elif self.age == 4:
            print("RIP")
        else:
            print(self.sound)

    def grow(self, limit):
        self.age += limit
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")


    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"

def main():
    animal = Animal (" ", " ")
    while True:
        line: str = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break

        elif args[0] == "init":
            species = args [1]
            sound = args [2]
            animal = Animal(species, sound)

        elif args[0] == "show":
            print (animal)

        elif args[0]== "grow":
                limit: int = int(args[1])
                animal.grow(limit)
        elif args[0]== "noise":
            animal.noise()
    
            
main()

        





  






