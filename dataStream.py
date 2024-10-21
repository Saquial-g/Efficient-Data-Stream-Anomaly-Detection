import random
import numpy as np

# Stores the data flow
dataArray = []

def genStream(t):
    # Generate the next data point
    pattern = dataArray[-1] + 5 * np.sin(2 * np.pi * t/50)
    trend = 0.05
    noise = random.uniform(-18,18)
    point = pattern + noise + trend

    # Add the data point to the data stream while avoiding negative values
    if dataArray[-1] + point < 0:
        dataArray.append(abs(point))
    else:
        dataArray.append(point)

    # Handle memory leak
    if len(dataArray) > 100000:
        del dataArray[0]

    return point

# Detector of anomalies by using a mix of ZScore and exponential moving average (EMA)
#   - Alpha defines how much the current point affects the EMA 
#   - Threshold defines the acceptable range for the ZScore
#   - Window defines the amount of points used to calculate the standard deviation
class anomaly_detector():
    def __init__(self, dataStream, alpha=0.2, threshold=1, window = 200):
        # Initialize the variables used by the detector. Make a first calculation
        self.EMA = [dataStream[-1], dataStream[-1]]
        self.alpha = alpha
        self.threshold = threshold
        self.window = window
        self.std = 0

        self.anomalies = []
        self.anomTime = []

        self.calculate_EMA(dataStream)  

    # Calculate point by using exponential moving average (EMA) and standard deviation
    # for the current data point to account for fluctuations in the data stream
    def calculate_EMA(self, dataStream):
        # Calculate the exponential moving average by using the current data point and the previous EMA
        self.EMA = [
            self.EMA[1], 
            dataStream[-1] * self.alpha + self.EMA[0] * (1-self.alpha)
        ]

        # Calculate the standard deviation of the data stream within the window
        if len(dataStream) < self.window:
            self.std = np.std(dataStream)
        else:
            self.std = np.std(dataStream[-self.window:-1])

    # Calculate a ZScore for the current data point and check if it is within the tolerable threshold
    def detect_anomaly(self, dataStream, t):
        # Calculate the ZScore
        self.calculate_EMA(dataStream)
        ZScore = abs(dataStream[-1] - self.EMA[1]) / self.std
        
        # If the ZScore is not within the defined threshold mark it as an anomaly
        # The first 50 data are ignored to allow the formation of a pattern
        if ZScore > self.threshold and len(dataStream) > 50:
            self.anomalies.append(dataStream[-1])
            self.anomTime.append(t-1)



    

