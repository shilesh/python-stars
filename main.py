#!/usr/local/bin/python3

import random
import turtle as my_turtle

import color_bucket
import draw

color_bucket_obj = color_bucket.ColorBucket()
draw_obj = draw.Draw()

print(color_bucket_obj.colors)
print(color_bucket.ColorBucket.description)

my_turtle.Screen().bgcolor('black')

while True:
    size = random.choice(range(5, 50))
    x = random.choice(range(-200, 200))
    y = random.choice(range(-200, 200))

    draw_obj.draw_star(my_turtle, size,
                       color_bucket_obj.get_color(), x, y, 8)
