from random import randrange
import time

def DisplayBoard(board):
    print(
    """
    +-------+-------+-------+
    |       |       |       |
    |  """,lst[0][0], """  |  """,lst[0][1], """  |  """,lst[0][2], """  |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |  """,lst[1][0], """  |  """,lst[1][1], """  |  """,lst[1][2], """  |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |  """,lst[2][0], """  |  """,lst[2][1], """  |  """,lst[2][2], """  |
    |       |       |       |
    +-------+-------+-------+
    """
    )

    

def VicrotyFor(board):
    print("Checking")
    time.sleep(1)
    if lst[0][0]==lst[0][1]==lst[0][2]:
        if lst[0][1]=="O":
            win = "Computer"
        elif lst[0][1]=="X":
            win = "YoU"
    elif lst[1][0]==lst[1][1]==lst[1][2]:
        if lst[1][1]=="O":
            win = "Computer"
        elif lst[1][1]=="X2":
            win = "YoU"
    elif lst[2][0]==lst[2][1]==lst[2][2]:
        if lst[2][1]=="O":
            win = "Copuuter"
        elif lst[2][1]=="X3":
            win = "YoU"
            
    elif lst[0][0]==lst[1][0]==lst[2][0]:
        if lst[0][0]=="O":
            win = "Computer"
        elif lst[0][0]=="X":
            win = "YoU"
    elif lst[0][1]==lst[1][1]==lst[2][1]:
        if lst[0][1]=="O":
            win = "Computer"
        elif lst[0][1]=="X":
            win = "YoU"
    elif lst[0][2]==lst[1][2]==lst[2][2]:
        if lst[0][2]=="O":
            win = "Copuuter"
        elif lst[0][2]=="X":
            win = "YoU"
            
    elif lst[0][0]==lst[1][1]==lst[2][2]:
        if lst[0][0]=="O":
            win = "Copuuter"
        elif lst[0][0]=="X":
            win = "YoU"
    elif lst[0][2]==lst[1][1]==lst[2][1]:
        if lst[0][2]=="O":
            win = "Copuuter"
        elif lst[0][2]=="X":
            win = "YoU"
    
    
            
    else:
        win = False
        
    if win != False or len(lst1)==9:
        print("<<----------",win,"WIN---------->>")
        print("<<----------GAME OVER---------->>")
        exit(0)
    else:
        return None
        

def EnterMove(board):
    global lst1
    x = int(input("Enter your move...(1-9) : "))
    while x in lst1 or x>9 or x <1:
        x = int(input("Try Different Option... : "))
        if x not in lst1:
            break
    lst1.append(x)
    if x<=3:
        lst[0][x-1] = "X"
    elif x>3 and x<=6:
        lst[1][(x%3)-1] = "X"
    else:
        lst[2][(x%3)-1] = "X"
    DisplayBoard(lst)
    VicrotyFor(lst)

    
def DrawMove(board):
    for i in range(len(lst1)):
        com = randrange(1,9)
        #print(lst1)
        #print("Please Wait ")
        while com in lst1:
            #print(". ")
            com = randrange(1,9)
            if com not in lst1:
                break
    print("Computer's Move : ",com)
    lst1.append(com)
    if com<=3:
        lst[0][com-1] = "O"
    elif com>3 and com<=6:
        lst[1][(com%3)-1] = "O"
    else:
        lst[2][(com%3)-1] = "O"
    DisplayBoard(lst)
    VicrotyFor(lst)
    
    
lst=[[1,2,3],[4,5,6],[7,8,9]]
lst1=[]
print("<<-------- Game STARTED -------->>")
DisplayBoard(lst)
while(len(lst1)<=9):
    EnterMove(lst)
    DrawMove(lst)
    print(lst1)
print("Game Over.....")
