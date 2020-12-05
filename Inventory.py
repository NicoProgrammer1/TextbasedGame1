
class Inventory:
    def __init__(self):
        return


class IronSword:
    def __init__(self):
        self.itemName = "IronSword"
        self.attack = None
        return

    def swordattack_move(self, attack):
        p1.Hp = p1.Hp - 1