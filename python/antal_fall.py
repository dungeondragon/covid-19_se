nd(c(1,2,3),c(4,5,6))#!/usr/bin/env python3

# importing the required module 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd
import matplotlib.ticker as mticker
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

link = 'https://www.arcgis.com/sharing/rest/content/items/b5e7488e117749c19881cce45db13f7e/data'

df = pd.read_excel(link, sheet_name='Antal per dag region', use_cols=['Statistikdatum', 'Totalt_antal_fall'])

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# plotting the points  
plt.plot(df["Statistikdatum"],df["Totalt_antal_fall"])

plt.xticks(rotation=90)
  
# naming the x axis 
plt.xlabel('Datum') 
# naming the y axis 
plt.ylabel('Antal fall') 

total = df["Totalt_antal_fall"].aggregate(func=sum)

# giving a title to my graph 
plt.title('Antal fall per dag (Totalt: {})'.format(total)) 
  
# function to show the plot 
plt.show() 
