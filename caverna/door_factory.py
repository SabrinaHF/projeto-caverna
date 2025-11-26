# ─────────────────────────────────────────
# Arquivo: door_factory.py
# ─────────────────────────────────────────


from strategies.door1 import Door1Strategy
from strategies.door2 import Door2Strategy
from strategies.door3 import Door3Strategy
from strategies.door4 import Door4Strategy
from strategies.door5 import Door5Strategy


class DoorFactory:

    @staticmethod
    
    def get_strategy(door):
        match door:
            case "1": return Door1Strategy()
            case "2": return Door2Strategy()
            case "3": return Door3Strategy()
            case "4": return Door4Strategy()
            case "5": return Door5Strategy()
            case _: return None