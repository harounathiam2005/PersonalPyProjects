on = True
turn_1 = True
play_board = [['* ', '* ', '* ', '* ', '* ', '* '], ['* ', '* ', '* ', '* ', '* ', '* '], ['* ', '* ', '* ', '* ', '* ', '* '], ['* ', '* ', '* ', '* ', '* ', '* '], ['* ', '* ', '* ', '* ', '* ', '* '], ['1 ', '2 ', '3 ', '4 ', '5 ', '6 ']]

symbol_1 = input("Welcome to PyConnect 4! Please enter your player 1 symbol: ")
print("")
symbol_2 = input("Please enter your player 2 symbol: ")
print("")
pieces = [symbol_1 + " ", symbol_2 + " "]
winner = ""

# Display board
def board():
  for i in play_board:
    print("".join(i))

def place_piece():
  print("")
  global turn_1
  if turn_1:
    print("It's player 1's turn!")
    symbol = symbol_1
    turn_1 = False
  else:
    print("It's player 2's turn!")
    symbol = symbol_2
    turn_1 = True
  print("")
  # Check if choice is acceptable
  choices = ["1", "2", "3", "4", "5", "6"]
  answer = input("Where would you like to place your piece? (1, 2, 3, 4, 5 or 6) ")
  while answer not in choices:
      print("")
      answer = input("This is not a valid space. Please enter (1, 2, 3, 4, 5, or 6) ")
    # If column is full, disallow choice
  occupied = False
  location = choices.index(answer)
  location = int(location)
  if play_board[0][location] != "* ":
    occupied = True
  while occupied:
    print("")
    answer = input("You can't place there! Choose again: ")
    location = choices.index(answer)
    location = int(location)
    if play_board[0][location] == "* ":
      occupied = False
      
  for i in range(len(play_board) - 1):
    if play_board[i + 1][location] != "* ":
      if play_board[0][location] != "* ":
        print("You can't place here!")
        continue
      play_board[i][location] = symbol + " "
      break

def check_win():
  current_piece = ""
  for i in range(len(play_board) - 1):
    counter = 0
    global winner
    if winner != "":
      break
    for x in range(0, 5):
      #print(x)
      current_piece = play_board[i][x]
      #print("-- ", current_piece)
      print((current_piece, play_board[i][x - 1]))
      if current_piece == play_board[i][x - 1] or current_piece == play_board[i - 1][x] or current_piece == play_board[i - 1][x - 1]:
        if current_piece == "* ":
          continue
        counter += 1
      if counter >= 4:
        winner = current_piece
        global on
        on = False
        break

while on:
  print("")
  board()
  place_piece()
  check_win()
print("")
board()
print("")
print(f"Congratulations to player {pieces.index(winner) + 1}! You win!")
