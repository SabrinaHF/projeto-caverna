# ─────────────────────────────────────────
# Pasta: strategies/door2.py
# ─────────────────────────────────────────


from strategies.base import BaseDoorStrategy
import random


class Door2Strategy(BaseDoorStrategy):
    def execute(self, player):
        print("Porta 2 — O Salão da Serpente")
        print("Uma cobra gigante surge das sombras!")


        dificuldade = random.randint(8, 18)
        print(f"Teste de Destreza necessário: {dificuldade}")


        if player.dex >= dificuldade:
            print("Você esquiva perfeitamente e encontra um tesouro escondido!")
        else:
            print("A serpente te atinge com sua cauda. Você cai desacordado.")