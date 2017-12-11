import mysql.connector
db = mysql.connector.connect(host="localhost", user="dbuser",
                             passwd="dbpass", db="omapeli", buffered=True)

cur = db.cursor()
playerAlive = True
magicDrink = False
animalDrink = False
commands = ["-Possible directions to walk to:","[north]/[n]","[east]/[e]","[west]/[w]",
            "[south]/[s]","[down]/[d]","[up]/[u]","-To open inventory:","[inventory]/[i]",
            "-Top open a gate:","[open gate]",
            "-To exit game:","[exit]","-To examine an item or a container:",
            "[examine (object)]","-To examine the room you are in:",
            "[examine room]","-To pick up/take an item:",
            "[pick (item)]/[pick up (item)]/[take (item)]","-To drop an item:",
            "[drop (item)]","-To drink something:","[drink (item)]",
            "-To attack/stab something:","[attack (target)]/[stab (target)]",
            "-To talk to someone:","[talk (npc)]/[talk to (npc)]"]
#pelinpulma metodina
def muunna(i):
    return (i+1)%2
def puzzle():
    print("You tried to move west, but there is some kind of a puzzle blocking your path. ([exit] to exit puzzle, [reset] to reset it)")

    a1=a2=a3=a4=b1=b2=b3=b4=c1=c2=c3=c4=d1=d2=d3=d4=0
    while not (a1==a2==a3==a4==b1==b4==c1==c4==d1==d2==d3==d4==0 and b2==b3==c2==c3==1):
        print("  "+str(1)+" "+str(2)+" "+str(3)+" "+str(4))
        print("A "+str(a1)+" "+str(a2)+" "+str(a3)+" "+str(a4))
        print("B "+str(b1)+" "+str(b2)+" "+str(b3)+" "+str(b4))
        print("C "+str(c1)+" "+str(c2)+" "+str(c3)+" "+str(c4))
        print("D "+str(d1)+" "+str(d2)+" "+str(d3)+" "+str(d4))

        ruutu = input("Give a command: ")

        if ruutu == "A1" or ruutu == "a1" or ruutu == "1A" or ruutu == "1a":
            a1 = muunna(a1)
            a2 = muunna(a2)
            b1 = muunna(b1)

        elif ruutu == "A2" or ruutu == "a2" or ruutu == "2A" or ruutu == "2a":
            a1 = muunna(a1)
            a2 = muunna(a2)
            a3 = muunna(a3)
            b2 = muunna(b2)

        elif ruutu == "A3" or ruutu == "a3" or ruutu == "3A" or ruutu == "3a":
            a2 = muunna(a2)
            a3 = muunna(a3)
            a4 = muunna(a4)
            b3 = muunna(b3)

        elif ruutu == "A4" or ruutu == "a4" or ruutu == "4a" or ruutu == "4A":
            a3 = muunna(a3)
            a4 = muunna(a4)
            b4 = muunna(b4)

        elif ruutu == "B1" or ruutu == "b1" or ruutu == "1B" or ruutu == "1b":
            a1 = muunna(a1)
            b1 = muunna(b1)
            b2 = muunna(b2)
            c1 = muunna(c1)

        elif ruutu == "B2" or ruutu == "b2" or ruutu == "2b" or ruutu == "2B":
            a2 = muunna(a2)
            b1 = muunna(b1)
            b2 = muunna(b2)
            b3 = muunna(b3)
            c2 = muunna(c2)

        elif ruutu == "B3" or ruutu == "b3" or ruutu == "3b" or ruutu == "3B":
            a3 = muunna(a3)
            b2 = muunna(b2)
            b3 = muunna(b3)
            b4 = muunna(b4)
            c3 = muunna(c3)

        elif ruutu == "B4" or ruutu == "b4" or ruutu == "4b" or ruutu == "4B":
            a4 = muunna(a4)
            b3 = muunna(b3)
            b4 = muunna(b4)
            c4 = muunna(c4)

        elif ruutu == "C1" or ruutu == "c1" or ruutu == "1c" or ruutu == "1C":
            b1 = muunna(b1)
            c1 = muunna(c1)
            c2 = muunna(c2)
            d1 = muunna(d1)

        elif ruutu == "C2" or ruutu == "c2" or ruutu == "2c" or ruutu == "2C":
            b2 = muunna(b2)
            c1 = muunna(c1)
            c2 = muunna(c2)
            c3 = muunna(c3)
            d2 = muunna(d2)

        elif ruutu == "C3" or ruutu == "c3" or ruutu == "3C" or ruutu == "3c":
            b3 = muunna(b3)
            c2 = muunna(c2)
            c3 = muunna(c3)
            c4 = muunna(c4)
            d3 = muunna(d3)

        elif ruutu == "C4" or ruutu == "c4" or ruutu == "4c" or ruutu == "4C":
            b4 = muunna(b4)
            c3 = muunna(c3)
            c4 = muunna(c4)
            d4 = muunna(d4)

        elif ruutu == "D1" or ruutu == "d1" or ruutu == "1d" or ruutu == "1D":
            c1 = muunna(c1)
            d1 = muunna(d1)
            d2 = muunna(d2)

        elif ruutu == "D2" or ruutu == "d2" or ruutu == "2d" or ruutu == "2D":
            c2 = muunna(c2)
            d1 = muunna(d1)
            d2 = muunna(d2)
            d3 = muunna(d3)

        elif ruutu == "D3" or ruutu == "d3" or ruutu == "3d" or ruutu == "3D":
            c3 = muunna(c3)
            d2 = muunna(d2)
            d3 = muunna(d3)
            d4 = muunna(d4)

        elif ruutu == "D4" or ruutu == "d4" or ruutu == "4d" or ruutu == "4D":
            c4 = muunna(c4)
            d3 = muunna(d3)
            d4 = muunna(d4)
        elif ruutu == "help" or ruutu == "h":
            print("-To reset the puzzle:\n[reset]\n-To exit the puzzle:\n[exit]/[stop]")
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
    haku = ("SELECT RoomTO FROM Connect where RoomFrom = " + str(playerpos[0][0]) + " and direction='" + str(command) + "'")
    cur.execute(haku)
    destination = cur.fetchall()
    if cur.rowcount == 1:
        cur.execute("Select isLocked From Connect where RoomFrom = " + str(playerpos[0][0]) + " and direction='" + str(command) + "'")
        locked = cur.fetchall()
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
            cur.execute("select RoomDescr from Room where positionID =" + str(playerpos[0][0]))
            kuvaus = cur.fetchall()
            cur.execute("Select RoomN from Room where positionID = " + str(playerpos[0][0]))
            loc = cur.fetchall()
            print("You are now in the " + str(loc[0][0]))
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
    #palauttaa stringin, joka kertoo kuoliko joku
    cur.execute("SELECT positionID FROM Player;")
    playerpos = cur.fetchall()
    cur.execute("Select isAlive From npc")
    npcstate = cur.fetchall()
    cur.execute("select itemposition from item where itemn='cheese'")
    cheese = cur.fetchall()
    if str(cheese[0][0]) != 'None':
        if int(playerpos[0][0]) == 113 and int(cheese[0][0]) == 113 and int(npcstate[0][0])==1:
            tool=input("What do you want to use to attack?: ")
            if tool == 'hands' or tool == 'fists' or tool == 'hand' or tool == 'fist':
                print("The rat was stronger than you and you died.")
                return 'playerdead'
            elif tool == 'sword' and magicDrink == True:
                print("You cannot carry a sword because the magic drink made you so small.")
                print("The rat was fast and killed you.")
                return 'playerdead'
            else:
                haku = ("Select PlayerID From Item where ItemN = '" + str(tool) + "'")
                cur.execute(haku)
                tulos = cur.fetchall()
                print(str(tulos))
                if len(tulos)>0:
                    if str(tulos[0][0]) != "None":
                        if tool == "sword" and magicDrink == False:
                            print("You killed the rat")
                            return 'ratdead'
                        elif tool == "needle":
                            print("You killed the rat")
                            return 'ratdead'
                        elif tool == "knife":
                            print("The rat is stronger than you and it killed you")
                            return 'playerdead'
                        else:
                            print("You cannot use that to attack. Please try again.")
                            return 'bothalive'
                    else:
                        print("You don't have that item. Please try again.")
                        return 'bothalive'
                else:
                    print("You don't have that item. Please try again.")
                    return 'bothalive'
        else:
            print("There seems to be nobody to attack.")
            return 'bothalive'
    else:
        print("There seems to be nobody to attack")

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
            cur.execute("UPDATE item SET ItemPosition = "+str(position)+" WHERE ItemN='"+str(item)+"'")
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
                cur.execute("UPDATE item SET ItemPosition = "+str(position)+" WHERE ItemN='"+str(item)+"'")
                
        else:
            print("There is nothing in the "+str(thing))

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
        if item == "cheese":
            cur.execute("SELECT positionID FROM player")
            result = cur.fetchall()
            if result[0][0] == 113:
                print("A rat comes out of it's hole to eat the cheese. It appears to have a key tied to it's tail!")
    else:
        print("You don't have that with you")

