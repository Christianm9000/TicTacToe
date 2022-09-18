#Initialize Variables
board = [1,2,3,4,5,6,7,8,9] #Board as a string, otherwise board = [[1,2,3], [4,5,6], [7,8,9]]
userinput = 0 #The users input, edited later
userturn = 0 #userturn, defines who's turn it is.


#Check Win Function
def checkwin(board, win):
    
    #Check win Horizontally
    for i in range(3):
        i *= 3 #Change the row when i is above 0
        if board[i] == "X" and board[i+1] == "X" and board[i+2] == "X": #check term in row, example. 0, 1, 2 or 3, 4, 5.
            print("Player 1 has won the game!")
            win = True
            break
        if board[i] == "O" and board[i+1] == "O" and board[i+2] == "O": #Check the same for player 2
            print("Player 2 has won the game!")
            win = True
            break
    
    #Check win Vertically
    for i in range(3): #Check for the 3 columns
        if board[i] == "X" and board[i+3] == "X" and board[i+6] == "X" : #Check if player 1 wins
            print("Player 1 has won the game!")
            win = True
            break
        if board[i] == "O" and board[i+3] == "O" and board[i+6] == "O" : #Check if player 2 wins
            print("Player 2 has won the game!")
            win = True
            break
    
    #Check win diagonally
    for i in range(2): #Check the 2 diagonals
        if i == 0 and board[i] == "X" and board[i+4] == "X" and board[i+8] == "X" : #Check Left to right diagonal, player 1
            print("Player 1 has won the game!")
            win = True
            break
        if i == 0 and board[i] == "O" and board[i+4] == "O" and board[i+8] == "O" : #Check left to right diagonal, player 2
            print("Player 2 has won the game!")
            win = True
            break
        if i == 1 and board[i+1] == "X" and board[i+3] == "X" and board[i+5] == "X" : #Check right to left diagonal, Player 1
            print("Player 1 has won the game!")
            win = True
            break
        if i == 1 and board[i+1] == "O" and board[i+3] == "O" and board[i+5] == "O" : #Check right to left diagonal, Player 2
            print("Player 2 has won the game!")
            win = True
            break

    return(win) #Return win value, True if game has to end.



#Draw Board
def drawboard(board):
    print('')
    print('')
    for i in range(3):
        i *= 3
        print(f"| {board[i]} | {board[i +1]} | {board[i +2]} |")
    
    print('')


#Get Userinput 
def user(board, userturn, win):

    #Define variables
    userinput = 0
    tempboard = []

    #What options are available
    for i in range(9):
        if type(board[i]) == int:
            tempboard.append(board[i])
    
    #Check Draw
    if len(tempboard) == 0: #If tempboard is empty (no user inputs left) call draw.
        print("Draw!")
        win = True

    #Start Userinput
    while True:
        try:
            if userturn % 2 == 0 and win == False:
                print(f"Pick one of: {tempboard}")
                userinput = int(input("Player 1: "))
                while userinput < 1 or userinput > 9 or userinput not in tempboard:
                    print(f"Pick one of: {tempboard}")
                    userinput = int(input("Player 1: "))
                board[userinput-1] = "X"
                break


            if userturn % 2 != 0 and win == False:
                print(f"Pick one of: {tempboard}")
                userinput = int(input("Player 2: "))
                while userinput < 1 or userinput > 9 or userinput not in tempboard:
                    print(f"Pick one of: {tempboard}")
                    userinput = int(input("Player 2: "))
                board[userinput-1] = "O"
                break

        except ValueError:
            print('')

    #Draw board again
    drawboard(board)
    
    #Do Next player
    userturn += 1

    #Return important edited values
    return board, userturn, win

#Main Game runner, controls the game
def tictactoe(board, userturn):
    win = False
    drawboard(board)
    while win == False:
        win = checkwin(board, win)
        if win == False:
            board, userturn, win = user(board, userturn, win)

#Start the Game
tictactoe(board, userturn)