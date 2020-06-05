#!/usr/bin/env python3

# importing the required module 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd
import matplotlib.ticker as mticker

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

link = 'https://www.arcgis.com/sharing/rest/content/items/b5e7488e117749c19881cce45db13f7e/data'
df = pd.read_excel(link, sheet_name='Antal avlidna per dag', use_cols=['Datum_avliden', 'Antal_avlidna'])

df['Datum_avliden'] = pd.to_datetime(df['Datum_avliden'], errors='coerce')
df = df.dropna(subset=['Datum_avliden'])

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# plotting the points  
plt.plot(df["Datum_avliden"],df["Antal_avlidna"])

plt.xticks(rotation=90)
  
# naming the x axis 
plt.xlabel('Datum') 
# naming the y axis 
plt.ylabel('Antal avlidna') 
 
total = df["Antal_avlidna"].aggregate(func = sum) 

# giving a title to my graph 
plt.title("Antal avlidna per dag (Totalt: {})".format(total)) 
  
# function to show the plot 
plt.show() 
