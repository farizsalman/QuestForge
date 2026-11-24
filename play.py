from domain.character import Character

if __name__ =="__main__":
    hero = Character("Aria", 100, 15)
    goblin = Character("Goblin", 30, 5)
    knight = Character("Knight", 70, 10)
    orc = Character("Orc", 40, 10)


    print(hero.describe())
    print(goblin.describe())
    print(knight.describe())
    print(orc.describe())


    hero.attack(goblin)
    print(goblin.describe())


    # 3 way attack
    # attack 1
    knight.attack(orc)
    print(orc.describe())
    orc.attack(knight)
    print(knight.describe())

    # attack 2
    knight.attack(orc)
    print(orc.describe())
    orc.attack(knight)
    print(knight.describe())

    # attack 3
    knight.attack(orc)
    print(orc.describe())
    orc.attack(knight)
    print(knight.describe())

    # test heal
    orc.heal(20)
    print(orc.describe())
    knight.heal(90)
    print(knight.describe())


    # level 2 test
    hero = Character("Aria",100,15)
    hero.take_damage(150)
    print(hero.health)