# ─────────────────────────────────────────
# Arquivo: main.py
# ─────────────────────────────────────────

import player
import door_factory

def main():
    
    print(""" ===============================
    BEM-VINDO À CAVERNA
    ===============================
    Cinco portas. Cinco destinos.
    Sua sorte e seus atributos decidirão.
    """)


    name = input("Digite seu nome, aventureiro(a): ")


    jogador = player.Player(name)
    jogador.roll_attributes()


    print(f"Seus atributos iniciais:{jogador}")


    door = input("Escolha uma porta (1–5): ")


    strategy = door_factory.DoorFactory.get_strategy(door)


    if strategy:
        strategy.execute(jogador)
    else:
        print("Porta inválida.")




if __name__ == "__main__":
    main()