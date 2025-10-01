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