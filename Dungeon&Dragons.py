import random

def dungeonAndDragons():
    #Nutzer zu Beginn begrüßen
    print("Willkommen bei Dungeon&Dragons!")
    print("Made by LonelyStreetracer with ♥")
    print("")

    #Klassen für Spielcharactere erstellen
    #Vaterklasse Charakter
    class character:
        def __init__(self, hp: int,initiative: int) -> None:
            self.hp = hp
            self.initiative = initiative
    
    #Subklasse Magier
    class mage(character):
        def __init__(self, hp: int,initiative: int) -> None:
            super().__init__(hp, initiative)
            
        def fireball(self):
            print("Fähigkeit Feuerball")
            
        def magicMissile(self):
            print("Fähigkeit magic Missile")
            
        def mirrorImage(self):
            print("Fähigkeit Spiegelbild")
            
        def smallHealthpotion(self):
            print("Fähigkeit kleine Heilung")

    #Subklasse Krieger
    class knight(character):
        def __init__(self, hp: int,initiative: int) -> None:
            super().__init__(hp, initiative)
            
        def swordstrike(self):
            print("Fähigkeit Schwertschlag")
            
        def shieldblock(self):
            print("Fähigkeit Schildblock")
            
        def healthpotion(self):
            print("Fähigkeit Heilung")
    
    #Subklasse Schurke
    class villain(character):
        def __init__(self, hp: int,initiative: int) -> None:
            super().__init__(hp, initiative)
            
        def sneakAttack(self):
            print("Fähigkeit Sneack-Attack")
            
        def dagger(self):
            print("Fähigkeit Dolchangriff")
            
        def dirtInEye(self):
            print("Fähigkeit Schmutz")
            
        def healthpotion(self):
            print("Fähigkeit healthpotion")
    
    #Nutzer die Charakterauswahl abfragen
    while (True):
        # print("Spieler 1, wähle deine Charakter. Zur Auswahl steht Magier, Krieger und Schurke")
        inputP1 = input("Spieler 1, wähle deine Charakter. Zur Auswahl steht Magier, Krieger und Schurke: ")
        if (inputP1.lower() == "magier"):
            p1Hp = random.randint(1,6)
            p1Initiative = random.randint(1,6)
            p1 = mage(p1Hp, p1Initiative)
            print("Magier:")
            print("HP",p1.hp)
            print("Initiative",p1.initiative)
            print("")
            break
        elif (inputP1.lower() == "krieger"):
            p1Hp = random.randint(1,10)
            p1Initiative = random.randint(1,8)
            p1 = knight(p1Hp, p1Initiative)
            print("Krieger:")
            print("HP",p1.hp)
            print("Initiative",p1.initiative)
            print("")
            break
        elif (inputP1.lower() == "schurke"):
            p1Hp = random.randint(1,8)
            p1Initiative = random.randint(1,10)
            p1 = villain(p1Hp, p1Initiative)
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
            p2Hp = random.randint(1,6)
            p2Initiative = random.randint(1,6)
            p2 = mage(p2Hp, p2Initiative)
            print("Magier:")
            print("HP",p2.hp)
            print("Initiative",p2.initiative)
            print("")
            break
        elif (inputP2.lower() == "krieger"):
            p2Hp = random.randint(1,10)
            p2Initiative = random.randint(1,8)
            p2 = knight(p2Hp, p2Initiative)
            print("Krieger:")
            print("HP",p2.hp)
            print("Initiative",p2.initiative)
            print("")
            break
        elif (inputP2.lower() == "schurke"):
            p2Hp = random.randint(1,8)
            p2Initiative = random.randint(1,10)
            p2 = villain(p2Hp, p2Initiative)
            print("Schurke:")
            print("HP",p2.hp)
            print("Initiative",p2.initiative)
            print("")
            break
        else:
            print(inputP2 + " ist kein valide Option, versuche es erneut!")
            print("")
            continue

dungeonAndDragons()
