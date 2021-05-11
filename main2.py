# -*- coding: utf-8 -*-
"""
Created on Mon May 10 21:21:18 2021

@author: Praful
"""

import requests
import time
import csv
import pandas as pd
import plotly.express as px 

def get_iss_data():
    
    api = 'https://api.wheretheiss.at/v1/satellites/25544'
    request = requests.get(api).json()
    latitude = request['latitude']
    longitude = request['longitude']
    
    return latitude, longitude
    
def into_csv():
    latitude, longitude = get_iss_data()
    data_list = []
    #header = ['latitude','longitude']
    data_list.append(latitude)
    data_list.append(longitude)
    print(data_list)
    
    with open('map_data2.csv','a', newline='') as file:
        writer = csv.writer(file, delimiter =',')
        #writer.writerow(header)

        writer.writerow(data_list)
        
def plotter():
    
    df = pd.read_csv("map_data2.csv")
    
    fig = px.scatter_geo(df, lat='latitude', lon='longitude')
    fig.update_layout(title = 'World map', title_x=0.5)
    fig.show()




i=0
while i<=50:
    into_csv()  
    i+=1



plotter()    