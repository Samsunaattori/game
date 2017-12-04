#main game loop
import mysql.connector
db = mysql.connector.connect(host="localhost", user="dbuser",
                             passwd="dbpass", db="omapeli", buffered=True)

cur = db.cursor()
playerAlive = True
commands = ["-Possible directions to walk to:","[north]/[n]","[east]/[e]","[west]/[w]",
            "[south]/[s]","[down]/[d]","[up]/[u]","-To open inventory:","[inventory]/[i]",
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
    a1=a2=a3=a4=b1=b2=b3=b4=c1=c2=c3=c4=d1=d2=d3=d4=0
    while not (a1==a2==a3==a4==b1==b4==c1==c4==d1==d2==d3==d4==0 and b2==b3==c2==c3==1):
        print("  "+str(1)+" "+str(2)+" "+str(3)+" "+str(4))
        print("A "+str(a1)+" "+str(a2)+" "+str(a3)+" "+str(a4))
        print("B "+str(b1)+" "+str(b2)+" "+str(b3)+" "+str(b4))
        print("C "+str(c1)+" "+str(c2)+" "+str(c3)+" "+str(c4))
        print("D "+str(d1)+" "+str(d2)+" "+str(d3)+" "+str(d4))

        ruutu = input("Give command: ")

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
def attack():
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
                    print("You killed the rat")
                elif tool == "needle":
                    print("You killed the rat")
                elif tool == "knife":
                    print("The rat is stronger than you and it killed you")
                else:
                    print("You cannot use that to attack")
            else:
                print("You don't have that item")
    else:
        print("There's nobody to attack.")

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
            for row in resultContainer:
                print(row[0])
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
                for row in resultContainer:
                    print(row[0])
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
        if item == "cheese":
            cur.execute("SELECT positionID FROM player")
            result = cur.fetchall()
            if result[0][0] == 113:
                print("A rat comes out of it's hole to eat the cheese. It appears to have a key tied to it's tail!")
    else:
        print("You don't have that with you")

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
          
        
print("goodbye!")
    

    
