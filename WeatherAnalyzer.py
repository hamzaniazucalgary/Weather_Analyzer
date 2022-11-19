import numpy as np
import matplotlib.pyplot as pyplot
from FileIO import *
class WeatherAnalyzer:
    def __init__(self):
        # self.ListTempData = TemperatureData
        self.get_weatherData = FileIO("F:\Fall 2020\ENGG 233\Term Project\CalgaryWeather.csv").dataTable()
    def getMinTemp(self,data):
        return np.min(data)
    def getMaxTemp(self,data):
        return np.max(data)
    def getMinTempAnnually(self):
        c = 0
        e = 11
        y = 0
        results = np.empty((30,2))
        i = 0
        while c < 359 and e <= 359:
            year = self.get_weatherData[y,0]
            x = self.get_weatherData[range(c,e),3]
            mini = np.min(x)
            c += 12
            e += 12
            y += 12
            results[i][0] = year
            results[i][1] = mini
            i += 1
        return(results)
    def getMaxTempAnnually(self):
        c = 0
        e = 11
        y = 0
        results = np.empty((30,2))
        i = 0
        while c < 359 and e <= 359:
            year = self.get_weatherData[y,0]
            x = self.get_weatherData[range(c,e),2]
            mixi = np.max(x)
            c += 12
            e += 12
            y += 12
            results[i][0] = year
            results[i][1] = mixi
            i += 1
        return(results)
    def getAvgSnowFallAnnually(self):
        c = 0
        e = 12
        y = 0
        results = np.empty((30,2))
        i = 0
        while c <= 348 and e <= 359 and y < 350:
            x = self.get_weatherData[range(c,e),4]
            avg = np.average(x)
            c += 12
            e += 12
            year = self.get_weatherData[y,0]
            results[i][0] = year
            results[i][1] = avg
            y += 12
            i += 1
            if c == 348:
                x = self.get_weatherData[range(348,359),4]
                avg = np.average(x)
                year = self.get_weatherData[348,0]
                results[29][0] = year
                results[29][1] = avg
        return(results)
    def getAvgTempAnnually(self,annual_min_temp,annual_max_temp):
        return ((annual_max_temp + annual_min_temp)/2)



    