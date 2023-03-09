import turtle as t
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M")


def draw_zero(x, y, size=1):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(90)

    t.forward(20 * size)
    t.circle(40 * size, 180)
    t.forward(100 * size)
    t.circle(40 * size, 180)
    t.forward(100 * size)


def draw_one(x, y, size=1):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(90)  # север/вверх
    t.forward(100 * size)
    t.left(135)
    t.forward(30 * size)
    t.right(90)
    t.forward(15 * size)
    t.right(90)
    t.forward(45 * size)
    t.right(45)
    t.forward(20 * size)
    t.right(90)
    t.forward(120 * size)
    t.right(90)
    t.forward(20 * size)


def draw_two(x, y, size=1):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(90)

    t.left(90)
    t.forward(50 * size)
    t.right(90)
    t.forward(50 * size)
    t.right(90)
    t.forward(50 * size)
    t.left(90)
    t.forward(50 * size)
    t.left(90)
    t.forward(50 * size)


def draw_three(x, y, size=1):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(90)
    t.right(90)
    t.forward(50 * size)
    t.left(90)
    t.forward(50 * size)
    t.left(90)
    t.forward(50 * size)
    t.right(150)
    t.forward(60 * size)
    t.left(150)
    t.forward(50 * size)


def draw_four(x, y, size=1):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(90)

    t.forward(100 * size)
    t.backward(40)
    t.left(90)
    t.forward(50 * size)
    t.right(110)
    t.forward(45 * size)


def draw_five(x, y, size=1):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(90)

    t.right(90)
    t.circle(50 * size, 180)
    t.right(90)
    t.forward(50 * size)
    t.right(90)
    t.forward(50 * size)


def draw_six(x, y, size=1):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(90)

    t.circle(50 * size)
    t.up()
    t.left(90)
    t.forward(100 * size)

    t.down()
    t.right(90)
    t.forward(10 * size)
    t.circle(-80 * size, 100)


def draw_seven(x, y, size=1):
    t.up()
    t.goto(x, y + 200)
    t.down()
    t.setheading(90)

    t.right(90)
    t.forward(100 * size)

    t.right(90)
    t.forward(20 * size)

    t.right(30)
    t.forward(145 * size)


def draw_eight(x, y, size=1):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(90)
    t.circle(50)
    t.up()
    t.left(90)
    t.forward(50 * size)
    t.left(90)
    t.forward(50 * size)
    t.left(90)
    t.down()
    t.circle(-50)


def draw_nine(x, y, size=1):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(0)
    t.forward(50 * size)
    t.left(90)
    t.forward(100 * size)
    t.left(90)
    t.forward(50 * size)
    t.left(90)
    t.forward(50 * size)
    t.left(90)
    t.forward(50 * size)


def draw_hour(first, second):
    if first == '0':
        draw_zero(-100, 0)

    if first == '1':
        draw_one(-100, 0)

    if first == '2':
        draw_two(-100, 0)

    if second == '0':
        draw_zero(-50, 50)

    if second == '1':
        draw_one(-50, 0)

    if second == '2':
        draw_two(-50, 0)

    if second == '3':
        draw_three(-50, 0)

    if second == '4':
        draw_four(-50, 0)

    if second == '5':
        draw_five(-50, 0)

    if second == '6':
        draw_six(-50, 0)

    if second == '7':
        draw_seven(-50, 0)

    if second == '8':
        draw_eight(-50, 0)

    if second == '9':
        draw_nine(-50, 0)


def draw_minute(first, second):
    if first == '0':
        draw_zero(50, 50)

    if first == '1':
        draw_one(50, 50)

    if first == '2':
        draw_two(50, 50)

    if first == '3':
        draw_three(50, 0)

    if first == '4':
        draw_four(50, 50)

    if first == '5':
        draw_five(50, 50)

    if first == '6':
        draw_six(50, 50)

    if first == '7':
        draw_seven(50, 50)

    if first == '8':
        draw_eight(50, 50)

    if first == '9':
        draw_nine(50, 50)

    if second == '0':
        draw_zero(100, 0)

    if second == '1':
        draw_one(100, 0)

    if second == '2':
        draw_two(200, 0)

    if second == '3':
        draw_three(200, 0)

    if second == '4':
        draw_four(200, 0)

    if second == '5':
        draw_five(200, 0)

    if second == '6':
        draw_six(200, 0)

    if second == '7':
        draw_seven(200, 0)

    if second == '8':
        draw_eight(200, 0)

    if second == '9':
        draw_nine(200, 0)


hour = current_time[0]
hour_two = current_time[1]

draw_hour(hour, hour_two)

first_minute = current_time[3]
second_minute = current_time[4]

draw_minute(first_minute, second_minute)

t.exitonclick()
