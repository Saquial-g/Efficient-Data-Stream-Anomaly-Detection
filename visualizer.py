import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import dataStream as ds

class flowGraph():
    # Initializes the graph variables.
    #   - data and anomalies define the starting data and anomalies
    #   - xsize defines how many data points are allowed in the graph
    #   - limitXSize defines if the graph should be limited to the amount of data points specified by xsize
    def __init__(self, data=[300], anomalies=[], xsize = 500, limitXSize = True):
        # Save the provided data in the local variables
        ds.dataArray = data
        self.anomalies = anomalies

        # Define the amount of values visible on the graph, could be setup by the user
        self.xsize = xsize
        self.limitXSize = limitXSize

        # Initialize anomaly detector
        self.detector = ds.anomaly_detector(data)
        
        # Create the initial graph
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])
        self.anomaly_points, = self.ax.plot([], [], 'ro', marker='.')  # red circles for anomalies
        plt.xlabel("Time")
        plt.ylabel("Value")

        # Check for data provided, start with default values otherwise
        if (len(data) > 0):
            self.ax.set_xlim(0, len(ds.dataArray))
            self.ax.set_ylim(min(ds.dataArray) - 5, max(ds.dataArray) + 5)
        else:
            self.ax.set_xlim(0, 50)
            self.ax.set_ylim(0, 1000)
        
    def update(self, frame):
        # Generate the next data point
        ds.genStream(frame)

        # Check if the graph can display all the data or limit itself to a specific range
        if len(ds.dataArray) > self.xsize and self.limitXSize:
            # Display the data within the range defined by xsize
            self.line.set_data(range(len(ds.dataArray) - self.xsize, len(ds.dataArray)-1), ds.dataArray[-self.xsize: -1])    
            self.ax.set_xlim(len(ds.dataArray) - self.xsize, len(ds.dataArray))
        else:
            # Display all data
            self.line.set_data(range(len(ds.dataArray)), ds.dataArray)
            self.ax.set_xlim(0, len(ds.dataArray))
        
        # Limits of the y axis are independent of the amount of data
        self.ax.set_ylim(0, max(ds.dataArray) + 100)

        # Scan the current data point to check if it's an anomaly
        self.detector.detect_anomaly(ds.dataArray, len(ds.dataArray))

        # Draw the anomalies in the graph
        self.anomaly_points.set_data(self.detector.anomTime, self.detector.anomalies)
    
    def animate(self):
        # Create an animation by running the update function in a loop. Shows the graph
        ani = FuncAnimation(self.fig, self.update, cache_frame_data=False)
        plt.show()