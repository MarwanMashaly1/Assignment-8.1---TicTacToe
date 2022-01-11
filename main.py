from turtle import *

screen = Screen()
pendown()
turn = "x"

def setup_game():
    penup()
    speed(8)
    goto(-200 ,200) 
    pendown()
    for intSquares in range(3):         # range for 3 squares
        for intSides in range(4):       # range for 4 sides
            forward(100)                 # forward 100 units
            right(90)                  # right 90 degrees
        forward(100)                 # forward"
    rt(90)                       # right 90 degrees
    fd(100)                      # forward 100 units
    rt(90)                       # right 90 degrees
    intPlace = 0                     # set value to zero 
    for intSquares in range(3):         # range for 3 squares
        for intSides in range(4):       # range for 4 sides
            fd(100)                 # forward 100 units
            lt(90)                  # right 90 degrees
        fd(100)                 # forward 100 units
    lt(90)                       # right 90 degrees
    fd(100)                      # forward 100 units
    lt(90)                       # right 90 degrees
    intPlace = 0                    # set to zero
    for intSquares in range(3):         # range for 3 squares
        for intSides in range(4):       # range for 4 sides
            fd(100)                 # forward 100 units
            rt(90)                  # right 90 degrees
        fd(100)                 # forward 100 units

def draw_x (location):
    style = ("Arial", 40)
    if location == 0:
        penup()
        goto(-175,150)
        write("X", font=style)
    elif location == 1:
        penup()
        goto(-75,150)
        write("X", font=style)
    elif location == 2:
        penup()
        goto( 25,150)
        write("X", font=style)
    elif location == 3:
        penup()
        goto(-175, 50 )
        write("X", font=style)
    elif location == 4:
        penup()
        goto(-75,50)
        write("X", font=style)
    elif location == 5:
        penup()
        goto(25,50)
        write("X", font=style)
    elif location == 6:
        penup()
        goto(-175,-50)
        write("X", font=style)
    elif location == 7:
        penup()
        goto(-75,-50)
        write("X", font=style)
    elif location == 8:
        penup()
        goto(25,-50)
        write("X", font=style)

# def draw_o(location): 
def draw_o (location):
    if location == 0:
        speed(2.5)
        penup()
        goto(-150, 175)
        pendown()
        circle(-25)
    elif location == 1:
        penup()
        goto(-50, 175)
        pendown()
        circle(-25)
    elif location == 2:
        penup()
        goto( 50, 175)
        pendown()
        circle(-25)
    elif location == 3:
        penup()
        goto(-150, 75)
        pendown()
        circle(-25)
    elif location == 4:
        penup()
        goto(-50, 75)
        pendown()
        circle(-25)
    elif location == 5:
        penup()
        goto(50, 75)
        pendown()
        circle(-25)
    elif location == 6:
        penup()
        goto(-150 ,-25)
        pendown()
        circle(-25)
    elif location == 7:
        penup()
        goto(-50, -25)
        pendown()
        circle(-25)
    elif location == 8:
        penup()
        goto(50, -25)
        pendown()
        circle(-25)

def win_check():
    # horizontal check
    for i in range(0, 9, 3):
        if (board[i] == board[i + 1] == board[i + 2]): 
            return True

    # vertical check
    for i in range(3):
        if (board[i] == board[i + 3] == board[i + 6]):
            return True

    # diagonal check
    if ((board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6])):
        return True

def play_move (move):

  global board, turn, game

  if board[move] >= 1 and board[move] <= 9:
    board[move] = turn
    print ("heres board", board)

    if turn == "o":
      draw_o(move)
      if (win_check()):
        print( "O win!" )
        game = "over"
      turn = "x"
    elif turn == "x":
      draw_x(move)
      if (win_check()):
        print( "X win!" )
        game = "over"
      turn = "o"

  

def which_square (x,y):

  """This function will convert the xy coordinate into squares of the tic tac toe board 
  [ 0 | 1 | 2 ]
  [ 3 | 4 | 5 ]
  [ 6 | 7 | 8 ]
  """

  # # for testing   
  print ("x and y: ", x, y)

  global game

  if game == "over":
    return None

  # check which square does the xy coordinate belongs to
  # if not((x < -200) or (x > 100)) or ((y > 200) or (y <-100)):
  if y <= 200 and y >= 100:
    if x >= 0:
      move = 2 
    elif x >= -100:
      move = 1 
    elif x >= -200:
      move = 0 
  
  elif y < 100 and y >=0:
    if x >= 0:
      move = 5 
    elif x >= -100:
      move = 4
    elif x >= -200:
      move = 3

  elif y <0 and y >= -100:
    if x >= 0:
      move = 8
    elif x >= -100:
      move = 7
    elif x >= -200:
      move = 6 
  
  # draws 
  play_move(move)
    

# Main Code   
setup_game()
game = "not over"
move = None
board = [0,1,2,3,4,5,6,7,8]

#Everytime this function is called, it passes xy coordinate into a function inside the parathensis.
screen.onscreenclick(which_square)
print("Heres the current board",board)
screen.mainloop()
