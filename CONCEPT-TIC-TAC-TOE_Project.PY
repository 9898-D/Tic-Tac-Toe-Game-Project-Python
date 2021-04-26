

def display(board):
    print(board[1]+ "|" +board[2]+ "|" +board[3])
    print("-----")
    print(board[4]+ "|" +board[5]+ "|" +board[6])
    print("-----")
    print(board[7]+ "|" +board[8]+ "|" +board[9])

#display(['#','1','2','3','4','5','6','7','8','9'])
board=['#','1','2','3','4','5','6','7','8','9']

def user_choice():
    choice="WROMG"
    while choice not in ['1','2','3','4','5','6','7','8','9']:
        
        choice=input("Enter the Position Bet (1 TO 9): ")
        
        if choice not in ['1','2','3','4','5','6','7','8','9']:
            print("Sorry Invalid! Number Must in Rang")
        
        
    return int(choice)
#print(user_choice())



def replacemen(board,post):
    marker=input("Enter The String: ")
    board[post]=marker
    return board

#print(replacemen(board,2))
#display(board)


def ply_again():
    
    choice="WROMG"
    
    while choice not in ['Y','N']:
        choice=input("Would You like PlAY Again (Y OR N): ")
    
        if choice not in ['Y','N']:
            print("Sorry I Dont Understand! (Y OR N) ")
    
    if choice=='Y':
        return game_one==True
    else:
        return game_one==False


#### GAME LOGIC ##

nw_board=[' ']*10
game_one=True
while game_one:
    print(" WELCOM TO FUNCKING GAME !!! ")
    display(nw_board)
    pos=user_choice()
    replacemen(nw_board,pos)
    display(nw_board)
    
    game_one=ply_again()
    
    