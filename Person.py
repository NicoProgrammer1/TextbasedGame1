class Person:
    def __init__(self):
        self.name = None
        self.healthPoints = None
        self.endurance = None
        self.ageGroup = None
        self.inventory = []
        self.inventorySize = 10

    def set_agegroup(self, ageGroup):
        self.ageGroup = ageGroup
        if ageGroup == "wise":
            self.endurance = 40
            self.healthPoints = 60
        elif ageGroup == "young":
            self.endurance = 50
            self.healthPoints = 50

    def getObject(self, object):
        if len(self.inventory >= self.inventorySize):
            print("sorry your inventory is full")
        else:
            self.inventory.append(object)

    def attack(self,otherPerson):
        otherPerson.healthPoints -= 5
        if otherPerson.healthPoints <= 0:
            print("You killed your Foe")
        else:
            print("your foe now has " + str(otherPerson.healthPoints) + " HealthPoints!")
            #pass