import random

def dungeonAndDragons():
    #Nutzer zu Beginn begrüßen
    print("Willkommen bei Dungeon&Dragons!")
    print("Made by LonelyStreetracer with ♥")
    print("")

    #Klassen für Spielcharactere erstellen
    #Vaterklasse Charakter
    class character:
        def __init__(self, hp: int,initiative: int, name: str, counterHealthpotions: int, counterAttack: int) -> None:
            self.hp = hp
            self.initiative = initiative
            self.name = name
            self.counterHealthpotions = counterHealthpotions
            self.counterAttack = counterAttack
    
    #Subklasse Magier
    class mage(character):
        def __init__(self, hp: int,initiative: int, name: str, counterHealthpotions: int, counterFireball: int, counterAttack: int) -> None:
            super().__init__(hp, initiative, name, counterHealthpotions, counterAttack)
            self.counterFireball = counterFireball
            
        def fireball(self,enemyHp, enemyName, player):
            if (player.counterFireball % 2 == 0 or player.counterFireball == 0):
                print("Der Feuerball lädt auf!")
                print("")
                newEnemyHp = enemyHp
                return newEnemyHp
            elif (player.counterFireball % 2 != 0):
                damageFirstAttack = random.randint(1,7)
                damageSecondAttack = random.randint(1,7)
                newEnemyHp = enemyHp - (damageFirstAttack + damageSecondAttack)
                if (newEnemyHp > 0):
                    print("Der ",enemyName," hat ",(damageFirstAttack + damageSecondAttack)," Schaden bekommen. ",newEnemyHp," HP übrig!")
                    print("")
                elif (newEnemyHp <= 0):
                    print("Der ",enemyName," hat ",(damageFirstAttack + damageSecondAttack)," Schaden bekommen. 0 HP übrig!")
                    print("")
                return newEnemyHp
            
        def magicMissile(self, enemyHp, enemyName):
            damage = random.randint(1,6)
            newEnemyHp = enemyHp - damage
            if (newEnemyHp > 0):
                print("Der ",enemyName," hat ",damage," Schaden bekommen. ",newEnemyHp," HP übrig!")
                print("")
            elif (newEnemyHp <= 0):
                print("Der ",enemyName," hat ",damage," Schaden bekommen. 0 HP übrig!")
                print("")
            return newEnemyHp
            
            
        def mirrorImage(self):
            percentage = random.random()
            percentage = round(percentage, 2)
            if (percentage >= 0.5):
                print("Der Magier bekommt für die nächsten zwei Angriffe keinen Schaden!")
                print("")
            elif (percentage < 0.5):
                print("pech gehabt, deine Immunität wird nicht gewährt!")
                print("")
            return percentage
            
        def smallHealthpotion(self, player):
            heal = random.randint(1,4)
            if (player.counterHealthpotions == 0):
                print("Deine HP wurden um ",heal," HP erhöht!")
                print("")
                return heal
            elif (player.counterHealthpotions != 0):
                print("Du hast die letzte Healthpotion aufgebraucht!")
                print("")
                heal = 0
                return heal

    #Subklasse Krieger
    class knight(character):
        def __init__(self, hp: int,initiative: int, name: str, counterHealthpotions: int, counterAttack: int) -> None:
            super().__init__(hp, initiative, name, counterHealthpotions, counterAttack)
            
        def swordstrike(self, enemyHP, enemyName):
            damage = random.randint(1,7)
            newEnemyHp = enemyHP - damage
            if (newEnemyHp > 0):
                print("Der ",enemyName," hat ",damage," Schaden bekommen. ",newEnemyHp," HP übrig!")
                print("")
            elif (newEnemyHp <= 0):
                print("Der ",enemyName," hat ",damage," Schaden bekommen. 0 HP übrig!")
                print("")
            return newEnemyHp
            
        def shieldblock(self):
            damagereduction = random.randint(1,4)
            print("Der nächste Angriff wir um ",damagereduction," Schadenspunkte reduziert!")
            print("")
            return damagereduction

        
        def healthpotionKnight(self, player):
            heal = random.randint(1,6)
            if (player.counterHealthpotions == 0):
                print("Deine HP wurden um ",heal," HP erhöht!")
                print("")
                return heal
            elif (player.counterHealthpotions != 0):
                print("Du hast die letzte Healthpotion aufgebraucht!")
                print("")
                heal = 0
                return heal
    
    #Subklasse Schurke
    class villain(character):
        def __init__(self, hp: int,initiative: int, name: str, counterHealthpotions: int, counterAttack: int) -> None:
            super().__init__(hp, initiative, name, counterHealthpotions, counterAttack)
            
        def sneakAttack(self, firstMove):
            if (firstMove == True):
                extraDamage = random.randint(1,3)
                print("Dein nächster Angriff wird um ",extraDamage," Schaden erhöht!")
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
                print("Der ",enemyName," hat ",(damageFirstAttack + damageSecondAttack)," Schaden bekommen. ",newEnemyHp," HP übrig!")
                print("")
            elif (newEnemyHp <= 0):
                print("Der ",enemyName," hat ",(damageFirstAttack + damageSecondAttack)," Schaden bekommen. 0 HP übrig!")
                print("")
            return newEnemyHp

            
        def dirtInEye(self):
            print("Fähigkeit Schmutz")
            print("")
            
        def healthpotionVillain(self, player):
            heal = random.randint(1,6)
            if (player.counterHealthpotions == 0):
                print("Deine HP wurden um ",heal," HP erhöht!")
                print("")
                return heal
            elif (player.counterHealthpotions != 0):
                print("Du hast die letzte Healthpotion aufgebraucht!")
                print("")
                heal = 0
                return heal
    
    #Nutzer die Charakterauswahl abfragen
    while (True):
        # print("Spieler 1, wähle deine Charakter. Zur Auswahl steht Magier, Krieger und Schurke")
        inputCharacterP1 = input("Spieler 1, wähle deine Charakter. Zur Auswahl steht Magier, Krieger und Schurke: ")
        if (inputCharacterP1.lower() == "magier"):
            p1Hp = random.randint(1,6) + 10
            p1Initiative = random.randint(1,6)
            p1 = mage(p1Hp, p1Initiative, "Magier", 0, 0, 0)
            print("Magier:")
            print("HP",p1.hp)
            print("Initiative",p1.initiative)
            print("")
            break
        elif (inputCharacterP1.lower() == "krieger"):
            p1Hp = random.randint(1,10) + 10
            p1Initiative = random.randint(1,8)
            p1 = knight(p1Hp, p1Initiative, "Krieger", 0, 0)
            print("Krieger:")
            print("HP",p1.hp)
            print("Initiative",p1.initiative)
            print("")
            break
        elif (inputCharacterP1.lower() == "schurke"):
            p1Hp = random.randint(1,8) + 10
            p1Initiative = random.randint(1,10)
            p1 = villain(p1Hp, p1Initiative, "Schurke", 0, 0)
            print("Schurke:")
            print("HP",p1.hp)
            print("Initiative",p1.initiative)
            print("")
            break
        else:
            print(inputCharacterP1 + " ist kein valide Option, versuche es erneut!")
            print("")
            continue
    
    while(True):
        inputCharacterP2 = input("Spieler 2, wähle deine Charakter. Zur Auswahl steht Magier, Krieger und Schurke: ")
        if (inputCharacterP2.lower() == "magier"):
            p2Hp = random.randint(1,6) + 10
            p2Initiative = random.randint(1,6)
            p2 = mage(p2Hp, p2Initiative, "Magier", 0, 0, 0)
            print("Magier:")
            print("HP",p2.hp)
            print("Initiative",p2.initiative)
            print("")
            break
        elif (inputCharacterP2.lower() == "krieger"):
            p2Hp = random.randint(1,10) + 10
            p2Initiative = random.randint(1,8)
            p2 = knight(p2Hp, p2Initiative, "Krieger", 0, 0)
            print("Krieger:")
            print("HP",p2.hp)
            print("Initiative",p2.initiative)
            print("")
            break
        elif (inputCharacterP2.lower() == "schurke"):
            p2Hp = random.randint(1,8) + 10
            p2Initiative = random.randint(1,10)
            p2 = villain(p2Hp, p2Initiative, "Schurke", 0, 0)
            print("Schurke:")
            print("HP",p2.hp)
            print("Initiative",p2.initiative)
            print("")
            break
        else:
            print(inputCharacterP2 + " ist kein valide Option, versuche es erneut!")
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
        print("")
        dungeonAndDragons()
    
    #Kampf iterativ abspielen, bis einer der Spieler tot ist
    p1NextMove = False
    p2NextMove = False
    tupelVillain = (0, False)
    percentage = 0
    damagereduction = 0
    while(True):
        if (p1FirstMove == True or p1NextMove == True):
            p2NextMove = True
            p1NextMove = False
            print(p1.name+", du bist am Zug!")
            print("HP: ",p1.hp)

            while(True):
                if (p1.name == "Krieger"):
                    inputMoveP1 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Schwertschlag (1), Schildblock (2), Healthpotion (3)"))

                    if (inputMoveP1 == 1):
                        newEnemyHp = p1.swordstrike(p2.hp, p2.name)
                        if (p1.name == "Krieger" and p2.name == "Krieger"):
                            if (damagereduction > 0 and p2.counterAttack < 1):
                                #Fähigkeit/Funktion Schildblock
                                print("Die Attacke wurde um ",damagereduction," Schadenspunkte reduziert.")
                                print("")
                                p2.hp = newEnemyHp + damagereduction
                                p2.counterAttack += 1
                                if (p2.counterAttack == 1):
                                    p2.counterAttack = 0
                                    damagereduction = 0
                            else:
                                p2.hp = newEnemyHp
                        elif (percentage >= 0.5 and p2.counterAttack < 2):
                            print("Spiegelbild")
                            #Fähigkeit/Funktion Spiegelbild
                            print("Angriff blockiert aufgrund von Spiegelbild")
                            print("")
                            p2.counterAttack += 1
                            if (p2.counterAttack == 2):
                                p2.counterAttack = 0
                                percentage = 0
                        else:
                            p2.hp = newEnemyHp
                        break
                    elif (inputMoveP1 == 2):
                        damagereduction = p1.shieldblock()
                        break
                    elif (inputMoveP1 == 3):
                        heal = p1.healthpotionKnight(p1)
                        p1.hp = p1.hp + heal
                        p1.counterHealthpotions = 1
                        break
                    else:
                        print(inputMoveP1," ist keine existierende Fähigkeit, versuche es mit 1,2 oder 3!")
                        continue
                elif (p1.name == "Magier"):
                    inputMoveP1 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Feuerball (1), Magic Missile (2), Spiegelbilder (3), kleine Heilung (4)"))
                    
                    if (inputMoveP1 == 1):
                        newEnemyHp = p1.fireball(p2.hp, p2.name, p1)
                        if (p2.name == "Magier" and p1.name == "Magier"):
                            if (p1.counterFireball % 2 != 0):
                                #Fähigkeit/Funktion Spiegelbild
                                if (percentage >= 0.5 and p2.counterAttack < 2):
                                    print("Angriff blockiert aufgrund von Spiegelbild")
                                    print("")
                                    p2.counterAttack += 1
                                    if (p2.counterAttack == 2 and p1.counterAttack == 2):
                                        p2.counterAttack = 0
                                        p1.counterAttack = 0
                                        percentage = 0
                                else:
                                    p2.hp = newEnemyHp
                        elif (damagereduction > 0 and p2.counterAttack < 1 and p1.counterFireball % 2 != 0):
                            #Fähigkeit/Funktion Schildblock
                            print("Die Attacke wurde um ",damagereduction," Schadenspunkte reduziert.")
                            print("")
                            p2.hp = newEnemyHp + damagereduction
                            p2.counterAttack += 1
                            if (p2.counterAttack == 1):
                                p2.counterAttack = 0
                                damagereduction = 0
                        else:
                            p2.hp = newEnemyHp
                        p1.counterFireball += 1
                        break
                    elif (inputMoveP1 == 2):
                        newEnemyHp = p1.magicMissile(p2.hp, p2.name)
                        if (p2.name == "Magier" and p1.name == "Magier"):
                            if (percentage >= 0.5 and p2.counterAttack < 2):
                                #Fähigkeit/Funktion Spiegelbild
                                print("Angriff blockiert aufgrund von Spiegelbild")
                                print("")
                                p2.counterAttack += 1
                                if (p2.counterAttack == 2 and p1.counterAttack == 2):
                                    p2.counterAttack = 0
                                    p1.counterAttack = 0
                                    percentage = 0
                            else:
                                p2.hp = newEnemyHp
                        elif (damagereduction > 0 and p2.counterAttack < 1):
                            #Fähigkeit/Funktion Schildblock
                            print("Die Attacke wurde um ",damagereduction," Schadenspunkte reduziert.")
                            print("")
                            p2.hp = newEnemyHp + damagereduction
                            p2.counterAttack += 1
                            if (p2.counterAttack == 1):
                                p2.counterAttack = 0
                                damagereduction = 0
                        else:
                            p2.hp = newEnemyHp
                        break
                    elif (inputMoveP1 == 3):
                        percentage = p1.mirrorImage()
                        break
                    elif (inputMoveP1 == 4):
                        heal = p1.smallHealthpotion(p1)
                        p1.hp = p1.hp + heal
                        p1.counterHealthpotions = 1
                        break
                    else:
                        print(inputMoveP1," ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
                elif (p1.name == "Schurke"):
                    inputMoveP1 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Sneak-Attack (1), Dolchangriff (2), Schmutz (3), Healthpotion (4)"))
                    if (inputMoveP1 == 1):
                        tupelVillain = p1.sneakAttack(p1FirstMove)
                        break
                    elif (inputMoveP1 == 2):
                        newEnemyHp = p1.dagger(p2.hp, p2.name)
                        if (tupelVillain[1] and percentage < 0.5):
                            #Fähigkeit/Funktion sneakAttack
                            print("Dein Gegner bekommt ",tupelVillain[0]," HP extra Schaden aufgrund der Sneak-Attack")
                            print("")
                            if (damagereduction > 0 and p2.counterAttack < 1):
                                #Fähigkeit/Funktion Schildblock
                                print("Die Attacke wurde um ",damagereduction," Schadenspunkte reduziert.")
                                print("")
                                p2.hp = newEnemyHp - tupelVillain[0] + damagereduction
                                p2.counterAttack += 1
                                if (p2.counterAttack == 1):
                                    p2.counterAttack = 0
                                    damagereduction = 0
                            else:
                                p2.hp = newEnemyHp - tupelVillain[0]
                        elif (percentage >= 0.5 and p2.counterAttack < 2):
                            #Fähigkeit/Funktion Spiegelbild
                            print("Angriff blockiert aufgrund von Spiegelbild")
                            print("")
                            p2.counterAttack += 1
                            if (p2.counterAttack == 2):
                                p2.counterAttack = 0
                                percentage = 0
                        elif (damagereduction > 0 and p2.counterAttack < 1):
                            #Fähigkeit/Funktion Schildblock
                            print("Die Attacke wurde um ",damagereduction," Schadenspunkte reduziert.")
                            print("")
                            p2.hp = newEnemyHp + damagereduction
                            p2.counterAttack += 1
                            if (p2.counterAttack == 1):
                                p2.counterAttack = 0
                                damagereduction = 0
                        else:
                            p2.hp = newEnemyHp
                        break
                    elif (inputMoveP1 == 3):
                        p1.dirtInEye()
                        break
                    elif (inputMoveP1 == 4):
                        heal = p1.healthpotionVillain(p1)
                        p1.hp = p1.hp + heal
                        p1.counterHealthpotions = 1
                        break
                    else:
                        print(inputMoveP1," ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
            p1FirstMove = False
        elif (p2FirstMove == True or p2NextMove == True):
            p1NextMove = True
            p2NextMove = False
            print(p2.name+",du bist am Zug!")
            print("HP: ",p2.hp)

            while(True):
                if (p2.name == "Krieger"):
                    inputMoveP2 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Schwertschlag (1), Schildblock (2), Healthpotion (3)"))

                    if (inputMoveP2 == 1):
                        newEnemyHp = p2.swordstrike(p1.hp, p1.name)
                        if (p1.name == "Krieger" and p2.name == "Krieger"):
                            if (damagereduction > 0 and p1.counterAttack < 1):
                                #Fähigkeit/Funktion Schildblock
                                print("Die Attacke wurde um ",damagereduction," Schadenspunkte reduziert.")
                                print("")
                                p1.hp = newEnemyHp + damagereduction
                                p1.counterAttack += 1
                                if (p1.counterAttack == 1):
                                    p1.counterAttack = 0
                                    damagereduction = 0
                            else:
                                p1.hp = newEnemyHp
                        elif (percentage >= 0.5 and p1.counterAttack < 2):
                            print("Spiegelbild")
                            #Fähigkeit/Funktion Spiegelbild
                            print("Angriff blockiert aufgrund von Spiegelbild")
                            print("")
                            p1.counterAttack += 1
                            if (p1.counterAttack == 2):
                                p1.counterAttack = 0
                                percentage = 0
                        else:
                            p1.hp = newEnemyHp
                        break
                    elif (inputMoveP2 == 2):
                        damagereduction = p2.shieldblock()
                        break
                    elif (inputMoveP2 == 3):
                        heal = p2.healthpotionKnight(p2)
                        p2.hp = p2.hp + heal
                        p2.counterHealthpotions = 1
                        break
                    else:
                        print(inputMoveP2," ist keine existierende Fähigkeit, versuche es mit 1,2 oder 3!")
                        continue
                elif (p2.name == "Magier"):
                    inputMoveP2 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Feuerball (1), Magic Missile (2), Spiegelbilder (3), kleine Heilung (4)"))
                   
                    if (inputMoveP2 == 1):
                        newEnemyHp = p2.fireball(p1.hp, p1.name, p2)
                        if (p2.name == "Magier" and p1.name == "Magier"):
                            if (p2.counterFireball % 2 != 0):
                                if (percentage >= 0.5 and p1.counterAttack < 2):
                                    #Fähigkeit/Funktion Spiegelbild
                                    print("Angriff blockiert aufgrund von Spiegelbild")
                                    print("")
                                    p1.counterAttack += 1
                                    if (p2.counterAttack == 2 and p1.counterAttack == 2):
                                        p2.counterAttack = 0
                                        p1.counterAttack = 0
                                        percentage = 0
                                else:
                                    p1.hp = newEnemyHp
                        elif (damagereduction > 0 and p1.counterAttack < 1 and p2.counterFireball % 2 != 0):
                                    #Fähigkeit/Funktion Schildblock
                                    print("Die Attacke wurde um ",damagereduction," Schadenspunkte reduziert.")
                                    print("")
                                    p1.hp = newEnemyHp + damagereduction
                                    p1.counterAttack += 1
                                    if (p1.counterAttack == 1):
                                        p1.counterAttack = 0
                                        damagereduction = 0
                        else:
                            p1.hp = newEnemyHp
                        p2.counterFireball += 1
                        break
                    elif (inputMoveP2 == 2):
                        newEnemyHp = p2.magicMissile(p1.hp, p1.name)
                        if (p2.name == "Magier" and p1.name == "Magier"):
                            if (percentage >= 0.5 and p1.counterAttack < 2):
                                #Fähigkeit/Funktion Spiegelbild
                                print("Angriff blockiert aufgrund von Spiegelbild")
                                print("")
                                p1.counterAttack += 1
                                if (p2.counterAttack == 2 and p1.counterAttack == 2):
                                    p2.counterAttack = 0
                                    p1.counterAttack = 0
                                    percentage = 0
                            else:
                                p1.hp = newEnemyHp
                        elif (damagereduction > 0 and p1.counterAttack < 1):
                            #Fähigkeit/Funktion Schildblock
                            print("Die Attacke wurde um ",damagereduction," Schadenspunkte reduziert.")
                            print("")
                            p1.hp = newEnemyHp + damagereduction
                            p1.counterAttack += 1
                            if (p1.counterAttack == 1):
                                p1.counterAttack = 0
                                damagereduction = 0
                        else:
                            p1.hp = newEnemyHp
                        break
                    elif (inputMoveP2 == 3):
                        percentage = p2.mirrorImage()
                        break
                    elif (inputMoveP2 == 4):
                        heal = p2.smallHealthpotion(p2)
                        p2.hp = p2.hp + heal
                        p2.counterHealthpotions = 1
                        break
                    else:
                        print(inputMoveP2," ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
                elif (p2.name == "Schurke"):
                    inputMoveP2 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Sneak-Attack (1), Dolchangriff (2), Schmutz (3), Healthpotion (4)"))
                    if (inputMoveP2 == 1):
                        tupelVillain = p2.sneakAttack(p2FirstMove)
                        break
                    elif (inputMoveP2 == 2):
                        newEnemyHp = p2.dagger(p1.hp, p1.name)
                        if (tupelVillain[1] and percentage < 0.5):
                            #Fähigkeit/Funktion sneakAttack
                            print("Dein Gegner bekommt ",tupelVillain[0]," HP extra Schaden aufgrund der Sneak-Attack")
                            print("")
                            if (damagereduction > 0 and p1.counterAttack < 1):
                                #Fähigkeit/Funktion Schildblock
                                print("Die Attacke wurde um ",damagereduction," Schadenspunkte reduziert.")
                                print("")
                                p1.hp = newEnemyHp - tupelVillain[0] + damagereduction
                                p1.counterAttack += 1
                                if (p1.counterAttack == 1):
                                    p1.counterAttack = 0
                                    damagereduction = 0
                            else:
                                p1.hp = newEnemyHp - tupelVillain[0]
                        elif (percentage >= 0.5 and p1.counterAttack < 2):
                            #Fähigkeit/Funktion Spiegelbild
                            print("Angriff blockiert aufgrund von Spiegelbild")
                            print("")
                            p1.counterAttack += 1
                            if (p1.counterAttack == 2):
                                p1.counterAttack = 0
                                percentage = 0
                        elif (damagereduction > 0 and p1.counterAttack < 1):
                            #Fähigkeit/Funktion Schildblock
                            print("Die Attacke wurde um ",damagereduction," Schadenspunkte reduziert.")
                            print("")
                            p1.hp = newEnemyHp + damagereduction
                            p1.counterAttack += 1
                            if (p1.counterAttack == 1):
                                p1.counterAttack = 0
                                damagereduction = 0
                        else:
                            p1.hp = newEnemyHp
                        break
                    elif (inputMoveP2 == 3):
                        p2.dirtInEye()
                        break
                    elif (inputMoveP2 == 4):
                        heal = p2.healthpotionVillain(p2)
                        p2.hp = p2.hp + heal
                        p2.counterHealthpotions = 1
                        break
                    else:
                        print(inputMoveP2," ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
            p2FirstMove = False

        if (p1.hp <= 0):
            print("Der " + p2.name + " hat das Spiel gewonnen. Sein Gegner, der " + p1.name + " ,ist gestorben!")
            break
        elif (p2.hp <= 0):
            print("Der " + p1.name + " hat das Spiel gewonnen. Sein Gegner, der " + p2.name + " ,ist gestorben!")
            break

dungeonAndDragons()
