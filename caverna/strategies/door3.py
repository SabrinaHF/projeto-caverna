from strategies.base import BaseDoorStrategy


class Door3Strategy(BaseDoorStrategy):
    def execute(self, player):
        print("Porta 3 — O Enigma do Eco")
        print("A sala está vazia, exceto por uma voz que pergunta:")
        print("'Aquilo que você dá, mas nunca mantém… o que é?'")


        resposta = input("Sua resposta: ").lower().strip()


        if resposta == "palavra" or resposta == "eco":
            print("A sala treme e um portal se abre. Você acertou!")
        else:
            print("A sala se fecha para sempre. Você fracassou no enigma.")