from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def __init__(self, name="Меч"):
        self.name = name
    def attack(self):
        return "удара мечом. Но не причинил вреда."


class Bow(Weapon):
    def __init__(self, name="Лук"):
        self.name = name
    def attack(self):
        return "выстрела из лука. Но не причинил вреда."

class Lutaya_Herobora(Weapon):
    def __init__(self, name="Лютая Херобора"):
        self.name = name
    def attack(self):
        return "волшебного нагибатора. Весь мир в труху."


class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"Боец сменил оружие на {weapon.name}")

    def fight(self, monster):
        print(f"Боец атакует {monster.name} с помощью {self.weapon.attack()}")


class Monster:
    def __init__(self, name):
        self.name = name


sword = Sword()
bow = Bow()

fighter = Fighter(sword)
monster = Monster("Гоблин")

fighter.fight(monster)
fighter.change_weapon(bow)
fighter.fight(monster)

fighter.change_weapon(Lutaya_Herobora())
fighter.fight(monster)