#main game loop
import mysql.connector
db = mysql.connector.connect(host="localhost", user="dbuser",
                             passwd="dbpass", db="omapeli", buffered=True)

cur = db.cursor()
playerAlive = True
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
            print("You examined the "+word2)

        elif word1 == "pick" or word1 == "take":
            pickUp(word2)

        elif word1 == "drop":
            print("You dropped the "+word2)

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
    

    
