import turtle
turtle.Screen()
board = turtle.Turtle()
 
# first triangle for star
board.forward(100) # draw base
 
board.left(120)
board.forward(100)
 
board.left(120)
board.forward(100)
 
board.penup()
board.right(150)
board.forward(50)

# second triangle for star
board.penup()

board.right(150)
board.forward(50)

board.pendown()

board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done