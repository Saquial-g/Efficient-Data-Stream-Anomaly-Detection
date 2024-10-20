import random
import math

#complete data flow, can be used by the program to analize historical patterns
dataArray = []

def genStream(t):
    #generate the next data point
    pattern = dataArray[-1] + 5 * math.sin(2 * math.pi * t/50)
    trend = 1
    noise = random.uniform(-18,18)
    point = pattern + noise + trend

    #Add the data point to the data stream while avoiding negative values
    if dataArray[-1] + point < 0:
        dataArray.append(abs(point))
    else:
        dataArray.append(point)

    #handle memory leak
    if len(dataArray) > 100000:
        del dataArray[0]

    return point