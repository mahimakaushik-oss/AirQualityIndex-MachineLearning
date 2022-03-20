# -*- coding: utf-8 -*-

"""
Created on Fri Mar 11 07:07:35 2022

@author: Mahima Kaushik
"""
import pandas as pd
import matplotlib.pyplot as plt


def overall_PM_avg():
    average_pm = {}
    for year in range(2013, 2019):
        data_file = "data/AQI/aqi{}.csv".format(year)
        average_pm[year] = PM_avg_per_day_for(data_file)
    return average_pm


def plot_PM(average_pm: dict):
    for year in list(average_pm.keys())[:3]:
        block = average_pm[year]
        plt.plot(range(0, len(block)), block, label = "{} data".format(year))
        

def PM_avg_per_day_for(d_file: str):
    temp_i = 0
    average = []
    for rows in pd.read_csv(d_file, chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        
        for index, row in df.iterrows():
            data.append(row['PM2.5'])

        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
    
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var = add_var + temp
                    
        avg = add_var / 24
        temp_i = temp_i + 1
        average.append(avg)
        
    return average
        
        
if __name__ == "__main__":
    #print(avg_data_2013()
    lst13 = PM_avg_per_day_for('data/AQI/aqi2013.csv')
    overall = overall_PM_avg()
    plot_PM(overall)
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc = 'upper right')
    plt.show()