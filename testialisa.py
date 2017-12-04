#main game loop
import mysql.connector
db = mysql.connector.connect(host="localhost", user="dbuser",
                             passwd="dbpass", db="omapeli", buffered=True)

cur = db.cursor()
playerAlive = True
potionDrink = False
magicDrink = False
commands = ["-Possible directions to walk to:","[north]/[n]","[east]/[e]","[west]/[w]",
            "[south]/[s]","[down]/[d]","[up]/[u]","-To open inventory:","[inventory]/[i]",
            "-To exit game:","[exit]","-To examine an item, room or a container:",
            "[examine (object)]","-To pick up/take an item:",
            "[pick (item)]/[pick up (item)]/[take (item)]","-To drop an item:",
            "[drop (item)]","-To drink something:","[drink (item)]",
            "-To attack/stab something:","[attack (target)]/[stab (target)]",
            "-To talk to someone:","[talk (npc)]/[talk to (npc)]"]
#pelinpulma metodina
def muunna(i):
    return (i+1)%2
def puzzle():
    a1=a2=a3=a4=b1=b2=b3=b4=c1=c2=c3=c4=d1=d2=d3=d4=0
    while not (a1==a2==a3==a4==b1==b4==c1==c4==d1==d2==d3==d4==0 and b2==b3==c2==c3==1):
        print("  "+str(1)+" "+str(2)+" "+str(3)+" "+str(4))
        print("A "+str(a1)+" "+str(a2)+" "+str(a3)+" "+str(a4))
        print("B "+str(b1)+" "+str(b2)+" "+str(b3)+" "+str(b4))
        print("C "+str(c1)+" "+str(c2)+" "+str(c3)+" "+str(c4))
        print("D "+str(d1)+" "+str(d2)+" "+str(d3)+" "+str(d4))

        ruutu = input("Anna ruutu: ")

        if ruutu == "A1" or ruutu == "a1":
            a1 = muunna(a1)
            a2 = muunna(a2)
            b1 = muunna(b1)

        elif ruutu == "A2" or ruutu == "a2":
            a1 = muunna(a1)
            a2 = muunna(a2)
            a3 = muunna(a3)
            b2 = muunna(b2)

        elif ruutu == "A3" or ruutu == "a3":
            a2 = muunna(a2)
            a3 = muunna(a3)
            a4 = muunna(a4)
            b3 = muunna(b3)

        elif ruutu == "A4" or ruutu == "a4":
            a3 = muunna(a3)
            a4 = muunna(a4)
            b4 = muunna(b4)

        elif ruutu == "B1" or ruutu == "b1":
            a1 = muunna(a1)
            b1 = muunna(b1)
            b2 = muunna(b2)
            c1 = muunna(c1)

        elif ruutu == "B2" or ruutu == "b2":
            a2 = muunna(a2)
            b1 = muunna(b1)
            b2 = muunna(b2)
            b3 = muunna(b3)
            c2 = muunna(c2)

        elif ruutu == "B3" or ruutu == "b3":
            a3 = muunna(a3)
            b2 = muunna(b2)
            b3 = muunna(b3)
            b4 = muunna(b4)
            c3 = muunna(c3)

        elif ruutu == "B4" or ruutu == "b4":
            a4 = muunna(a4)
            b3 = muunna(b3)
            b4 = muunna(b4)
            c4 = muunna(c4)

        elif ruutu == "C1" or ruutu == "c1":
            b1 = muunna(b1)
            c1 = muunna(c1)
            c2 = muunna(c2)
            d1 = muunna(d1)

        elif ruutu == "C2" or ruutu == "c2":
            b2 = muunna(b2)
            c1 = muunna(c1)
            c2 = muunna(c2)
            c3 = muunna(c3)
            d2 = muunna(d2)

        elif ruutu == "C3" or ruutu == "c3":
            b3 = muunna(b3)
            c2 = muunna(c2)
            c3 = muunna(c3)
            c4 = muunna(c4)
            d3 = muunna(d3)

        elif ruutu == "C4" or ruutu == "c4":
            b4 = muunna(b4)
            c3 = muunna(c3)
            c4 = muunna(c4)
            d4 = muunna(d4)

        elif ruutu == "D1" or ruutu == "d1":
            c1 = muunna(c1)
            d1 = muunna(d1)
            d2 = muunna(d2)

        elif ruutu == "D2" or ruutu == "d2":
            c2 = muunna(c2)
            d1 = muunna(d1)
            d2 = muunna(d2)
            d3 = muunna(d3)

        elif ruutu == "D3" or ruutu == "d3":
            c3 = muunna(c3)
            d2 = muunna(d2)
            d3 = muunna(d3)
            d4 = muunna(d4)

        elif ruutu == "D4" or ruutu == "d4":
            c4 = muunna(c4)
            d3 = muunna(d3)
            d4 = muunna(d4)

        elif ruutu == "reset":
            a1=a2=a3=a4=b1=b2=b3=b4=c1=c2=c3=c4=d1=d2=d3=d4=0
        elif ruutu == "exit" or ruutu=="stop":
            return False
            break
        else:
            print("False command")


    if (a1==a2==a3==a4==b1==b4==c1==c4==d1==d2==d3==d4==0 and b2==b3==c2==c3==1):    
        print("  "+str(1)+" "+str(2)+" "+str(3)+" "+str(4))
        print("A "+str(a1)+" "+str(a2)+" "+str(a3)+" "+str(a4))
        print("B "+str(b1)+" "+str(b2)+" "+str(b3)+" "+str(b4))
        print("C "+str(c1)+" "+str(c2)+" "+str(c3)+" "+str(c4))
        print("D "+str(d1)+" "+str(d2)+" "+str(d3)+" "+str(d4))
        print("The door opens")
        return True

