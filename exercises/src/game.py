import random

from rps import Hand, hand_options


class Game:

    def __init__(self):
        self.ia_victories = 0
        self.user_victories = 0
    
    def results(self):
        print("\nEstos han sido los resultados:")
        print(f" - Usuario: {self.user_victories} victorias")
        print(f" - Máquina: {self.ia_victories} victorias")

    def play(self):
        while True:
            ia_hand = random.choice(hand_options)
            try:
                user_hand_kind = input("¿Qué sacas (rock, paper, scissors)?: ")
                user_hand = Hand(user_hand_kind)
                print(f"Has sacado {user_hand} y la máquina {ia_hand}")
                if user_hand == ia_hand:
                    print("¡Empate!")
                elif user_hand > ia_hand:
                    print("¡Has ganado!")
                    self.user_victories +=1
                    print(f"Llevas {self.user_victories} victorias")
                else:
                    print("¡Gana la máquina!")
                    self.ia_victories +=1
                    print(f"La máquina lleva {self.ia_victories} victorias")
            except AssertionError:
                print(f"¡{user_hand_kind} no es válido!")
                continue
            except EOFError:
                self.results()
                break
