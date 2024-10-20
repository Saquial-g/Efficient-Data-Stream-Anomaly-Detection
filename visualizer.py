import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import dataStream as ds

class flowGraph():
    #Generates the initial graph. Displays provided data, but can be initialized empty
    def __init__(self, data=[300], anomalies=[], xsize = 100, limitXSize = True):
        #Save the provided data in the local variables
        ds.dataArray = data
        self.anomalies = anomalies

        #Define the amount of values visible on the graph, could be setup by the user
        self.xsize = xsize
        self.limitXSize = limitXSize
        
        #Create the initial graph
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])
        self.anomaly_points, = self.ax.plot([], [], 'ro')  # red circles for anomalies
        plt.xlabel("Time")
        plt.ylabel("Value")

        #Check for data provided, start with default values otherwise
        if (len(data) > 0):
            self.ax.set_xlim(0, len(ds.dataArray))
            self.ax.set_ylim(min(ds.dataArray) - 5, max(ds.dataArray) + 5)
        else:
            self.ax.set_xlim(0, 50)
            self.ax.set_ylim(0, 1000)
        
    def update(self, frame):
        ds.genStream(frame)
        if len(ds.dataArray) > self.xsize and self.limitXSize:
            self.line.set_data(range(len(ds.dataArray) - self.xsize, len(ds.dataArray)-1), ds.dataArray[-self.xsize: -1])    
            self.ax.set_xlim(len(ds.dataArray) - self.xsize, len(ds.dataArray))
        else:
            self.line.set_data(range(len(ds.dataArray)), ds.dataArray)
            self.ax.set_xlim(0, len(ds.dataArray))
            
        self.ax.set_ylim(0, max(ds.dataArray) + 100)

        #self.anomaly_points.set_data([i for i, x in enumerate(self.anomalies) if x], [ds.dataArray[i] for i in range(frame) if self.anomalies[i]])
        return self.line, self.anomaly_points
    
    def animate(self):
        ani = FuncAnimation(self.fig, self.update, cache_frame_data=False)
        plt.show()