def move(command):
    cur.execute("SELECT positionID FROM Player;")
    playerpos = cur.fetchall()
    print(str(playerpos[0][0]))
    haku = ("SELECT RoomTO FROM Connect where RoomFrom = " + str(playerpos[0][0]) + " and direction='" + str(command) + "'")
    cur.execute(haku)
    destination = cur.fetchall()
    if cur.rowcount == 1:
        cur.execute("Select isLocked From Connect where RoomFrom = " + str(playerpos[0][0]) + " and direction='" + str(command) + "'")
        locked = cur.fetchall()
        print(str(locked[0][0]))
        if int(playerpos[0][0]) == 122 and int(destination[0][0])== 121 and int(locked[0][0])== 1:
            if puzzle() == True:
                cur.execute("UPDATE Connect set isLocked = 0 where RoomFrom = 122 and RoomTo = 121")
            else:
                print("You did not solve the puzzle, the door is still locked")
        else:
            liikkuu = ("UPDATE Player set PositionID = " + str(destination[0][0]))
            cur.execute(liikkuu)
            cur.execute("SELECT positionID FROM Player;")
            playerpos = cur.fetchall()
            print(str(playerpos[0][0]))
            cur.execute("select RoomDescr from Room where positionID =" + str(playerpos[0][0]))
            kuvaus = cur.fetchall()
            print(str(kuvaus[0][0]))
            cur.execute("select ItemN from Item where itemPosition = " + str(playerpos[0][0]))
            tavarat = cur.fetchall()
            if cur.rowcount >=1:
                print("There are following items in this room:")
                for row in tavarat:
                      print(" - " + str(row[0]))
    else:
        print("You cannot go there, because there is nothing in that direction")

def pickUp(object):
    cur.execute("SELECT ItemN FROM item WHERE ItemN like '"+object+"'")
    result = cur.fetchall()
    if len(result) == 1:
        cur.execute("SELECT ItemN FROM item WHERE ItemN like '"+object+"' AND ItemN IN (\
    SELECT ItemN FROM item INNER JOIN player ON item.ItemPosition = \
    player.PositionID WHERE ItemPosition IN (SELECT PositionID FROM player))")
        result = cur.fetchall()
        if len(result) == 1:
            print(str(object))
            cur.execute("UPDATE item SET ItemPosition=null WHERE ItemN='"+str(object)+"'")
            cur.execute("UPDATE item SET PlayerID=1 WHERE ItemN='"+str(object)+"'")
            print("You picked up the "+str(object))
        else:
            print("There is no such item in the room")
    else:
        print("There is no such item in the room")

