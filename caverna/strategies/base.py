# ─────────────────────────────────────────
# Pasta: strategies/base.py
# ─────────────────────────────────────────


class BaseDoorStrategy:
    def execute(self, player):
        raise NotImplementedError("Subclasses devem implementar execute()")