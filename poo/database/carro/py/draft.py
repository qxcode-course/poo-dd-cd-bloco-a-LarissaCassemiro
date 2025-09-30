#Nesta atividade, vamos implementar um carro ecológico. Ele deve ser capaz de embarcar e desembarcar pessoas, abastecer e andar.

#- O carro deve ser inicializado com o tanque vazio, sem ninguém dentro e com 0 quilômetros percorridos.
# Suporta até 2 pessoas e até 100 litros de combustível.

#- Construtor do Carro
#  - `pass`: 0 passageiros. 
#  - `km`: 0 quilômetros percorridos.
#  - `passMax`: Máximo de 2 pessoas.
#  - `gas`: 0 litros de gasolina.
#  - `gasMax`: Máximo de 100 litros de gasolina.
#  - Mostrar `$show`
# - Imprime a chamada do método `toString` do carro.
#  - `toString` - Retorna uma string com o estado atual do carro no formato:
#  - `"pass:{pass}, gas:{gas}, km:{km}"`.
# - Entrar `$enter`
 # - Embarca uma pessoa por vez, mas não além do máximo.
#  - Se o carro estiver lotado, emite a mensagem de erro.
#    - `fail: limite de pessoas atingido`.
#- Sair `$leave`
#  - Desembarca uma pessoa por vez.
#  - Se não houver ninguém no carro, emite a mensagem de erro.
#    - `fail: nao ha ninguem no carro`.
#- Abastecer certa quantidade `$fuel increment`
#  - Abastece o tanque com a quantidade de litros de combustível passada.
#  - Caso tente abastecer acima do limite, descarta o valor excedente.
#- Dirigir certa distância `$drive distance`
#  - Para dirigir, o carro consome combustível e aumenta a quilometragem.
#  - Só pode dirigir se houver combustível e se houver alguém no carro.
#  - Caso não haja ninguém no carro, emite a mensagem de erro.
#    - `fail: não há ninguém no carro`
#  - Caso não haja combustível, emite a mensagem de erro.
#    - `fail: tanque vazio`
#  - Caso não exista combustível suficiente para completar a viagem inteira, dirija o máximo possível e emite uma mensagem indicando quanto foi percorrido
#    - `fail: tanque vazio após andar {distancia} km`.


class Carro:
    def __init__(self):
        self.passageiros = 0          
        self.passMax = 2        
        self.gas = 0            
        self.gasMax = 100       
        self.km = 0             

    def enter(self):
        if self.passageiros < self.passMax:
            self.passageiros += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.passageiros > 0:
            self.passageiros -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def fuel(self, qtd: int):
        self.gas += qtd
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, dist: int):
        if self.passageiros == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return

        if dist <= self.gas:
            self.gas -= dist
            self.km += dist
        else:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas
            self.gas = 0

    def __str__(self):
        return f"pass: {self.passageiros}, gas: {self.gas}, km: {self.km}"


def main():
    carro = Carro()
    while True:
        line: str = input()
        args:list[str] = line.split(" ")
        print("$" + line)

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            carro.fuel(int(args[1]))
        elif args[0] == "drive":
            carro.drive(int(args[1]))
        else:
            print("fail: comando invalido")


main()
