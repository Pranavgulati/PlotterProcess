
import multiprocessing
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class plotter(multiprocessing.Process):
    def __init__(self,dataQ,processName):
        multiprocessing.Process.__init__(self)
        self.dataQ = dataQ
        self.processName=processName

    def run(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=300)
        plt.show()

    def animate(self,i):
        if not self.dataQ.empty():
            dataIn=self.dataQ.get()
            t=range(0,len(dataIn))
            self.ax.clear()
            self.ax.plot(t, dataIn, linewidth=1.0, linestyle="-", color="red", label="PPG")
            self.ax.legend(loc='upper left')
            self.ax.grid(True)
            self.ax.relim()
            self.ax.autoscale_view(True,True,True)
            self.fig.canvas.draw()
        else:
            return

if __name__ == '__main__':

    sendData=[1,2,3,4,5,6,7,6,5,4,3,2,1]
    manager = multiprocessing.Manager()
    plotDataQ=manager.Queue()
    plotProcess=plotter(plotDataQ,"plotProcess")
    STOP=1
    plotProcess.daemon=False
    plotProcess.start()

    while (STOP):
        try:
            sendData[5]+=1
            if plotDataQ.empty():
                '''sending the data to the plotProcess'''
                plotDataQ.put(sendData);
            time.sleep(1)
        except KeyboardInterrupt:
            '''add pause code here'''
            print(len(sendData));
            STOP = 0


        
