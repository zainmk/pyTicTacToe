# Consider the following link
# https://www.skillshare.com/classes/Creating-a-TIC-TAC-TOE-game-using-Python-and-Tkinter/886857159

# Issue where the win window comes up twice.

from tkinter import *
import tkinter.messagebox
from random import randint
import numpy as np
from math import inf as infinity

tk = Tk()
tk.title("Tic Tac Toe")

# Should remove the global variable and pass them as arguments in a function

win = False
clickCounter = 1  # Be careful changing this value, as to determine a tie is to see if clickCounter = 10
buttonsDict = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
winner = "No Winner Yet"

print("Welcome to Tic Tac Toe")
print("Choose a difficultly for the Computer")
print("1. Easy ")
print("2. Medium ")
print("3. Hard")
print("4. Player vs Player")

choice = int(input())


# Note that when you pass buttonsDict[] as board, you're passing the reference to buttonsDict[]
# Make a copy of it to work with so you don't change the actual values.
def hard_computer(board, ):
    pass


def med_computer(board):
    global clickCounter
    global win
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


def easy_computer(board):
    global clickCounter
    global buttonsDict
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


# This function will return True if the game is over, and a winner if there is one
def check_win(board):
    global clickCounter

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

# When the Computer goes first
if clickCounter == 2:
    button1.invoke()  # Invoke the first move the computer should make


tk.mainloop()  # Continuously loops till the GUI is closed.
