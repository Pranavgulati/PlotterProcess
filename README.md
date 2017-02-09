# PlotterProcess
This script demonstrates using the matplotlib animated plots in a separate process so that the main process doesnt get blocked by matplotlib.
this was a problem that i encountered with matplotliba and this serves as a solution

# Instructions
- you can use the code to understand how it is working, the part after ( if __name__ == '__main__': ) is the area of the main process.
- it is advised to define the class in the main script because you would like to tweak the 'animate' function of the class to your liking
- be advised, the animate function of the class plotter is called at a set interval periodically and you may want to tweak it depending on the data you are sending to the process
