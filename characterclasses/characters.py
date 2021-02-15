

class Character:
    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def loseHp(self, loss):
        self.hp -= loss

    def gainHp(self, gain):
        self.hp += gain

    def getHp(self):
        return self.hp

    def printHp(self):
        print(self.hp)
        
#defining how much stats each class has
        
class Mage(Character):
    mageStats = {
        'hp': 110,
        'defence': 110,
        'attack': 80,
        
    }
        
class Cavalry(Character):
    cavalryStats = {
        'hp': 110,
        'defence': 80,
        'attack': 110,
        
    }
        
class Archer(Character):
    archerStats = {
        'hp': 90,
        'defence': 100,
        'aatack': 110,
    }

class Warrior(Character):
    stats = {
        'hp': 100,
        'defence': 110,
        'attack': 90,
        
    }
    def createWarrior(self):
        newWarrior = CharacterManager.createCharacter
    

class CharacterManager:
    def createCharacter(self, hp, attack, defence):
        newCharacter = Character(hp=hp, attack=attack, defence=defence)
        return newCharacter

randomCharacter = CharacterManager().createCharacter(hp=10, defence=12, attack=8)
randomCharacter.printHp()
    


    

