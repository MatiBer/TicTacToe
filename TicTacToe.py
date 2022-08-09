from random import randrange

board = [[str((i+1)+j*3) for i in range(3)] for j in range(3)]

def display_board(board):
    # Funkcja, ktora przyjmuje jeden parametr zawierajacy biezacy stan tablicy
    # i wyswietla go w oknie konsoli.
    
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[0][0]+"   |   "+board[0][1]+"   |   "+board[0][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[1][0]+"   |   "+board[1][1]+"   |   "+board[1][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[2][0]+"   |   "+board[2][1]+"   |   "+board[2][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    
    


def enter_move(board):
    # Funkcja, ktora przyjmuje parametr odzwierciedlajacy biezacy stan tablicy,
    # prosi uzytkownika o wykonanie ruchu, 
    # sprawdza dane wejsciowe i aktualizuje tablice zgodnie z decyzja uzytkownika.
    key = input("Wykonaj swój ruch: ")
    
    if key.isdigit():
        move = int(key)
    else:
        move = 0
    
    if move > 0 and move < 10:
        if move < 4 and board[0][move-1] != "O" and board[0][move-1] != "X":
            board[0][move-1] = "O"
            display_board(board)
            victory_for(board, "O")
        elif 4 <= move < 7 and board[1][move-4] != "O" and board[1][move-4] != "X": 
            board[1][move-4] = "O"
            display_board(board)
            victory_for(board, "O")
        elif move >= 7 and board[2][move-7] != "O" and board[2][move-7] != "X":
            board[2][move-7] = "O"
            display_board(board)
            victory_for(board, "O")
        else:
            print("To pole jest już zajęte! Wykonaj ruch jeszcze raz!")
            enter_move(board)
    else:
        print("Nieprawidłowy ruch! Wykonaj jeszcze raz!")
        enter_move(board)
    


def make_list_of_free_fields(board):
    # Funkcja, ktora przeglada tablice i tworzy liste wszystkich wolnych pol; 
    # lista sklada sie z krotek, a kazda krotka zawiera pare liczb odzwierciedlajacych rzad i kolumne.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "O" and board[i][j] != "X":
                free_fields.append((i-1,j-1))
    
    if free_fields == []:
        return True
    else:
        return False



def victory_for(board, sign):
    # Funkcja, ktora dokonuje analizy stanu tablicy w celu sprawdzenia
    # czy uzytkownik/gracz stosujacy "O" lub "X" wygral rozgrywke.
    winO_cond = ["O","O","O"]
    winX_cond = ["X","X","X"]
    win_seq = [ [board[0][0],board[0][1],board[0][2]], [board[1][0],board[1][1],board[1][2]], [board[2][0],board[2][1],board[2][2]],
                [board[0][0],board[1][0],board[2][0]], [board[0][1],board[1][1],board[2][1]], [board[0][2],board[1][2],board[2][2]],
                [board[0][0],board[1][1],board[2][2]], [board[0][2],board[1][1],board[2][0]] ]
    end = False
    for seq in win_seq:
        if seq == winO_cond:
            print("Gratulacje! Wygrałeś!!!")
            end = True
        elif seq == winX_cond:
            print("Komputer wygrał! Następnym razem ci się uda")
            end = True
    
    is_draw = make_list_of_free_fields(board)
    
    if is_draw == False and end == False:
        if sign == "O": draw_move(board)
        elif sign == "X": enter_move(board)
    elif is_draw == True and end == False:
        print("Remis! Nie ma więcej wolnych pól!")


def draw_move(board):
    # Funkcja, ktora wykonuje ruch za komputer i aktualizuje tablice.
    moveX = randrange(9)+1
    
    if moveX < 4 and board[0][moveX-1] != "O" and board[0][moveX-1] != "X":
        board[0][moveX-1] = "X"
        display_board(board)
        victory_for(board, "X")
    elif 4 <= moveX < 7 and board[1][moveX-4] != "O" and board[1][moveX-4] != "X": 
        board[1][moveX-4] = "X"
        display_board(board)
        victory_for(board, "X")
    elif moveX >= 7 and board[2][moveX-7] != "O" and board[2][moveX-7] != "X":
        board[2][moveX-7] = "X"
        display_board(board)
        victory_for(board, "X")
    else:
        draw_move(board)
    




board[1][1] = "X"
display_board(board)
enter_move(board)