def talking(animalDrink, magicDrink):
    val=val2=val3=val4=val5=val6=0
    cur.execute("SELECT positionID FROM Player;")
    playerpos = cur.fetchall()
    cur.execute("Select isAlive From npc")
    npcstate = cur.fetchall()
    cur.execute("select itemposition from item where itemn='cheese'")
    cheese = cur.fetchall()
    if str(cheese[0][0]) != 'None':
        if int(playerpos[0][0]) == 113 and int(cheese[0][0]) == 113 and int(npcstate[0][0])==1 and animalDrink == True:
            print("Hello, sir! I've been living in this castle for decades. I have been observing your and your family's life.")
            while val != '1' or val != '2' or val != '3' or val != 'exit':
                val= input("Please choose one of the following: \n1. Why can I understand you?\n2. Can you help me get out of here?\n3. [attack the rat]\n")
                if val == '1':
                    print("You can talk to me because you probably found a magic potion that allows you to talk to animals.")
                    while val2 != '1' or val2 != '2' or val2 != '3' or val2 != 'exit':
                        val2 = input("1. Where's my family and servants?\n2. Can you help me get out of here?\n3. Why would anyone make a potion like that?\n")
                        if val2 == '1':
                            print("I'm afraid I don't know the answer to that question.")
                            while val3 != '1' or val3 != '2' or val3 != 'exit':
                                val3 = input("1. [attack]\n2. Can you help me get out of here?\n")
                                if val3 == '1':
                                    kill = attack(magicDrink)
                                    return kill
                                if val3 == '2':
                                    print("Yes, I think I can help you but first I have something special for you. Would you like to take this magic drink from me?")
                                    while val5 != '1' or val5 != '2' or val5 != 'exit':
                                        val5 = input("1. Yes, I will take the drink\n2. No, thank you. Just help me get out of here.\n")
                                        if val5 == '1':
                                            print("Great! Here, take a magic drink I have for you.")
                                            magicDrink = True
                                            print("You drank the magic drink and the drink made you the size of an ant")
                                            print("'I have observed your family's life and created a plan to take over the castle.' said the rat")
                                            print("The rat is now attacking you, due to being so small you are not carrying most of your items anymore.")
                                            cur.execute("select playerid from item where itemn='needle'")
                                            needle = cur.fetchall()
                                            if str(needle[0][0]) != 'None':
                                                print("However you are still holding a needle. Maybe you could use it to attack?")
                                                kill = attack(magicDrink)
                                                return kill
                                            else:
                                                kill = attack(magicDrink)
                                                return kill
                                        elif val5 == '2':
                                            print("As you please. I think that the key I have on my tail will help you get out. Here you can have it.")
                                            cur.execute("update item set itemposition = 113 where itemn='key'")
                                            cur.execute("update item set npcid = null where itemn='key'")
                                            print("The rat dropped a key")
                                            return 'bothalive'
                                        elif val5 == 'exit':
                                            print("You ended the conversation with the rat.")
                                            return 'bothalive'
                                        else:
                                            print("That is not an option. Please try again.")
                                            
                                if val3 == 'exit':
                                    print("You ended the conversation with the rat.")
                                    return 'bothalive'
                                else:
                                    print("That is not an option. Please try again.")
                        elif val2 == '2':
                            print("Yes, I think I can help you but first I have something special for you. Would you like to take this magic drink from me?")
                            while val4 != '1' or val4 != '2' or val4 != 'exit':
                                val4 = input("1. Yes, I will take the drink\n2. No, thank you. Just help me get out of here.\n")
                                if val4 == '1':
                                    print("Great! Here, take a magic drink I have for you.")
                                    magicDrink = True
                                    print("You drank the magic drink and the drink made you the size of an ant")
                                    print("'I have observed your family's life and created a plan to take over the castle.' said the rat")
                                    print("The rat is now attacking you, due to being so small you are not carrying most of your items anymore.")
                                    cur.execute("select playerid from item where itemn='needle'")
                                    needle = cur.fetchall()
                                    if str(needle[0][0]) != 'None':
                                        print("However you are still holding a needle. Maybe you could use it to attack?")
                                        kill = attack(magicDrink)
                                        return kill
                                    else:
                                        kill = attack(magicDrink)
                                        return kill
                                elif val4 == '2':
                                    print("As you please. I think that the key I have on my tail will help you get out. Here you can have it.")
                                    cur.execute("update item set itemposition = 113 where itemn='key'")
                                    cur.execute("update item set npcid = null where itemn='key'")
                                    print("The rat dropped a key")
                                    return 'bothalive'
                                elif val4 == 'exit':
                                    print("You ended the conversation with the rat.")
                                    return 'bothalive'
                                else:
                                    print("That is not an option. Please try again.")
                        elif val2 == '3':
                            print("Well, I think that maybe the maker of the potion thought it would be fun to be able to talk to animals.")
                            print("Come back to me if you other questions")
                            return 'bothalive'
                        elif val2 == 'exit':
                            print("You ended the conversation with the rat.")
                            return 'bothalive'
                        else:
                            print("That is not an option. Please try again.")

                elif val == '2':
                    print("Yes, I think I can help you but first I have something special for you. Would you like to take this magic drink from me?")
                    while val6 != '1' or val6 != '2' or val6 != 'exit':
                        val6 = input("1. Yes, I will take the drink\n2. No, thank you. Just help me get out of here.\n")
                        if val6 == '1':
                            print("Great! Here, take a magic drink I have for you.")
                            magicDrink = True
                            print("You drank the magic drink and the drink made you the size of an ant")
                            print("'I have observed your family's life and created a plan to take over the castle.' said the rat")
                            print("The rat is now attacking you, due to being so small you are not carrying most of your items anymore.")
                            cur.execute("select playerid from item where itemn='needle'")
                            needle = cur.fetchall()
                            if str(needle[0][0]) != 'None':
                                print("However you are still holding a needle. Maybe you could use it to attack?")
                                kill = attack(magicDrink)
                                return kill
                            else:
                                kill = attack(magicrink)
                                return kill
                        elif val6 == '2':
                            print("As you please. I think that the key I have on my tail will help you get out. Here you can have it.")
                            cur.execute("update item set itemposition = 113 where itemn='key'")
                            cur.execute("update item set npcid = null where itemn='key'")
                            print("The rat dropped a key")
                            return 'bothalive'
                        elif val6 == 'exit':
                            print("You ended the conversation with the rat.")
                            return 'bothalive'
                        else:
                            print("That is not an option. Please try again.")
                elif val == '3':
                    kill = attack(magicDrink)
                    return kill
                elif val == 'exit':
                    print("You ended the conversation with the rat.")
                    return 'bothalive'
                else:
                    print("That is not an option. Please try again.")
        else:
            print("There seems to be nobody to talk to.")
            return 'bothalive'
    else:
            print("There seems to be nobody to talk to.")
            return 'bothalive'

