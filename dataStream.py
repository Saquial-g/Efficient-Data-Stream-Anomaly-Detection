import random
import math

dataArray = []

def genStream(t):
    pattern = 1000 + 100 * math.sin(2 * math.pi * t/100)
    trend = 0
    variation = random.uniform(-200,200)
    point = pattern + variation + trend
    dataArray.append(point)
    return point