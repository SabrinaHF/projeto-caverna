# ─────────────────────────────────────────
# Pasta: strategies/door4.py
# ─────────────────────────────────────────


from strategies.base import BaseDoorStrategy
import random


class Door4Strategy(BaseDoorStrategy):
    def execute(self, player):
        print("Porta 4 — O Salão das Portas Falsas")
        print("Cinco portas aparecem. Apenas uma salva você.")


    correta = str(random.randint(1, 5))
    escolha = input("Escolha uma porta (1–5): ")


    if escolha == correta:
        print("A porta abre e você encontra a saída da caverna!")
    else:
        print("A porta se fecha atrás de você. Uma armadilha mortal ativa… Fim.")