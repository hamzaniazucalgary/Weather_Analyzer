import numpy as np
import matplotlib.pyplot as pyplot
class Chart:
    def __init__(self,x,y,title,xlabel,ylabel):
        self.x = x
        self.y = y
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
    def drawLineChart(self):
        fig = pyplot.figure()
        pyplot.title("Temperature in Calgary between Jan-Dec in 2000")
        pyplot.ylabel("Min Temperature (F)")
        pyplot.xlabel("Month of Year")
        pyplot.plot(self.x,self.y,marker="o")
        pyplot.show()
    def drawBarChart(self):
        fig = pyplot.figure()
        pyplot.title("Temperature in Calgary between Jan-Dec in 2000")
        pyplot.ylabel("Min Temperature (F)")
        pyplot.xlabel("Month of Year")
        pyplot.bar(self.x,self.y)
        pyplot.show()