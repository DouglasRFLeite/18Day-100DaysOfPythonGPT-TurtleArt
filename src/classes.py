from turtle import Turtle, Screen
import colorgram
import numpy as np 
import random

colors = colorgram.extract("image.jpg", 6)
colors_rgb = [tuple(color.rgb) for color in colors]
print(colors_rgb)