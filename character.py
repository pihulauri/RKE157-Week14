import random  # Vajalik randint() kasutamiseks


class Character:  # Baasklass kõigile tegelastele

    def __init__(self, name, weapon):  # Konstruktor, saab nime ja relva
        self.name = name  # Salvestab tegelase nime
        self.weapon = weapon  # Salvestab tegelase relva
        self.hp = len(name) + 10  # HP sõltub nime pikkusest

    def is_alive(self):  # Kontrollib, kas tegelane on elus
        return self.hp > 0  # True, kui HP on suurem kui 0

    def take_damage(self, damage):  # Vähendab tegelase HP-d
        self.hp = self.hp - damage

        if self.hp < 0:
            self.hp = 0


class Hero(Character):  # Hero pärib Character klassist

    def __init__(self, name, weapon):
        super().__init__(name, weapon)

    def attack(self, other):  # Hero ründab vastast

        damage = random.randint(0, len(self.weapon))
        # Kahju sõltub relva nime pikkusest

        if damage == 0:
            print(
                f"{self.name} attacks with {self.weapon}, "
                f"but {other.name} dodges!"
            )

        elif damage > other.hp:
            print(
                f"{self.name} attacks with {self.weapon} "
                f"for {damage}. CRITICAL HIT!"
            )

        else:
            print(
                f"{self.name} attacks with {self.weapon} "
                f"for {damage}."
            )

        other.take_damage(damage)

        print(f"{other.name} has {other.hp} HP left.")

        heal = random.randint(0, 3)
        # Hero võib pärast rünnakut taastada 0–3 HP

        if heal > 0:
            self.hp = self.hp + heal

            print(
                f"{self.name} heals for {heal} HP "
                f"and now has {self.hp} HP.\n"
            )

        else:
            print()


class Villain(Character):  # Villain pärib Character klassist

    def __init__(self, name, weapon):
        super().__init__(name, weapon)

    def attack(self, other):  # Villain ründab vastast

        damage = random.randint(0, len(self.weapon) * 2)
        # Villaini kahju võib olla suurem kui Hero oma

        if self.hp <= 5 and damage > 0:
            damage = damage + 2
            # Madala HP korral saab Villain +2 bonuskahju

        if damage == 0:
            print(
                f"{self.name} attacks with {self.weapon}, "
                f"but {other.name} dodges!"
            )

        elif damage > other.hp:
            print(
                f"{self.name} attacks with {self.weapon} "
                f"for {damage}. CRITICAL HIT!"
            )

        else:
            print(
                f"{self.name} attacks with {self.weapon} "
                f"for {damage}."
            )

        other.take_damage(damage)

        print(f"{other.name} has {other.hp} HP left.\n")