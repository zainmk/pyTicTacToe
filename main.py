# --------------------------------------------------------------------------------------------------------------------#
#                                                   pyTicTacToe
# This code simulates a game of Tic Tac Toe, with various difficulties of computer that the player can play against, or
#                       the player can play against another human player if he/she so chooses.
# --------------------------------------------------------------------------------------------------------------------#

from tkinter import *
import tkinter.messagebox
from random import randint
import numpy as np
from math import inf as infinity

MAX = 1
MIN = -1


tk = Tk()
tk.title("Tic Tac Toe")

clickCounter = 1
buttonsDict = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

print("Welcome to Tic Tac Toe")
print("Choose a difficultly for the Computer")
print("1. Easy ")
print("2. Medium ")
print("3. Hard")
print("4. Player vs Player")

choice = int(input())

# Using the recursive MINIMAX game theory for the hard_comp() function.
def minimax(board, depth, player):
    if player == MAX:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    # Need to convert matrix back to boardDict
    boardDict = {}
    for i in range(0, 3):
        for j in range(0, 3):
            indexNumber = i*3 + j + 1
            if board[i][j] == 0:
                boardDict[indexNumber] = " "
            elif board[i][j] == 1:
                boardDict[indexNumber] = "O"
            elif board[i][j] == -1:
                boardDict[indexNumber] = "X"

    win, winner = check_win(boardDict)

    if depth == 0 or win:
        if winner == "X":  # If the person wins this state
            return [-1, -1, -1]
        elif winner == "O":  # If the computer wins this state
            return [-1, -1, 1]
        else:  # If the game ends as a tie, otherwise winner = "Tie"
            return [-1, -1, 0]

    emptyCells = []
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == 0:
                emptyCells.append([x, y])

    for cell in emptyCells:
        x, y = cell[0], cell[1]
        board[x][y] = player  # Player is designated as 1 or -1, the state of the board needs a numeric evaluation
        score = minimax(board, depth - 1, -player)
        board[x][y] = 0

        score[0], score[1] = x, y

        if player == MAX:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score
    return best


# The following function is for the hard_computer() option. The computer in this case uses the minimax game theory. In
# the case of a 2 player game, such as Tic Tac Toe, the computer evaluates states of the game from the potential moves
# it could make, and the potential moves the player could respond with. After playing out these game states, the
# computer chooses the move that would result it to either win or draw (with a preference for win) and in the fewest
# moves possible.
def hard_computer(board):
    # We make a copy of the current state of the board and input it into the minimax function
    newBoard = {}
    for x in board:
        newBoard[x] = board[x]

    # We convert the current state of the board to a 3 by 3 matrix for minimax to evaluate the states. + 1 is for the
    # computer while -1 is designated for the player.
    boardMatrix = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
    counter = 0
    for i in range(0, 3):
        for j in range(0, 3):
            counter = counter + 1
            if newBoard[counter] == "X":
                boardMatrix[i][j] = -1
            elif newBoard[counter] == "O":
                boardMatrix[i][j] = 1
            else:
                boardMatrix[i][j] = 0

    # The initial depth of the minimax tree has the potential to go as far as there are remaining moves to make in the
    # game. We use the current state of the clickCounter to determine the remaining amount of moves.

    initialDepth = 10 - clickCounter

    # bestMove returns an index point of a 3 by 3 matrix, we convert it back to our move selection format (1-9)
    bestMove = minimax(boardMatrix, initialDepth, MAX)
    bestIndexPoint = bestMove[0]*3 + bestMove[1] + 1

    if bestIndexPoint == 1:
        button1.invoke()
    if bestIndexPoint == 2:
        button2.invoke()
    if bestIndexPoint == 3:
        button3.invoke()
    if bestIndexPoint == 4:
        button4.invoke()
    if bestIndexPoint == 5:
        button5.invoke()
    if bestIndexPoint == 6:
        button6.invoke()
    if bestIndexPoint == 7:
        button7.invoke()
    if bestIndexPoint == 8:
        button8.invoke()
    if bestIndexPoint == 9:
        button9.invoke()


