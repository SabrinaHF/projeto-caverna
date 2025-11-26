# ─────────────────────────────────────────
# Arquivo: player.py
# ─────────────────────────────────────────


import random


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 0
        self.strength = 0
        self.dex = 0
        self.speed = 0
        self.luck = 0


    def roll_attributes(self):
        self.hp = random.randint(5, 15)
        self.strength = random.randint(1, 10)
        self.dex = random.randint(1, 10)
        self.speed = random.randint(1, 10)
        self.luck = random.randint(1, 10)


    def total(self):
        return self.hp + self.strength + self.dex + self.speed + self.luck


    def __str__(self):
        return (f"HP: {self.hp}, FOR: {self.strength}, DEX: {self.dex}, "
        f"VEL: {self.speed}, SORTE: {self.luck}, TOTAL: {self.total()}")