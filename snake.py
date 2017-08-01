import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500

turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE=22
START_LENGTH=8

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]


snake=turtle.clone()
snake.shape("square")

turtle.hideturtle()


for snake_draw in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)

    stamp_id=snake.stamp()
    stamp_list.append(stamp_id)


UP_ARROW="Up"
DOWN_ARROW="Down"
LEFT_ARROW="Left"
RIGHT_ARROW="Right"
TIM_STEP=100
SPACEBAR="space"

UP=0
LEFT=1
DOWN=2
RIGHT=3

direction=UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction
    direction= UP
    move_snake()
    print("you pressed the up key!")

def down():
    global direction
    direction= DOWN
    move_snake()
    print("you pressed the down key!")

def left():
    global direction
    direction= LEFT
    move_snake()
    print("you pressed the left key!")

def right():
    global direction
    direction= RIGHT
    move_snake()
    print("you pressed the right key!")


turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print('you moved right')
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moved left')

    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved up')
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down')

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last
    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print('You hit the right edge! Game over!')
        quit()

    
