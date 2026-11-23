from utils import get_random_item
from character import Hero, Villain


# Valime failidest juhuslikud nimed ja relvad
hero_name = get_random_item("data/heroes.txt")
hero_weapon = get_random_item("data/weapons.txt")

villain_name = get_random_item("data/villains.txt")
villain_weapon = get_random_item("data/weapons.txt")


# Loome objektid
hero = Hero(hero_name, hero_weapon)
villain = Villain(villain_name, villain_weapon)


# Kuvame mängu algseisu
print("=== HERO VS VILLAIN ===")
print()

print(f"Hero: {hero.name} | HP: {hero.hp} | Weapon: {hero.weapon}")
print(f"Villain: {villain.name} | HP: {villain.hp} | Weapon: {villain.weapon}")

print()
print("=== FIGHT STARTS ===")
print()


round_number = 1  # Alustab võitlusringide lugemist


while hero.is_alive() and villain.is_alive():

    print(f"--- Round {round_number} ---")

    hero.attack(villain)

    if not villain.is_alive():
        break

    villain.attack(hero)

    if not hero.is_alive():
        break

    round_number = round_number + 1


print("=== GAME OVER ===")

if hero.is_alive():
    print("Hero saves the day.")

else:
    print("Dark Side wins.")