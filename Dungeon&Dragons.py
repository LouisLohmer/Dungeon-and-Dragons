import random

def dungeonAndDragons():
    #Nutzer zu Beginn begrüßen
    print("Willkommen bei Dungeon&Dragons!")
    print("Made by LonelyStreetracer with ♥")
    print("")

    #Klassen für Spielcharactere erstellen
    #Vaterklasse Charakter
    class character:
        def __init__(self, hp: int,initiative: int, name: str) -> None:
            self.hp = hp
            self.initiative = initiative
            self.name = name
    
    #Subklasse Magier
    class mage(character):
        def __init__(self, hp: int,initiative: int, name: str) -> None:
            super().__init__(hp, initiative, name)
            
        def fireball(self):
            print("Fähigkeit Feuerball")
            print("")
            
        def magicMissile(self):
            print("Fähigkeit magic Missile")
            print("")
            
        def mirrorImage(self):
            print("Fähigkeit Spiegelbild")
            print("")
            
        def smallHealthpotion(self):
            print("Fähigkeit kleine Heilung")
            print("")

    #Subklasse Krieger
    class knight(character):
        def __init__(self, hp: int,initiative: int, name: str) -> None:
            super().__init__(hp, initiative, name)
            
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
            
        def healthpotionKnight(self):
            print("Fähigkeit Heilung")
            print("")
    
    #Subklasse Schurke
    class villain(character):
        def __init__(self, hp: int,initiative: int, name: str) -> None:
            super().__init__(hp, initiative, name)
            
        def sneakAttack(self):
            print("Fähigkeit Sneack-Attack")
            print("")
            
        def dagger(self):
            print("Fähigkeit Dolchangriff")
            print("")
            
        def dirtInEye(self):
            print("Fähigkeit Schmutz")
            print("")
            
        def healthpotionVillain(self):
            print("Fähigkeit healthpotion")
            print("")
    
    #Nutzer die Charakterauswahl abfragen
    while (True):
        # print("Spieler 1, wähle deine Charakter. Zur Auswahl steht Magier, Krieger und Schurke")
        inputP1 = input("Spieler 1, wähle deine Charakter. Zur Auswahl steht Magier, Krieger und Schurke: ")
        if (inputP1.lower() == "magier"):
            p1Hp = random.randint(1,6) + 10
            p1Initiative = random.randint(1,6)
            p1 = mage(p1Hp, p1Initiative, "Magier")
            print("Magier:")
            print("HP",p1.hp)
            print("Initiative",p1.initiative)
            print("")
            break
        elif (inputP1.lower() == "krieger"):
            p1Hp = random.randint(1,10) + 10
            p1Initiative = random.randint(1,8)
            p1 = knight(p1Hp, p1Initiative, "Krieger")
            print("Krieger:")
            print("HP",p1.hp)
            print("Initiative",p1.initiative)
            print("")
            break
        elif (inputP1.lower() == "schurke"):
            p1Hp = random.randint(1,8) + 10
            p1Initiative = random.randint(1,10)
            p1 = villain(p1Hp, p1Initiative, "Schurke")
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
            p2 = mage(p2Hp, p2Initiative, "Magier")
            print("Magier:")
            print("HP",p2.hp)
            print("Initiative",p2.initiative)
            print("")
            break
        elif (inputP2.lower() == "krieger"):
            p2Hp = random.randint(1,10) + 10
            p2Initiative = random.randint(1,8)
            p2 = knight(p2Hp, p2Initiative, "Krieger")
            print("Krieger:")
            print("HP",p2.hp)
            print("Initiative",p2.initiative)
            print("")
            break
        elif (inputP2.lower() == "schurke"):
            p2Hp = random.randint(1,8) + 10
            p2Initiative = random.randint(1,10)
            p2 = villain(p2Hp, p2Initiative, "Schurke")
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
    while(True):
        if (p1FirstMove == True or p1NextMove == True):
            p2NextMove = True
            p1NextMove = False
            p1FirstMove = False
            print(p1.name+", du bist am Zug!")

            while(True):
                if (p1.name == "Krieger"):
                    input2P1 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Schwertschlag (1), Schildblock (2), Healthpotion (3)"))

                    if (input2P1 == 1):
                        returnValue = p1.swordstrike(p2.hp, p2.name)
                        p2.hp = returnValue
                        break
                    elif (input2P1 == 2):
                        p1.shieldblock()
                        break
                    elif (input2P1 == 3):
                        p1.healthpotionKnight()
                        break
                    else:
                        print(str(input2P1) + " ist keine existierende Fähigkeit, versuche es mit 1,2 oder 3!")
                        continue
                elif (p1.name == "Magier"):
                    input2P1 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Feuerball (1), Magic Missile (2), Spiegelbilder (3), kleine Heilung (4)"))
                    if (input2P1 == 1):
                        p1.fireball()
                        break
                    elif (input2P1 == 2):
                        p1.magicMissile()
                        break
                    elif (input2P1 == 3):
                        p1.mirrorImage()
                        break
                    elif (input2P1 == 4):
                        p1.smallHealthpotion()
                        break
                    else:
                        print(str(input2P1) + " ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
                elif (p1.name == "Schurke"):
                    input2P1 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Sneak-Attack (1), Dolchangriff (2), Schmutz (3), Healthpotion (4)"))
                    if (input2P1 == 1):
                        p1.sneakAttack()
                        break
                    elif (input2P1 == 2):
                        p1.dagger()
                        break
                    elif (input2P1 == 3):
                        p1.dirtInEye()
                        break
                    elif (input2P1 == 4):
                        p1.healthpotionVillain()
                        break
                    else:
                        print(str(input2P1) + " ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
        elif (p2FirstMove == True or p2NextMove == True):
            p1NextMove = True
            p2NextMove = False
            p2FirstMove = False
            print(p2.name+",du bist am Zug!")
            while(True):
                if (p2.name == "Krieger"):
                    input2P2 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Schwertschlag (1), Schildblock (2), Healthpotion (3)"))

                    if (input2P2 == 1):
                        p2.swordstrike(p1.hp, p1.name)
                        p1.hp = returnValue
                        break
                    elif (input2P2 == 2):
                        p2.shieldblock()
                        break
                    elif (input2P2 == 3):
                        p2.healthpotionKnight()
                        break
                    else:
                        print(str(input2P2) + " ist keine existierende Fähigkeit, versuche es mit 1,2 oder 3!")
                        continue
                elif (p2.name == "Magier"):
                    input2P2 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Feuerball (1), Magic Missile (2), Spiegelbilder (3), kleine Heilung (4)"))
                    if (input2P2 == 1):
                        p2.fireball()
                        break
                    elif (input2P2 == 2):
                        p2.magicMissile()
                        break
                    elif (input2P2 == 3):
                        p2.mirrorImage()
                        break
                    elif (input2P2 == 4):
                        p2.smallHealthpotion()
                        break
                    else:
                        print(str(input2P2) + " ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
                elif (p2.name == "Schurke"):
                    input2P2 = int(input("Folgende Fähigkeiten stehen zur Auswahl: Sneak-Attack (1), Dolchangriff (2), Schmutz (3), Healthpotion (4)"))
                    if (input2P2 == 1):
                        p2.sneakAttack()
                        break
                    elif (input2P2 == 2):
                        p2.dagger()
                        break
                    elif (input2P2 == 3):
                        p2.dirtInEye()
                        break
                    elif (input2P2 == 4):
                        p2.healthpotionVillain()
                        break
                    else:
                        print(str(input2P2) + " ist keine existierende Fähigkeit, versuche es mit 1,2,3 oder 4!")
                        continue
        
        if (p1.hp <= 0):
            print("Der " + p2.name + " hat das Spiel gewonnen. Sein Gegner,der " + p1.name + " ,ist gestorben!")
            return
        elif (p2.hp <= 0):
            print("Der " + p1.name + " hat das Spiel gewonnen. Sein Gegner,der " + p2.name + " ,ist gestorben!")
            return

dungeonAndDragons()
