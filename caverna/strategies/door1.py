from strategies.base import BaseDoorStrategy
import random


class Door1Strategy(BaseDoorStrategy):
    
    def execute(self, player):
        print("Porta 1 — A Caverna dos Goblins")
        print("Você entra e é cercado por pequenos goblins armados!")


        escolha = input("Lutar (L) ou Fugir (F)? ").lower()


        if escolha == "l":
            dificuldade = random.randint(5, 15)
            print(f"Força necessária: {dificuldade}")
            if player.strength >= dificuldade:
                print("Você derrotou os goblins! Vitória!")
            else:
                print("Você foi sobrecarregado pelos goblins... Fim de aventura.")
        elif escolha == "f":
            dificuldade = random.randint(5, 15)
            print(f"Velocidade necessária: {dificuldade}")
            if player.speed >= dificuldade:
                print("Você escapou ileso!")
            else:
                print("Os goblins te alcançaram. Game over.")
        else:
            print("Você hesitou e os goblins atacaram. Game over.")