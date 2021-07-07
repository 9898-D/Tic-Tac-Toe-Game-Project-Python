#  ---------------------------------------------------------- TIC-TAC-TOE-GAME-PROJECT --------------------------------------------------


# WRITE FUNCTION Display Game Structure

tstboard=['#','X','O','X','O','X','O','X','O','X']
def display(board):
    
    """
    [display board structuers]

    Args:
        board ([list]): [tic tac toe game strucuture return " BOARD "]
    """
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("- - -")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("- - -")
    print(board[7]+"|"+board[8]+"|"+board[9])

#display(tstboard)



# Write The Function To Choice (X OR O) for player 1 and player 2

def player_choice():
    
    """
    [chose marker as player 1 or player 2]

    Returns:
        [TUPLE]: [we can return 2 value (player 1, player 2) we can done with TUPLE UNPACKING]
    """
    
    marker=''
    while marker not in ['X','O']:
        
        marker=input("\nPlayer 1 choose (X OR O): ")
        
        if marker not in ['X','O']:
            print("\nSORRY INVALID INPUT! Choose (X OR O) ")

    if marker=='X':
        return ('X','O')  # Return a tuple for both player because we can be UNPACKING a tuple
    else:
        return ('O','X')

#player_1,player_2=player_choice()
#print("Player Chooses: " + player_1)
#print("Player Chooses: " + player_2)


# Write function to replacement a userinput index (1 TO 9)

def replacement(board,marker,pos):
    
    """
    [user choose position and that position in board is replaced with as per player's MARKES]

    Args:
        board ([list]): [ LIST OF BOARD strucuture]
        marker ([STRING]): [ player's marker ]
        pos ([INT]): [ Posiion player choosed as per list of board  ]
    """
    board[pos]=marker

#replacement(tstboard,'$',2)
#print(tstboard)
#display(tstboard)


#  WRITE A FUNC TO CHECK A MARKER WIN OR NOT 

def win_chk(board,marker):
    
    """
    [take (Board, marker) and check it possible conditions as per below given ]

    Args:
        board ([LIST]): [DISPLAY BOARD]
        marker (STRING]): [marker is (X,Y)]
    Return:
        [all possible conditions as per situation given that (TRUE) ]
    """
    return(
        (board[1]==marker and board[2]==marker and board[3]==marker)or
        (board[4]==marker and board[5]==marker and board[6]==marker)or
        (board[7]==marker and board[8]==marker and board[9]==marker)or
        (board[1]==marker and board[4]==marker and board[7]==marker)or
        (board[2]==marker and board[5]==marker and board[8]==marker)or
        (board[3]==marker and board[6]==marker and board[9]==marker)or
        (board[1]==marker and board[5]==marker and board[9]==marker)or
        (board[7]==marker and board[5]==marker and board[3]==marker))

#print(win_chk(tstboard,'O'))
#display(tstboard)



#  WRITE A FUNC TO RETURN RANDOM PLAYER GO FIRST

import random
def choose_first():
    
    """
    [Who go first to play a game (player 1, player 2)]

    Returns:
        [STRING]: [use Random INT (0,1) if O (Player 1) or 1 (Player 2)]
    """
    rd=random.randint(0,1)
    if rd==0:
        return "Player 1"
    else:
        return "Player 2"

#print(choose_first())


# TO CHECK IN BOARD EMPTY SPACE IS YES OR NOT IF YES RETURN TRUE ELSE FALSE

def chk_space(board,position):
    
    """
    [check a space in board if space are here return True ]

    Args:
        board ([LIST]): [displayed board ]
        position ([INT]): [player position INT]

    Returns:
        [STRING]: [Empty String in board]
    """
    return board[position]==' '

#print(chk_space(tstboard,2))


#  WRITE A FUNC TO CHECK A BOARD IS FULL OR NOT AND RETURN TRUE IF FULL AND OTHERWISE FALSE

def full_board_chk(board):
    
    """[CHECK FULL BOARD IS FULL OR NOT AND RETURN TRUE IF FULL AND OTHERWIS FALSE]

    Args:
        board ([LIST]): [board display]

    Returns:
        [Boolean]: [if borad is full return true OTHERWIS False]
    """
    
    for i in range(1,10):
        if chk_space(board,i):
            return False       # FOR BOARD IS EMPTY
        
    return True # BOARD IS FULL


# WRITE A FUNC ASK A PLAYER TO NEXT POSITION (AS A Position 1 TO 9) 

def player_position(board):
    
    """
    [take player position as per board structure ]

    Args:
        board ([LIST]): [displayed board structure]

    Returns:
        [INT]: [return a PLAYER POSITION in (INT) ]
    """
    position=0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not chk_space(board,position):
        
        position=int(input("Choose the Position in (1 TO 9): "))        
        
        if not chk_space(board,position):
            print("\nSPACE IS NOT EMPTY! CHOOSE ANOTHER INDEX ")
    
    return position

#print(player_position(tstboard))


# Write Func that ask the player if they want to play again and return boolean True
def replay():
    
    """[players should be play again or not]

    Returns:
        [STRING]: [if player choice (Y,N) and if (Y->TRUE) or (N->False)]
    """
    
    choose=''
    
    while choose not in ['Y','N']:
        choose=input("\nWould You  Like To Play Again (Y OR N): ").upper()
        
        if choose not in ['Y','N']:
            print("\nI DON'T UNDERSTAND! (Y OR N)")
    
    return choose=='Y'


#  -------------------------------------------------------- GAME LOGIC PART --------------------------------------------------------

while True:
    print("\nWELCOME TO TIC TAC TOE GAME ")
    
    nw_board=[' ']*10
    
    player_1,player_2=player_choice()
    
    turn=choose_first()
    print("\n"+turn+" WILL BE GO FIRST ")
    
    play_game=''
    while play_game not in ['Y','N']:
        play_game=input("\nReady to play Game (Y OR N): ")
        
    if play_game=='Y':
        game_on=True
    else:
        game_on=False
    
    while game_on:
        
        if turn=="Player 1":
            
            display(nw_board)
            
            position=player_position(nw_board)
            
            replacement(nw_board,player_1,position)
            
            if win_chk(nw_board,player_1):
                print("\nPLAYER 1 HAS WON ")
                display(nw_board)
                game_on=False
            else:
                if full_board_chk(nw_board):
                    display(nw_board)
                    print("\nGAME TIE ")
                    game_on=False
                else:
                    turn="Player 2"
        else:
            
            display(nw_board)
            
            position=player_position(nw_board)
            
            replacement(nw_board,player_2,position)
            
            if win_chk(nw_board,player_2):
                print("\nPLAYER 2 HAS WON ")
                display(nw_board)
                game_on=False
            else:
                if full_board_chk(nw_board):
                    display(nw_board)
                    print("\nGAME TIE ")
                    game_on=False
                else:
                    turn="Player 1"
                    
    if not replay():
        break
        
      
      