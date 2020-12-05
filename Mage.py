
from Person import Person

class Mage(Person):
    def __init__(self):
        super(Mage, self).__init__()
        self.healthPoints = 90

    def magicSpell(self):
        print("Wingardian leviosa")
    pass