def inventory():
    cur.execute("SELECT ItemN FROM item WHERE PlayerID=1")
    result = cur.fetchall()
    if len(result) > 0:
        print("You have the following items: ")
        for row in result:
            print(row[0])
    else:
        print("You have no items in your inventory")
def attack(magicDrink):
    cur.execute("SELECT positionID FROM Player;")
    playerpos = cur.fetchall()
    print(str(playerpos[0][0]))
    if playerpos[0][0] == 113:
        tool=input("What do you want to use to attack?: ")
        haku = ("Select PlayerID From Item where ItemN = '" + str(tool) + "'")
        cur.execute(haku)
        tulos = cur.fetchall()
        print(str(tulos))
        if len(tulos)>0:
            if str(tulos[0][0]) != "None":
                if tool == "sword":
                    if magicDrink == False:
                        print("You killed the rat")
                        return True
                    else:
                        print("You are not carrying a sword anymore and cannot use it")
                        print("The rat was fast and killed you")
                        return False
                elif tool == "needle":
                    print("You killed the rat")
                    return True
                elif tool == "knife":
                    print("The rat is stronger than you and it killed you")
                    return False
                else:
                    print("You cannot use that to attack")
            else:
                print("You don't have that item")
                return False
    else:
        print("There's nobody to attack.")
        return False

def examine(thing):
    cur.execute("SELECT ItemDescr FROM item WHERE ItemN LIKE '"+thing+"' AND PlayerID=1")
    resultItem = cur.fetchall()

    cur.execute("SELECT ItemDescr FROM item INNER JOIN player ON item.ItemPosition = \
    player.PositionID WHERE ItemN LIKE '"+thing+"'")
    resultInRoom = cur.fetchall()

    cur.execute("SELECT ContainerDescr FROM container INNER JOIN player ON \
    container.ContainerPosition = player.PositionID WHERE ContainerN LIKE '"+thing+"'")
    resultContainer = cur.fetchall()
    
    if len(resultItem) > 0:
        for row in resultItem:
            print(row[0])
    elif len(resultInRoom) > 0:
        for row in resultInRoom:
            print(row[0])
    elif len(resultContainer) > 0:
        for row in resultContainer:
            print(row[0])
        cur.execute("SELECT ItemN FROM item WHERE ContainerID IN (SELECT ContainerID FROM container \
    INNER JOIN player ON container.ContainerPosition = player.PositionID WHERE container.containerID = 3)")
        result = cur.fetchall()

        cur.execute("SELECT ItemN FROM item WHERE ContainerID IN (SELECT ContainerID FROM container \
    INNER JOIN player ON container.ContainerPosition = player.PositionID)")
        result2 = cur.fetchall()

        if len(result) > 0:
            for row in result:
                item = row[0]
            print("A "+str(item)+" dropped from it.")
            cur.execute("UPDATE item SET ContainerID = null WHERE ItemN='"+str(item)+"'")
            cur.execute("SELECT PositionID FROM player")
            result = cur.fetchall()
            for row in result:
                position = row[0]
            print("toimii")
            cur.execute("UPDATE item SET ItemPosition = "+str(position)+" WHERE ItemN='"+str(item)+"'")
            print("toimii2")

        elif len(result2) > 0:
            cur.execute("SELECT ItemN from item WHERE ItemID = 4 AND PlayerID = 1")
            result = cur.fetchall()

            if len(result) == 0:
                print("You are too short to examine it")

            else:
                for row in result2:
                    item = row[0]
                print("A "+str(item)+" dropped from it.")
                cur.execute("UPDATE item SET ContainerID = null WHERE ItemN='"+str(item)+"'")
                cur.execute("SELECT PositionID FROM player")
                result = cur.fetchall()
                for row in result:
                    position = row[0]
                print("toimii")
                cur.execute("UPDATE item SET ItemPosition = "+str(position)+" WHERE ItemN='"+str(item)+"'")
                print("toimii2")
        else:
            print("I as a coder have no idea how you got here...")

    elif thing == "room":
        cur.execute("SELECT positionID FROM Player;")
        playerpos = cur.fetchall()
        cur.execute("select RoomDescr from Room where positionID =" + str(playerpos[0][0]))
        kuvaus = cur.fetchall()
        print(str(kuvaus[0][0]))
        cur.execute("select ItemN from Item where itemPosition = " + str(playerpos[0][0]))
        tavarat = cur.fetchall()
        if cur.rowcount >=1:
            print("There are following items in this room:")
            for row in tavarat:
                  print(" - " + str(row[0]))
    
    else:
        print("That cannot be done I'm afraid")

