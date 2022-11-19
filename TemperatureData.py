import numpy as np
import matplotlib.pyplot as pyplot
class TemperatureData:
    def __init__(self,date_obj,minTemp,maxTemp,snowFall):
        self.date_obj = date_obj
        self.minTemp = minTemp
        self.maxTemp = maxTemp
        self.snowFall = snowFall