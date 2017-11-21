

#main game loop
playerAlive = True
while (playerAlive == True):
    command = str(input("Insert command: "))
    command = command.lower()
    print(command)
    
    wordCount = len(command.split())
    print(str(wordCount))

    if wordCount == 1:
        if command == "n":
            print("pohjoiseen")
        elif command == "s":
            print("etelään")
        elif command == "exit":
            playerAlive = False
        else:
            print("That could not be done I'm afraid")

    if wordCount == 2:
        word1 = command.split(' ',1)[0]
        word2 = command.split(' ',1)[1]

        print(word1)
        print(word2)

        if word1 == "examine":
            print("you examined "+word2)

    if wordCount == 3:
        word1 = command.split(' ',1)[0]
        word2 = command.split(' ',1)[0]
        word3 = command.split(' ',1)[0]

    
        
print("goodbye!")
    

    

    
    