# med_computer() randomly selects one of the free available choices it could make, and places its marker in that spot.
def med_computer(board):
    randomNumber = 0

    while randomNumber == 0:
        randomNumber = randint(1, 9)
        if board[randomNumber] == " ":
            break
        else:
            randomNumber = 0

    if randomNumber == 1:
        button1.invoke()
    if randomNumber == 2:
        button2.invoke()
    if randomNumber == 3:
        button3.invoke()
    if randomNumber == 4:
        button4.invoke()
    if randomNumber == 5:
        button5.invoke()
    if randomNumber == 6:
        button6.invoke()
    if randomNumber == 7:
        button7.invoke()
    if randomNumber == 8:
        button8.invoke()
    if randomNumber == 9:
        button9.invoke()


# easy_computer is where the computer simply chooses the next available empty spot.
def easy_computer(board):
    nextButton = 0

    for x in range(1, 10):
        if board[x] == " ":
            nextButton = x
            break

    if nextButton == 1:
        button1.invoke()
    if nextButton == 2:
        button2.invoke()
    if nextButton == 3:
        button3.invoke()
    if nextButton == 4:
        button4.invoke()
    if nextButton == 5:
        button5.invoke()
    if nextButton == 6:
        button6.invoke()
    if nextButton == 7:
        button7.invoke()
    if nextButton == 8:
        button8.invoke()
    if nextButton == 9:
        button9.invoke()


# check_win() determines if there is a winner for the current state of the game as well as who that winner is
def check_win(board):
    if board[1] != " " and board[1] == board[2] == board[3]:
        return True, board[1]
    elif board[4] != " " and board[4] == board[5] == board[6]:
        return True, board[4]
    elif board[7] != " " and board[7] == board[8] == board[9]:
        return True, board[7]
    elif board[1] != " " and board[1] == board[4] == board[7]:
        return True, board[1]
    elif board[2] != " " and board[2] == board[5] == board[8]:
        return True, board[2]
    elif board[3] != " " and board[3] == board[6] == board[9]:
        return True, board[3]
    elif board[1] != " " and board[1] == board[5] == board[9]:
        return True, board[1]
    elif board[3] != " " and board[3] == board[5] == board[7]:
        return True, board[3]
    elif clickCounter == 10:
        return True, "Tie"
    else:
        return False, "No"


# clicker() is the main driving function of the game. Every click that is made on a button on the GUI leads to this
# function, where the computer can respond and determine if there is a winner.
def clicker(buttons, number):
    global clickCounter
    global buttonsDict
    global choice

    if buttons["text"] == " " and (clickCounter % 2):
        buttonsDict[number] = "X"
        buttons["text"] = buttonsDict[number]
        clickCounter = clickCounter + 1

        if choice == 1 and not check_win(buttonsDict)[0]:
            easy_computer(buttonsDict)
        if choice == 2 and not check_win(buttonsDict)[0]:
            med_computer(buttonsDict)
        if choice == 3 and not check_win(buttonsDict)[0]:
            hard_computer(buttonsDict)

    elif buttons["text"] == " " and not (clickCounter % 2):
        buttonsDict[number] = "O"
        buttons["text"] = buttonsDict[number]
        clickCounter = clickCounter + 1

    _win, _winner = check_win(buttonsDict)

    if _win:
        if _winner == "Tie":
            tkinter.messagebox.showinfo("Game Over!", "The game is a TIE!")
            tk.quit()
        else:
            tkinter.messagebox.showinfo("Congratulations!", _winner + " is the winner!")
            tk.quit()


# The following create the buttons on the tkinter GUI that is displayed to the user.
button1 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: clicker(button1, 1))
button1.grid(row=0, column=0, sticky=S+N+E+W)

button2 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: clicker(button2, 2))
button2.grid(row=0, column=1, sticky=S+N+E+W)

button3 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: clicker(button3, 3))
button3.grid(row=0, column=2, sticky=S+N+E+W)

button4 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: clicker(button4, 4))
button4.grid(row=1, column=0, sticky=S+N+E+W)

button5 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: clicker(button5, 5))
button5.grid(row=1, column=1, sticky=S+N+E+W)

button6 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: clicker(button6, 6))
button6.grid(row=1, column=2, sticky=S+N+E+W)

button7 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: clicker(button7, 7))
button7.grid(row=2, column=0, sticky=S+N+E+W)

button8 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: clicker(button8, 8))
button8.grid(row=2, column=1, sticky=S+N+E+W)

button9 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: clicker(button9, 9))
button9.grid(row=2, column=2, sticky=S+N+E+W)

tk.mainloop()  # Continuously loops till the GUI is closed.
