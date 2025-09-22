class Towel:
    def __init__(self, color: str, size: str): 
        self.color = color 
        self.size = size 
        self.wetness: int =  0

def dry(self, amount: int) -> None:
    self.wetness += amount
    if self.wetness >= self.getMaxWetness():
        print("toalha encharcada")
        self.wetness = self.getMaxWetness()

def isDry(self) -> bool:
    return self.wetness == 0

def wringOut(self) -> None:
    self.wetness = 0

    
def getMaxWetness (self) -> int: 
    if self.size == "P":
        return 10 
    if self.size == "M":
        return 20
    if self.size == "G":
        return 30

def __str__ (self):
    return f"color:{self.color}, size{self.size}, wetness{self.wetness}"

def main():
    toalha = Towel("", "")
    while True:
        line:str = input()
        line:list[str] =line.split(" ")

        if args[0] == "end":
            break 
        elif args [0] == "new":
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0] == "show"
            print(toalha)
        elif args[0]== "dry":
            amount: int = (args[1])
            toalha.dry(amount)
        else:
            print:("fail:comando inválido")

main()



doguito = Towel("suja", "M")
print(doguito.color)
print(doguito.size)
print(doguito.wetness)
print(str(doguito)+ "está velha")