board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
used=[]
player1=input('Enter the player-1 name.')
player2=input('Enter the player-2 name.')
print('Here we start!\n')
turn=1
while(not check_x(board) and not check_o(board)):
    display_board(board)
    if(turn%2==0):
        o=int(input('Player-2 turn'))
        if(o in used):
            print(f'The place {o} is taken .\n please input another number')
            while(o in used):
                o=int(input('player-2 turn'))
        
        board[o]='O'
        used.append(o)
    else:
        x=int(input('player-1 turn'))
        if( x in used):
            print(f'The place {x} is taken .\n please input another number')
            while(x in used):
                x=int(input('player-1 turn'))
    
        board[x]='X'
        used.append(x)
    turn=turn+1
        
else:
    display_board(board)
    check_win(board)