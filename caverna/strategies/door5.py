from strategies.base import BaseDoorStrategy


class Door5Strategy(BaseDoorStrategy):
    def execute(self, player):
        print("Porta 5 — O Guardião da Luz")
        print("Um ser luminoso avalia sua alma e seus atributos…")


        if player.total() >= 60:
            print("Sua força interior é suficiente. Você é liberado com bênçãos!")
        else:
            print("Você ainda não está pronto. Volte quando for mais forte.")