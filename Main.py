import numpy as np
import matplotlib.pyplot as pyplot
from Chart import *
from FileIO import *
from Date import *
from TemperatureData import *
from WeatherAnalyzer import *
def menu():
    print("1- Get Minimum Temperautre of 1990-2019")
    print("2- Get Maximum Temperautre of 1990-2019")
    print("3- Get Minimum Temperature of 1990-2019 Annually")
    print("4- Get Maximum Temperautre of 1990-2019 Annually")
    print("5- Get Average Snowfall between 1990-2019 Annually")
    print("6- Get Average Temperature between 1990-2019 Annually")
def main():
    weather_data = FileIO("F:\Fall 2020\ENGG 233\Term Project\CalgaryWeather.csv")
    weather_data_obj = weather_data.dataTable()
    weather_analyzer = WeatherAnalyzer()
    menu()
    n = int(input("Enter A Number To Get The Corresponding Data: "))
    if (n > 0 and n <= 5 and n == 1):
        Min_temp = WeatherAnalyzer().getMinTemp(weather_data_obj[:,3])
        print("According to provided Calgary weather data the minimum temperature between years 1990 and 2019 was " + str(Min_temp) +  " (F) temperature")
    elif (n > 0 and n <= 5 and n == 2):
        Max_temp = WeatherAnalyzer().getMaxTemp(weather_data_obj[:,2])
        print("According to provided Calgary weather data the maximum temperature between years 1990 and 2019 was " + str(Max_temp) +  " (F) temperature")
    elif (n > 0 and n <= 5 and n == 3):
        Min_temp_annually = WeatherAnalyzer().getMinTempAnnually()
        print("Annual minimum temperature between years 1990 and 2019:'\n'" + str(Min_temp_annually))
    elif (n > 0 and n <= 5 and n == 4):
        Max_temp_annually = WeatherAnalyzer().getMaxTempAnnually()
        print("Annual maximum temperature between years 1990 and 2019:'\n'" + str(Max_temp_annually))
    elif (n > 0 and n <= 5 and n == 5):
        A_S = WeatherAnalyzer().getAvgSnowFallAnnually()
        print("Annual average snow fall between years 1990 and 2019:'\n'" + str(np.round(A_S,2)))
    elif (n > 0 and n == 6):
        Max_temp_annually = WeatherAnalyzer().getMaxTempAnnually()
        Min_temp_annually = WeatherAnalyzer().getMinTempAnnually()
        Avg_Temp_Annually = WeatherAnalyzer().getAvgTempAnnually(Max_temp_annually,Min_temp_annually)
        print("Annual Average Temperature between years 1990 and 2019:'\n'" + str(Avg_Temp_Annually))

if __name__ == "__main__":
    main()