import constant
import random


class ColorBucket:
    description = 'Color Bucket provides one color from the bucket'

    def __init__(self):
        print('__ init __ ')
        self.colors = constant.COLORS

    def get_color(self):
        color = random.choice(self.colors)
        return color
