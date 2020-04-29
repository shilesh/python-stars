class Draw:

    def draw_star(self, my_turtle, size, color, x, y, points):
        my_turtle.hideturtle()
        my_turtle.penup()
        my_turtle.goto(x, y)
        my_turtle.pendown()
        my_turtle.color(color)

        counter = 0
        while counter <= points:
            my_turtle.forward(size)
            my_turtle.right(135)
            counter = counter + 1
