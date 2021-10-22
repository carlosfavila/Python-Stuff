# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 08:46:20 2021

@author: CarlosFavila
"""
from random import randrange

board = [['1','2','3'],['4','5','6'],['7','8','9']]
     
def DisplayBoard(board):
    print('+-------+-------+-------+')
    for i in range(len(board)):
        f1, f2, f3 = board[i]
        print("""|       |       |       |
|   %s   |   %s   |   %s   |
|       |       |       |"""%(str(f1),str(f2),str(f3)))
        print('+-------+-------+-------+')
            

def EnterMove(board):
    casilla = input('Ingresa una casilla: ')
    while casilla not in numbers:
        casilla = input('Ésa casilla ya está ocupada, ingresa otra: ')
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == casilla:
                board[i][j] = 'O'

def MakeListOfFreeFields(board):
    global numbers 
    numbers = []
    indexes = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 'X' and board[i][j] != 'O':
                numbers.append(board[i][j])
                indexes.append((i,j))
                
              
def VictoryFor(board):
    
    for columna in range(len(board[0])):#analiza las columnas
        c1, c2, c3 = board[0][columna], board[1][columna], board[2][columna]
        if c1==c2 and c1==c3:
            return (False,c1)
    
    for fila in range(len(board)):#Analiza las filas
        c1,c2,c3 = board[fila]
        if c1==c2 and c1==c3:
            return (False,c1)

        
    return(True,'0')
    
    
    
    
def DrawMove(board):
    isin=True
    while isin:
        randnum = str(randrange(1,10))
        if randnum in numbers: isin=False
         
    for i in range(len(board)):
        for j in range(len(board)):
            if str(randnum)==board[i][j]:
                board[i][j]='X'
    



print('\t\t\t TIC TAC TOE\n')  
print('Comienza la Máquina')
state = True

while state==True:
    
    MakeListOfFreeFields(board)
    if numbers == []:
        break
    DrawMove(board)
    DisplayBoard(board)
    MakeListOfFreeFields(board)
    state, win= VictoryFor(board)
    if numbers == []:
        break
    
    EnterMove(board)
    DisplayBoard(board)
    MakeListOfFreeFields(board)
    state, win= VictoryFor(board)
    if numbers == []:
        break
    
if win!='0':
    print('¡GANAN LAS %s!'%win)
else: print('¡EMPATE!')
