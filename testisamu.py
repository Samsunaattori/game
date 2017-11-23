#main game loop
import mysql.connector
db = mysql.connector.connect(host="localhost", user="dbuser",
                             passwd="dbpass", db="omapeli", buffered=True)

cur = db.cursor()

def move(command):
    cur.execute("SELECT positionID FROM Player;")
    playerpos = cur.fetchall()
    print(str(playerpos[0][0]))
    haku = ("SELECT RoomTO FROM Connect where RoomFrom = " + str(playerpos[0][0]) + " and direction='" + str(command) + "'")
    cur.execute(haku)
    destination = cur.fetchall()
    if cur.rowcount == 1:
            liikkuu = ("UPDATE Player set PositionID = " + str(destination[0][0]))
            cur.execute(liikkuu)
            cur.execute("SELECT positionID FROM Player;")
            playerpos = cur.fetchall()
            print(str(playerpos[0][0]))
    else:
        print("You cannot go there, because there is nothing in that direction")
move(input("Enter direction: "))

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
        

playerAlive = True
commands = ["-Possible directions to walk to:","[north]/[n]","[east]/[e]","[west]/[w]",
            "[south]/[s]","[down]","[up]","-To open inventory:","[inventory]/[i]",
            "-To exit game:","[exit]","-To examine an item, room or a container:",
            "[examine (object)]","-To pick up/take an item:",
            "[pick (item)]/[pick up (item)]/[take (item)]","-To drop an item:",
            "[drop (item)]","-To drink something:","[drink (item)]",
            "-To attack/stab something:","[attack (target)]/[stab (target)]",
            "-To talk to someone:","[talk (npc)]/[talk to (npc)]"]


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
            print("pohjoiseen")
        elif command == "e" or command == "east":
            print("itään")
        elif command == "w" or command == "west":
            print("länteen")
        elif command == "s" or command == "south":
            print("etelään")
        elif command == "up":
            print("ylös")
        elif command == "down":
            print("alas")

        elif command == "inventory" or command == "i":
            print("You have the following items: ")
            #sql jol saa kaikki itemit jotka pelaajalla, sit for loopil kaikki nimet

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
            #tarkista onko hyökkäyksen kohde ok!!!

            weapon = input("What would you like to attack with? ")
            print("You attacked "+target+" with a "+word2)

        elif word1 == "talk":
            print("You talked to "+word2)
        
        else:
            print("That could not be done I'm afraid")

    if wordCount == 3:
        word1 = command.split(' ',)[0]
        word2 = command.split(' ',)[1]
        word3 = command.split(' ',)[2]

        if word1 == "pick" and word2 == "up":
            print("You picked up a "+word3)
            pickUp(word2)

        elif word1 == "talk" and word2 == "to":
            print("You talked to "+word3)

        else:
            print("That could not be done I'm afraid")
          
        
print("goodbye!")
    

    