def openGate():
    cur.execute("SELECT PositionID FROM player WHERE PositionID = 121")
    result = cur.fetchall()
    if len(result) > 0:
        print("toimii1")
        cur.execute("SELECT ItemN FROM item WHERE PlayerID = 1 AND ItemN = 'key'")
        print("toimii2")
        result = cur.fetchall()
        if len(result) > 0:
            return 'won'
        else:
            return 'noKey'
    else:
        return 'noGate'

print("It is early late morning. Tim, the 12 year old boy who you play as, has just woken up from his bed, and \
to his surprise it seems to be almost noon already. This is unusual, because one of his servants usually \
wakes him up at 9am. After waiting for a while, he starts to yell demanding for someone to come help him \
up from his bed, but nobody answers. An hour later, bored to death, he finally rises from his bed on his own, \
ready to find something to do. \n Two hours later, still nothing. Not a soul seems to realize he is here. \
Then he finally realized, that if there is no-one to help him, there propably is no-one to stop him from \
doing whatever he wants. 'With everyone gone, maybe I could finally get out of the castle and see what the \
world really looks like!' And so he becan his quest of wcaping the castle.")
examine("room")

#main game loop
while (playerAlive == True):
    command = str(input("Insert command: "))
    command = command.lower()
    for i in [".",",","!","?","'",'"',"(",")","[","]",]:
        command = command.replace(i, "")
    for i in [" a "," an "," the "]:
        command = command.replace(i, " ")
    
    wordCount = len(command.split())

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
            x = input("What would you like to drink?")
            if x == "potion" or x == "magic potion" or x == "drink" or x == "magic drink":
                cur.execute("Select playerID from item where itemn = 'potion'")
                res=cur.fetchall()
                if str(res[0][0]) != "None":
                    animalDrink = True
                    print("You drank the magic potion and can now talk to animals.")
                else:
                    print("You don't have anything to drink")
            else:
                print("You cannot drink that.")

        elif word1 == "open" and word2 == "gate":
            isOpened = openGate()
            if isOpened == 'won':
                print("You won the game!")
            elif isOpened == 'noKey':
                print("You don't have the gate key")
            elif isOpened == 'noGate':
                print("You don't see a gate you could open here")
                wonGame = True
                playerAlive = False
        
        elif word1 == "stab" or word1 == "attack":
            resattack = attack(magicDrink)
            if resattack == 'ratdead':
                cur.execute("Update npc set isAlive = 1 where npcN = 'rat'")
                magicDrink = False
                cur.execute("update item set itemposition = 113 where itemn='key'")
                cur.execute("update item set npcid = null where itemn='key'")
                print("The rat dropped a key")
            if resattack == 'playerdead':
                playerAlive = False

        elif word1 == "talk":
            restalk = talking(animalDrink, magicDrink)
            if restalk == 'ratdead':
                cur.execute("Update npc set isAlive = 1 where npcN = 'rat'")
                magicDrink = False
                cur.execute("update item set itemposition = 113 where itemn='key'")
                cur.execute("update item set npcid = null where itemn='key'")
                print("The rat dropped a key")
        
        else:
            print("That could not be done I'm afraid")

    if wordCount == 3:
        word1 = command.split(' ',)[0]
        word2 = command.split(' ',)[1]
        word3 = command.split(' ',)[2]

        if word1 == "pick" and word2 == "up":
            pickUp(word3)

        elif word1 == "talk" and word2 == "to":
            restalk = talking(animalDrink, magicDrink)
            if restalk == 'ratdead':
                cur.execute("Update npc set isAlive = 1 where npcN = 'rat'")
                magicDrink = False
                cur.execute("update item set itemposition = 113 where itemn='key'")
                cur.execute("update item set npcid = null where itemn='key'")
                print("The rat dropped a key")
                
            if restalk == 'playerdead':
                playerAlive = False

        else:
            print("That could not be done I'm afraid")
print("Game over!")
