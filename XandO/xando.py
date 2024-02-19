board = [0, 1, 2,  # i = 0
         3, 4, 5,  # i = 1
         6, 7, 8]  # i = 2

def draw_board():
    print("-------------")
    for i in range(3):
        print('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
    print("-------------")

def input_XO(token):
    while True:
        value = input("Куда поставить " + token + '?' + f"\n")
        value = int(value)
        if not(value in board):
            print("Введено неверное число")
            continue
        if str(board[value]) in "XO":
            print("Эта ячейка уже занята")
            continue
        board[value] = token
        break

def check_win():
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    if board[0] == board[3] == board[6]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    if board[0] == board[4] == board[8]:
        return True
    if board[6] == board[4] == board[2]:
        return True
    return False

def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            input_XO('X')
        else:
            input_XO('O')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                if counter%2 == 0:
                    print("X","WIN")
                    break
                else:
                    print("O","WIN")
                    break
        counter += 1
        if counter > 8:
            draw_board()
            print("Ничья!")
            break

main()