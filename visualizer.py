import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import dataStream as ds

class flowGraph():
    def __init__(self, data=[], anomalies=[]):
        self.data = data
        self.anomalies = anomalies

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])
        self.anomaly_points, = self.ax.plot([], [], 'ro')  # red circles for anomalies

        if (len(data) > 0):
            self.ax.set_xlim(0, len(self.data))
            self.ax.set_ylim(min(self.data) - 5, max(self.data) + 5)
        
    
    def update(self, frame):
        self.data.append(ds.genStream(frame))
        self.line.set_data(range(len(self.data)), self.data)

        self.ax.set_xlim(0, len(self.data))
        self.ax.set_ylim(min(self.data) - 5, max(self.data) + 5)

        #self.anomaly_points.set_data([i for i, x in enumerate(self.anomalies) if x], [self.data[i] for i in range(frame) if self.anomalies[i]])
        return self.line, self.anomaly_points
    
    def animate(self):
        ani = FuncAnimation(self.fig, self.update, blit=True)
        plt.show()