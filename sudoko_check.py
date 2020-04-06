import time


def DisplayBoard(board):
    print(
    """
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |     |     |     |     |     |     |
    | """,lst[0][0], """ | """,lst[0][1], """ | """,lst[0][2], """ | """,lst[0][3], """ | """,lst[0][4], """ | """,lst[0][5], """ | """,lst[0][6], """ | """,lst[0][7], """ | """,lst[0][8], """ |
    |     |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |     |     |     |     |     |     |
    | """,lst[1][0], """ | """,lst[1][1], """ | """,lst[1][2], """ | """,lst[1][3], """ | """,lst[1][4], """ | """,lst[1][5], """ | """,lst[1][6], """ | """,lst[1][7], """ | """,lst[1][8], """ |
    |     |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |     |     |     |     |     |     |
    | """,lst[2][0], """ | """,lst[2][1], """ | """,lst[2][2], """ | """,lst[2][3], """ | """,lst[2][4], """ | """,lst[2][5], """ | """,lst[2][6], """ | """,lst[2][7], """ | """,lst[2][8], """ |
    |     |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |     |     |     |     |     |     |
    | """,lst[3][0], """ | """,lst[3][1], """ | """,lst[3][2], """ | """,lst[3][3], """ | """,lst[3][4], """ | """,lst[3][5], """ | """,lst[3][6], """ | """,lst[3][7], """ | """,lst[3][8], """ |
    |     |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |     |     |     |     |     |     |
    | """,lst[4][0], """ | """,lst[4][1], """ | """,lst[4][2], """ | """,lst[4][3], """ | """,lst[4][4], """ | """,lst[4][5], """ | """,lst[4][6], """ | """,lst[4][7], """ | """,lst[4][8], """ |
    |     |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |     |     |     |     |     |     |
    | """,lst[5][0], """ | """,lst[5][1], """ | """,lst[5][2], """ | """,lst[5][3], """ | """,lst[5][4], """ | """,lst[5][5], """ | """,lst[5][6], """ | """,lst[5][7], """ | """,lst[5][8], """ |
    |     |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |     |     |     |     |     |     |
    | """,lst[6][0], """ | """,lst[6][1], """ | """,lst[6][2], """ | """,lst[6][3], """ | """,lst[6][4], """ | """,lst[6][5], """ | """,lst[6][6], """ | """,lst[6][7], """ | """,lst[6][8], """ |
    |     |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |     |     |     |     |     |     |
    | """,lst[7][0], """ | """,lst[7][1], """ | """,lst[7][2], """ | """,lst[7][3], """ | """,lst[7][4], """ | """,lst[7][5], """ | """,lst[7][6], """ | """,lst[7][7], """ | """,lst[7][8], """ |
    |     |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |     |     |     |     |     |     |
    | """,lst[8][0], """ | """,lst[8][1], """ | """,lst[8][2], """ | """,lst[8][3], """ | """,lst[8][4], """ | """,lst[8][5], """ | """,lst[8][6], """ | """,lst[8][7], """ | """,lst[8][8], """ |
    |     |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+

    """
    )
    return True

def row_check(lst_check):
    flag = 1
    check = [1,2,3,4,5,6,7,8,9]
    for i in lst_check:
        if i in check:
            check.remove(i)
            continue
        elif i not in check:
            flag = 0
            break
    if flag==1:
        print("True")
        return True
    else:
        return False


def flag_check(a):
    if a==1:
        return True
    else:
        return False
            
        
    

lst = []
lst_check = []
flag=1
for i in range(9):
    for j in range(1):
        x = input("Enter elements of " + str(i+1) + " row : ")
        x = " ".join(x)
        lst1 = list(x.split(" "))
        lst.append(lst1)
    #print(lst)       
disp = DisplayBoard(lst)

'''for i in range(9):
    for j in range(9):
        lst_check.append(int(lst[i][j]))

    ch = row_check(lst_check)
    lst_check=[]
    if ch == False:
        flag = 0
        break
    else:
        continue

if ch==True:
    print("All Rows follow sudoko rule")
    print("Please wait for column check")
    time.sleep(1)
    for i in range(9):
        for j in range(9):
            lst_check.append(int(lst[j][i]))
        #print(lst_check)
        ch = row_check(lst_check)
        lst_check=[]
        if ch == False:
            flag = 0
            break
        else:
            continue'''
ch=True
if ch==True:
    print("All Column follow sudoko rule")
    print("Please wait for column check")
    time.sleep(1)
    a=0
    b=3
    for k in range(3):
        #print(a,b)
        for i in range(a,b):
            for j in range(a,b):
                print(i,j)
                lst_check.append(int(lst[i][j]))
        print(lst_check)
        #ch = row_check(lst_check)
        lst_check=[]
        a = b
        b += 3
        
            

elif ch==0:
    print("Game OVER")
    