def drop(item):
    cur.execute("SELECT PlayerID FROM item WHERE item.ItemN='"+str(item)+"'")
    result = cur.fetchall()
    if len(result) > 0:
        cur.execute("UPDATE item SET PlayerID = null WHERE ItemN='"+str(item)+"'")
        cur.execute("SELECT PositionID FROM player")
        result = cur.fetchall()
        position = result[0][0]
        cur.execute("UPDATE item SET ItemPosition = "+str(position)+" WHERE ItemN LIKE '"+str(item)+"'")
        print("You dropped the "+str(item)+" on the ground.")

def talking(potion):
    val=val2=val3=val4=val5=val6=0
    cur.execute("SELECT positionID FROM Player;")
    playerpos = cur.fetchall()
    cur.execute("Select isAlive From npc")
    npcstate = cur.fetchall()
    if int(playerpos[0][0]) == 113 and int(npcstate[0][0])==1 and potion == True:
        print("Hello, sir! I've been living in this castle for decades. I have been observing your and your family's life.")
        while val != '1' or val != '2' or val != '3' or val != 'exit': 
            val= input("Please choose one of the following: \n 1. Why can I understand you? \n 2. Can you help me get out of here?\n 3. [attack the rat]")
            if val == '3':
                attack()
            elif val == '1':
                print("You can talk to me because you probably found a magic potion that allows you to talk to animals.")
                val2 = input("1. Where's my family and servants? \n 2. Can you help me get out of here? \n 3. Why would anyone make a potion like that?")
                while val2 != '1' or val2 != '2' or val2 != '3' or val2 != 'exit':
                     if val2 == '1':
                         print("I'm afraid I don't know the answer to that question.")
                         while val4 != '1' or val4 != '2' or val4 != 'exit':
                            val4 = input("1. [attack] \n 2. Can you help me get out of here?")
                            if val4 == '1':
                                 attack()
                            if val4 == '2':
                                print("Yes, I think I can help you but first I have something special for you. Would you like to take this magic drink from me?")
                                val5 = input("1. Yes, I will take the drink \n 2. No, thank you. Just help me get out of here.")
                                while val5 != '1' or val5 != '2' or val5 != 'exit':
                                    if val5 == '1':
                                        print("Great! Here, take a magic drink I have for you.")
                                        print("You drank the magic drink and the drink made you the size of an ant")
                                        print("'I have observed your family's life and created a plan to take over the castle.' said the rat")
                                        print("The rat is now attacking you, due to being so small you are not carrying most of your items anymore.")
                                        #TARKISTA ONKO PELAAJALLA NEULA INVENTORYS JOS ON TULOSTA INVENTORY jos ei tulosta että hän voi taistella käsin
                                    elif val5 == '2':
                                        print("As you please. I think that the key I have on my tail will help you get out. Here you can have it.")
                                        print("The rat dropped a key")
                                        return
                                        #LISÄÄ AVAIMEN PUDOTUS HUONEESEEN
                                    elif val5 == 'exit':
                                        return
                                    else:
                                        print("That is not an option. Please try again")
                        elif val2 == '2':
                                print("Yes, I think I can help you but first I have something special for you. Would you like to take this magic drink from me?")
                                val6 = input("1. Yes, I will take the drink \n 2. No, thank you. Just help me get out of here.")
                                while val6 != '1' or val6 != '2' or val6 != 'exit':
                                    if val6 == '1':
                                        print("Great! Here, take a magic drink I have for you.")
                                        print("You drank the magic drink and the drink made you the size of an ant")
                                        print("'I have observed your family's life and created a plan to take over the castle.' said the rat")
                                        print("The rat is now attacking you, due to being so small you are not carrying most of your items anymore.")
                                        #TARKISTA ONKO PELAAJALLA NEULA INVENTORYS JOS ON TULOSTA INVENTORY jos ei tulosta että hän voi taistella käsin
                                    elif val6 == '2':
                                        print("As you please. I think that the key I have on my tail will help you get out. Here you can have it.")
                                        print("The rat dropped a key")
                                        return
                                        #LISÄÄ AVAIMEN PUDOTUS HUONEESEEN
                                    elif val6 == 'exit':
                                        return
                                    else:
                                        print("That is not an option. Please try again")

                        elif val2 == '3':
                            print("Well, I think that maybe the maker of the potion thought it would be fun to be able to talk to animals.")
                            print("Come back to me if you other questions")
                        elif val2 == 'exit':
                            return
                        else:
                            print("That is not an option. Please try again")
            elif val == '2':
                print("Yes, I think I can help you but first I have something special for you. Would you like to take this magic drink from me?")
                val6 = input("1. Yes, I will take the drink \n 2. No, thank you. Just help me get out of here.")
                while val6 != '1' or val6 != '2' or val6 != 'exit':
                    if val6 == '1':
                        print("Great! Here, take a magic drink I have for you.")
                        print("You drank the magic drink and the drink made you the size of an ant")
                        print("'I have observed your family's life and created a plan to take over the castle.' said the rat")
                        print("The rat is now attacking you, due to being so small you are not carrying most of your items anymore.")
                        #TARKISTA ONKO PELAAJALLA NEULA INVENTORYS JOS ON TULOSTA INVENTORY jos ei tulosta että hän voi taistella käsin
                    elif val6 == '2':
                        print("As you please. I think that the key I have on my tail will help you get out. Here you can have it.")
                        print("The rat dropped a key")
                        return
                        #LISÄÄ AVAIMEN PUDOTUS HUONEESEEN
                    elif val6 == 'exit':
                        return
                    else:
                        print("That is not an option. Please try again")
            elif val == 'exit':
                return
            else:
                print("That is not an option. Please try again.")

