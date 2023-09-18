
def SelectOptions(userInput):
     if userInput.upper() == 'A':
          print("You decided to head towards Mars? Would you like to head into it?")
          LifeOnMars = input("Enter A or B. A) Head into Mars B) Head back from start")
          if LifeOnMars == 'A':
               return "It seems like there is no life on Mars due to the lack of atmosphere to maintain water and ultraviolet radiation. Let's try finding a better place to live."
          elif LifeOnMars == 'B':
               return "You decided to head towards Mars? Would you like to head into it?"
     elif userInput.upper() == 'B':
          EmptySpace = input("Enter A or B. A) Investigate further B) Head back from start")
          if EmptySpace == 'A':
               print("Wow, you disovered a new Earth-like planet!")
               NewEarth = input("Enter A or B. A) Head into the planet B) Head back from start")
               if NewEarth == 'A':
                    return "This is definitely suitable for human life! Good job on finding it"
               elif NewEarth == 'B':
                    return "You decided to head towards Mars? Would you like to head into it?"
          elif EmptySpace == 'B':
               return "You decided to head towards Mars? Would you like to head into it?"
     else: 
          print("You entered something wrong - refresh and try again!")

def main():
     print("You are off on your space mission! You've just taken off and left the Earth's atmosphere. Your team is ready for an adventure of a lifetime! The goal of this mission is to try to find life in the universe. As the captain - you now have an important choice. Where do you go?")
     userInput = input("Enter A or B. A) Head towards Mars B) Head into empty space")
     print(SelectOptions(userInput))

if __name__ == "__main__":
    main()
