
from Inventory import Inventory
from Inventory import IronSword
from Person import Person
class Hero(Person):
    def __init__(self):
        super(Hero, self).__init__()
        self.ironSword = IronSword()
    pass

