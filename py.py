import time
#importing time

TwoDListArray = [
        ["r1c1", "r1c2", "r1c3"],
        ["r2c1", "r2c2", "r2c3"],
        ["r3c1", "r3c2", "r3c3"]
    ]
#for 2d list

while True:
#repeats



    
    
    

    print("Player 1 pick a position: ")
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    row = row - 1
    column = column - 1
    #selects row and column


    if TwoDListArray[row][column] != "x":

        TwoDListArray[row][column] = "o"

        for elements in TwoDListArray:
                print(elements)

    #changes and prints the list
        

    if TwoDListArray[row][column] == "x":
        print("invalid space, choose another space")
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        row = row - 1
        column = column - 1
        if TwoDListArray[row][column] != "x":
            TwoDListArray[row][column] = "o"
        for elements in TwoDListArray:
            print(elements)


    elif TwoDListArray[0][0] == "x":
            if TwoDListArray[0][1] == "x":
                if TwoDListArray[0][2] == "x":
                    print("X won")

    elif TwoDListArray[1][0] == "x":
                if TwoDListArray[1][1] == "x":
                    if TwoDListArray[1][2] == "x":
                        print("X won")

    elif TwoDListArray[2][0] == "x":
        if TwoDListArray[2][1] == "x":
            if TwoDListArray[2][2] == "x":
                print("X won")

    elif TwoDListArray[0][0] == "o":
                if TwoDListArray[0][1] == "o":
                    if TwoDListArray[0][2] == "o":
                        print("O won")

    elif TwoDListArray[1][0] == "o":
                if TwoDListArray[1][1] == "o":
                    if TwoDListArray[1][2] == "o":
                        print("O won")

    elif TwoDListArray[2][0] == "o":
        if TwoDListArray[2][1] == "o":
            if TwoDListArray[2][2] == "o":
                print("O won")


    



    
        

    
    


        




    


    print("Player 2 pick a position: ")
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    row = row - 1
    column = column - 1

    if TwoDListArray[row][column] != "o":

        TwoDListArray[row][column] = "x"
        for elements in TwoDListArray:
            print(elements)

    if TwoDListArray[row][column] == "o":
        print("invalid space, choose another space")
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        row = row - 1
        column = column - 1
        if TwoDListArray[row][column] != "o":
            TwoDListArray[row][column] = "x"
        for elements in TwoDListArray:
            print(elements)


    elif TwoDListArray[0][0] == "x":
            if TwoDListArray[0][1] == "x":
                if TwoDListArray[0][2] == "x":
                    print("X won")

    elif TwoDListArray[1][0] == "x":
                if TwoDListArray[1][1] == "x":
                    if TwoDListArray[1][2] == "x":
                        print("X won")

    elif TwoDListArray[2][0] == "x":
        if TwoDListArray[2][1] == "x":
            if TwoDListArray[2][2] == "x":
                print("X won")

    elif TwoDListArray[0][0] == "o":
            if TwoDListArray[0][1] == "o":
                if TwoDListArray[0][2] == "o":
                    print("O won")

    elif TwoDListArray[1][0] == "o":
                if TwoDListArray[1][1] == "o":
                    if TwoDListArray[1][2] == "o":
                        print("O won")

    elif TwoDListArray[2][0] == "o":
        if TwoDListArray[2][1] == "o":
            if TwoDListArray[2][2] == "o":
                print("O won")

                


            







            

    
    



        




    

