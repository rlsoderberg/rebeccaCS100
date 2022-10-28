type = ["0", "Uppercase", "Lowercase", "Title Case"]

print("You enter an aviary with three doors. Which will it be?")
turncount = 0

#input functions
def inputio():
    valid = False
    while valid == False:
        try:
            door = input("1, 2, or 3?")
            inte = int(door)
            valid = True
        except ValueError:
            print("Invalid Input!")
    return inte

def input2():
    x = inputio()
    while x == "":
        print("I didn't hear you!")
        x = inputio()
    return x

def input3():
    inte = input2()
    while inte < 1 or inte > 3:
        print("Not that many doors!")
        inte = input2()
    return inte

#door related occurences
def doorhappen(turncount):
    inte = input3()
    
    print("As you step closer to door ",inte,", you can read the sign on it: ",type[inte])
    print("You open the door, and a bird swoops down in front of you.")

    #introduce program, request user input
    print("Hello! I'm the",type[inte],"parrot!")
    #i skipped some checks with this one, but i just figured, like, it works ok i guess
    user_status = input("How are you doing today? ")
    #split user input at spaces
    array = user_status.split(" ")
    #convert words to uppercase
    if inte == 1:
        print(array[0].upper(), "\n", array[0].upper(), "\n")
        for s in array:
            print(s.upper())
    elif inte == 2:
        print(array[0].lower(), "\n", array[0].lower(), "\n")
        for s in array:
            print(s.lower())
    elif inte == 3:
        print(array[0].title(), "\n", array[0].title(), "\n")
        for s in array:
            print(s.title())

    print("You step back out of the door.")
    turncount += 1
    return turncount

#slight glitch in loop for some reason
turncount = doorhappen(turncount)
while turncount < 4:
    print("Which door will it be?")
    doorhappen(turncount)