#main game loop
while (playerAlive == True):
    command = str(input("Insert command: "))
    command = command.lower()
    for i in [".",",","!","?","'",'"',"(",")","[","]",]:
        command = command.replace(i, "")
    for i in [" a "," an "," the "]:
        command = command.replace(i, " ")
    
    wordCount = len(command.split())
    print(str(wordCount))

    if wordCount == 1:
        #directions you can go to:
        if command == "n" or command == "north":
            move("n")
        elif command == "e" or command == "east":
            move("e")
        elif command == "w" or command == "west":
            move("w")
        elif command == "s" or command == "south":
            move("s")
        elif command == "up" or command == "u":
            move("u")
        elif command == "down" or command == "d":
            move("d")

        elif command == "inventory" or command == "i":
            inventory()
            
        elif command == "help" or command == "h":
            for word in commands:
                print(word)

        elif command == "exit":
            playerAlive = False

        else:
            print("That could not be done I'm afraid")

    if wordCount == 2:
        word1 = command.split(' ',)[0]
        word2 = command.split(' ',)[1]

        if word1 == "examine":
            examine(word2)

        elif word1 == "pick" or word1 == "take":
            pickUp(word2)

        elif word1 == "drop":
            drop(word2)

        elif word1 == "drink":
            print("You drank the "+word2)
        
        elif word1 == "stab" or word1 == "attack":
            attack()

        elif word1 == "talk":
            print("You talked to "+word2)
        
        else:
            print("That could not be done I'm afraid")

    if wordCount == 3:
        word1 = command.split(' ',)[0]
        word2 = command.split(' ',)[1]
        word3 = command.split(' ',)[2]

        if word1 == "pick" and word2 == "up":
            pickUp(word3)

        elif word1 == "talk" and word2 == "to":
            print("You talked to "+word3)

        else:
            print("That could not be done I'm afraid")
          
        
print("goodbye!")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
