players = ["Player 1", "Player 2"]

options = ["X", "Y"]

matrix = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def print_board():
    for row in matrix:
        print(" | ".join(row))
        print("---------")

def check_winner():
    ## check for a winner in the rows and columns
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            return matrix[i][0]
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
            return matrix[0][i]
    # check for a winner in the diagonals
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return matrix[0][2]
    return None
        
        
def play():
    move = 0
    count = 0
    winner = None
    for count in range(9):
        player = players[count % 2]
        option = options[count % 2]
        move = int(input(f"{player} ({option}), please make your move:"))
        
        while move not in range(1, 10) or matrix[(move - 1) // 3][(move - 1) % 3] in options:
            print("Invalid move. Please enter a number between 1-9 that is not already taken")
            move = int(input(f"{player} ({option}), please make your move:"))
        
        print(f"{player} made a move")
        move -= 1
        matrix[move // 3][move % 3] = options[count % 2]
        
        count += 1
        ## lets print the board after player one makes a move
        print_board()
        
        winner = check_winner()
        
        if winner:
            if winner == options[0]:
                player = players[0]
            else:
                player = players[1]
            print(f"Congratulations {player}! You have won!")
            break
    if winner == None:
        print("It's a draw!")
   
def main():
    print("Welcome to a friendly game of Tic Tac Toe!")
    players[0] = input("Player one: Please enter your name: ")
    players[1] = input("Player two: Please enter your name: ")
    
    print(f"The game will be played between {players[0]} and {players[1]}")
    print(f"{players[0]}, you will be X and {players[1]}, you will be Y")
    print(f"{players[0]} will go first")
    print("The board is as follows:")
    print_board()
    print("--------------------------------")
    print("When it is your turn, you will make your move by entering a number between 1-9")
    print("Let's get started!")
    print("--------------------------------\n")
    play()
    
        
if __name__ == "__main__":
    main()

