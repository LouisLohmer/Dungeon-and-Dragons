import random

def dungeonAndDragons():
    #Nutzer zu Beginn begrüßen
    print("Willkommen bei Dungeon&Dragons!")
    print("Made by LonelyStreetracer with ♥")
    print("")

    #Klassen für Spielcharactere erstellen
    #Vaterklasse Charakter
    class character:
        def __init__(self, hp: int,initiative: int, name: str, counterHealthpotions: int) -> None:
            self.hp = hp
            self.initiative = initiative
            self.name = name
            self.counterHealthpotions = counterHealthpotions
    
    #Subklasse Magier
    class mage(character):
        def __init__(self, hp: int,initiative: int, name: str, counterHealthpotions: int, counterFireball: int) -> None:
            super().__init__(hp, initiative, name, counterHealthpotions)
            self.counterFireball = counterFireball
            
        def fireball(self,enemyHp, enemyName, player):
            if (player.counterFireball % 2 == 0 or player.counterFireball == 0):
                print("Der Feuerball lädt auf!")
                print("")
            elif (player.counterFireball % 2 != 0):
                damageFirstAttack = random.randint(1,7)
                damageSecondAttack = random.randint(1,7)
                newEnemyHp = enemyHp - (damageFirstAttack + damageSecondAttack)
                if (newEnemyHp > 0):
                    print("Der " + str(enemyName) + " hat " + str(damageFirstAttack + damageSecondAttack) + " Schaden bekommen. " + str(newEnemyHp) + " HP übrig!")
                    print("")
                elif (newEnemyHp <= 0):
                    print("Der " + str(enemyName) + " hat " + str(damageFirstAttack + damageSecondAttack) + " Schaden bekommen. 0 HP übrig!")
                    print("")
                return newEnemyHp
            
        def magicMissile(self, enemyHp, enemyName):
            damage = random.randint(1,6)
            newEnemyHp = enemyHp - damage
            if (newEnemyHp > 0):
                print("Der " + str(enemyName) + " hat " + str(damage) + " Schaden bekommen. " + str(newEnemyHp) + " HP übrig!")
                print("")
            elif (newEnemyHp <= 0):
                print("Der " + str(enemyName) + " hat " + str(damage) + " Schaden bekommen. 0 HP übrig!")
                print("")
            return newEnemyHp
            
            
        def mirrorImage(self):
            print("Fähigkeit Spiegelbild")
            print("")
            
        def smallHealthpotion(self, hp, player):
            heal = random.randint(1,4)
            newHp = hp + heal
            if (player.counterHealthpotions == 0):
                print("Deine HP wurden um " + str(heal) + " HP auf insgesamt " + str(newHp) + " HP erhöht!")
                print("")
            elif (player.counterHealthpotions != 0):
                print("Du hast die letzte Healthpotion aufgebraucht!")
                print("")
            return newHp

    #Subklasse Krieger
    class knight(character):
        def __init__(self, hp: int,initiative: int, name: str, counterHealthpotions: int) -> None:
            super().__init__(hp, initiative, name, counterHealthpotions)
            
        def swordstrike(self, enemyHP, enemyName):
            damage = random.randint(1,7)
            newEnemyHp = enemyHP - damage
            if (newEnemyHp > 0):
                print("Der " + str(enemyName) + " hat " + str(damage) + " Schaden bekommen. " + str(newEnemyHp) + " HP übrig!")
                print("")
            elif (newEnemyHp <= 0):
                print("Der " + str(enemyName) + " hat " + str(damage) + " Schaden bekommen. 0 HP übrig!")
                print("")
            return newEnemyHp
            
        def shieldblock(self):
            print("Fähigkeit Schildblock")
            print("")
        
        def healthpotionKnight(self, hp, player):
            heal = random.randint(1,6)
            newHp = hp + heal
            if (player.counterHealthpotions == 0):
                print("Deine HP wurden um " + str(heal) + " HP auf insgesamt " + str(newHp) + " HP erhöht!")
                print("")
            elif (player.counterHealthpotions != 0):
                print("Du hast die letzte Healthpotion aufgebraucht!")
                print("")
            return newHp
    
    #Subklasse Schurke
    class villain(character):
        def __init__(self, hp: int,initiative: int, name: str, counterHealthpotions: int) -> None:
            super().__init__(hp, initiative, name, counterHealthpotions)
            
        def sneakAttack(self, firstMove):
            if (firstMove == True):
                extraDamage = random.randint(1,3)
                print("Dein nächster Angriff wird um " + str(extraDamage) + " Schaden erhöht!")
                print("")
                return (extraDamage, firstMove)
            else:
                print("Der erste Zug gehört nicht dir, es folgt kein extra Schaden!")
                print("")
                extraDamage = 0
                return (extraDamage, firstMove)

            
        def dagger(self, enemyHP, enemyName):
            damageFirstAttack = random.randint(1,4)
            damageSecondAttack = random.randint(1,4)
            newEnemyHp = enemyHP - (damageFirstAttack + damageSecondAttack)
            if (newEnemyHp > 0):
                print("Der " + str(enemyName) + " hat " + str(damageFirstAttack + damageSecondAttack) + " Schaden bekommen. " + str(newEnemyHp) + " HP übrig!")
                print("")
            elif (newEnemyHp <= 0):
                print("Der " + str(enemyName) + " hat " + str(damageFirstAttack + damageSecondAttack) + " Schaden bekommen. 0 HP übrig!")
                print("")
            return newEnemyHp

            
        def dirtInEye(self):
            print("Fähigkeit Schmutz")
            print("")
            
        def healthpotionVillain(self, hp, player):
            heal = random.randint(1,6)
            newHp = hp + heal
            if (player.counterHealthpotions == 0):
                print("Deine HP wurden um " + str(heal) + " HP auf insgesamt " + str(newHp) + " HP erhöht!")
                print("")
            elif (player.counterHealthpotions != 0):
                print("Du hast die letzte Healthpotion aufgebraucht!")
                print("")
            return newHp
    
    #Nutzer die Charakterauswahl abfragen
    while (True):
        # print("Spieler 1, wähle deine Charakter. Zur Auswahl steht Magier, Krieger und Schurke")
        inputP1 = input("Spieler 1, wähle deine Charakter. Zur Auswahl steht Magier, Krieger und Schurke: ")
        if (inputP1.lower() == "magier"):
            p1Hp = random.randint(1,6) + 10
            p1Initiative = random.randint(1,6)
            p1 = mage(p1Hp, p1Initiative, "Magier", 0, 0)
            print("Magier:")
            print("HP",p1.hp)
            print("Initiative",p1.initiative)
            print("")
            break
        elif (inputP1.lower() == "krieger"):
            p1Hp = random.randint(1,10) + 10
            p1Initiative = random.randint(1,8)
            p1 = knight(p1Hp, p1Initiative, "Krieger", 0)
            print("Krieger:")
            print("HP",p1.hp)
            print("Initiative",p1.initiative)
            print("")
            break
        elif (inputP1.lower() == "schurke"):
            p1Hp = random.randint(1,8) + 10
            p1Initiative = random.randint(1,10)
            p1 = villain(p1Hp, p1Initiative, "Schurke", 0)
            print("Schurke:")
            print("HP",p1.hp)
            print("Initiative",p1.initiative)
            print("")
            break
        else:
            print(inputP1 + " ist kein valide Option, versuche es erneut!")
            print("")
            continue
    
    while(True):
        inputP2 = input("Spieler 2, wähle deine Charakter. Zur Auswahl steht Magier, Krieger und Schurke: ")
        if (inputP2.lower() == "magier"):
            p2Hp = random.randint(1,6) + 10
            p2Initiative = random.randint(1,6)
            p2 = mage(p2Hp, p2Initiative, "Magier", 0, 0)
            print("Magier:")
            print("HP",p2.hp)
            print("Initiative",p2.initiative)
            print("")
            break
        elif (inputP2.lower() == "krieger"):
            p2Hp = random.randint(1,10) + 10
            p2Initiative = random.randint(1,8)
            p2 = knight(p2Hp, p2Initiative, "Krieger", 0)
            print("Krieger:")
            print("HP",p2.hp)
            print("Initiative",p2.initiative)
            print("")
            break
        elif (inputP2.lower() == "schurke"):
            p2Hp = random.randint(1,8) + 10
            p2Initiative = random.randint(1,10)
            p2 = villain(p2Hp, p2Initiative, "Schurke", 0)
            print("Schurke:")
            print("HP",p2.hp)
            print("Initiative",p2.initiative)
            print("")
            break
        else:
            print(inputP2 + " ist kein valide Option, versuche es erneut!")
            print("")
            continue
        
    #Initiative beider Spieler für den ersten Zug abfragen
    p1FirstMove = False
    p2FirstMove = False
    if (p1.initiative > p2.initiative):
        p1FirstMove = True
    elif (p2.initiative > p1.initiative):
        p2FirstMove = True
    else:
        print("Die Initiativen beider Spieler sind gleich groß, das Spiel wird neu gestart!")
        dungeonAndDragons()
    
    #Kampf iterativ abspielen, bis einer der Spieler tot ist
    p1NextMove = False
    p2NextMove = False
    tupel = (0, False)
    while(True):
        if (p1FirstMove == True or p1NextMove == True):
            p2NextMove = True
            p1NextMove = False
            print(p1.name+", du bist am Zug!")
            print("HP: " + str(p1.hp))

            while(True):
                if (p1.name == "Krieger"):
                    input2P1 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Schwertschlag (1), Schildblock (2), Healthpotion (3)"))

                    if (input2P1 == 1):
                        newEnemyHp = p1.swordstrike(p2.hp, p2.name)
                        p2.hp = newEnemyHp
                        break
                    elif (input2P1 == 2):
                        p1.shieldblock()
                        break
                    elif (input2P1 == 3):
                        newHp = p1.healthpotionKnight(p1.hp, p1)
                        p1.hp = newHp
                        p1.counterHealthpotions = 1
                        break
                    else:
                        print(str(input2P1) + " ist keine existierende Fähigkeit, versuche es mit 1,2 oder 3!")
                        continue
                elif (p1.name == "Magier"):
                    input2P1 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Feuerball (1), Magic Missile (2), Spiegelbilder (3), kleine Heilung (4)"))
                    if (input2P1 == 1):
                        newEnemyHp = p1.fireball(p2.hp, p2.name, p1)
                        if (p1.counterFireball % 2 != 0):
                            p2.hp = newEnemyHp
                        p1.counterFireball += 1
                        break
                    elif (input2P1 == 2):
                        newEnemyHp = p1.magicMissile(p2.hp, p2.name)
                        p2.hp = newEnemyHp
                        break
                    elif (input2P1 == 3):
                        p1.mirrorImage()
                        break
                    elif (input2P1 == 4):
                        newHp = p1.smallHealthpotion(p1.hp, p1)
                        p1.hp = newHp
                        p1.counterHealthpotions = 1
                        break
                    else:
                        print(str(input2P1) + " ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
                elif (p1.name == "Schurke"):
                    input2P1 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Sneak-Attack (1), Dolchangriff (2), Schmutz (3), Healthpotion (4)"))
                    if (input2P1 == 1):
                        tupel = p1.sneakAttack(p1FirstMove)
                        break
                    elif (input2P1 == 2):
                        newEnemyHp = p1.dagger(p2.hp, p2.name)
                        if (tupel[1]):
                            print("Dein Gegner bekommt " + str(tupel[0]) + " HP extra Schaden aufgrund der Sneak-Attack")
                            print("")
                            p2.hp = newEnemyHp - tupel[0]
                        else:
                            p2.hp = newEnemyHp
                        break
                    elif (input2P1 == 3):
                        p1.dirtInEye()
                        if (tupel[1]):
                            #Code hier
                            pass
                        else:
                            #Code hier
                            pass
                        break
                    elif (input2P1 == 4):
                        newHp = p1.healthpotionVillain(p1.hp, p1)
                        p1.hp = newHp
                        p1.counterHealthpotions = 1
                        break
                    else:
                        print(str(input2P1) + " ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
            p1FirstMove = False
        elif (p2FirstMove == True or p2NextMove == True):
            p1NextMove = True
            p2NextMove = False
            print(p2.name+",du bist am Zug!")
            print("HP: " + str(p2.hp))

            while(True):
                if (p2.name == "Krieger"):
                    input2P2 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Schwertschlag (1), Schildblock (2), Healthpotion (3)"))

                    if (input2P2 == 1):
                        newEnemyHp = p2.swordstrike(p1.hp, p1.name)
                        p1.hp = newEnemyHp
                        break
                    elif (input2P2 == 2):
                        p2.shieldblock()
                        break
                    elif (input2P2 == 3):
                        newHp = p2.healthpotionKnight(p2.hp, p2)
                        p2.hp = newHp
                        p2.counterHealthpotions = 1
                        break
                    else:
                        print(str(input2P2) + " ist keine existierende Fähigkeit, versuche es mit 1,2 oder 3!")
                        continue
                elif (p2.name == "Magier"):
                    input2P2 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Feuerball (1), Magic Missile (2), Spiegelbilder (3), kleine Heilung (4)"))
                    if (input2P2 == 1):
                        newEnemyHp = p2.fireball(p1.hp, p1.name, p2)
                        if (p2.counterFireball % 2 != 0):
                            p1.hp = newEnemyHp
                        p2.counterFireball += 1
                        break
                    elif (input2P2 == 2):
                        newEnemyHp = p2.magicMissile(p1.hp, p1.name)
                        p1.hp = newEnemyHp
                        break
                    elif (input2P2 == 3):
                        p2.mirrorImage()
                        break
                    elif (input2P2 == 4):
                        newHp = p2.smallHealthpotion(p2.hp, p2)
                        p2.hp = newHp
                        p2.counterHealthpotions = 1
                        break
                    else:
                        print(str(input2P2) + " ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
                elif (p2.name == "Schurke"):
                    input2P2 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Sneak-Attack (1), Dolchangriff (2), Schmutz (3), Healthpotion (4)"))
                    if (input2P2 == 1):
                        tupel = p2.sneakAttack(p2FirstMove)
                        break
                    elif (input2P2 == 2):
                        newEnemyHp = p2.dagger(p1.hp, p1.name)
                        if (tupel[1]):
                            print("Dein Gegner bekommt " + str(tupel[0]) + " HP extra Schaden aufgrund der Sneak-Attack")
                            print("")
                            p1.hp = newEnemyHp - tupel[0]
                        else:
                            p1.hp = newEnemyHp
                        break
                    elif (input2P2 == 3):
                        p2.dirtInEye()
                        if (tupel[1]):
                            #Code hier
                            pass
                        else:
                            #Code hier
                            pass
                        break
                    elif (input2P2 == 4):
                        newHp = p2.healthpotionVillain(p2.hp, p2)
                        p2.hp = newHp
                        p2.counterHealthpotions = 1
                        break
                    else:
                        print(str(input2P2) + " ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
            p2FirstMove = False
        
        if (p1.hp <= 0):
            print("Der " + p2.name + " hat das Spiel gewonnen. Sein Gegner,der " + p1.name + " ,ist gestorben!")
            break
        elif (p2.hp <= 0):
            print("Der " + p1.name + " hat das Spiel gewonnen. Sein Gegner,der " + p2.name + " ,ist gestorben!")
            break

dungeonAndDragons()
