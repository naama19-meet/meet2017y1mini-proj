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
    pos_list.append(stamp_id)


UP_ARROW="Up"
LEFT_ARROW="Left"
RIGHT_ARROW="Right"
TIM_STEP="100"

SPACEBAR="space"

UP=0

    
