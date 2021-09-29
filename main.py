import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

import streamlit as st
import numpy as np

#Getting the live data from API

from urllib.request import urlopen

import json

url = "https://badger-analytics.herokuapp.com/boosts"

response = urlopen(url)

#Live data in json format
data_json = json.loads(response.read())

 #live data Native Balance
lvd1 = data_json['data']['boosts']['userData']
lvd2 = pd.DataFrame.from_dict(lvd1).T
lvd_nativeBal_sum = sum(lvd2['nativeBalance'])

#live data Non Native Balance
lvd3 = data_json['data']['boosts']['userData'] 
lvd4 = pd.DataFrame.from_dict(lvd3).T
#print(lvd4)
lvd_non_nativeBal_sum = sum(lvd4['nonNativeBalance'])

#Title
st.title('Badger Boost Data Visualization')



def createList(r1, r2):
    return [item for item in range(r1, r2+1)]


df = pd.read_csv('Native_Balance_Historical.csv')
if list(df['Native Balance'])[-1] == lvd_nativeBal_sum:
	df_temp = df
else:
	df_temp = df['Native Balance'].append(pd.Series(lvd_nativeBal_sum), ignore_index =True)
	
#Appended Data Frame Native Balance
lvd_native_balance = pd.DataFrame(df_temp, columns = ['Native Balance'])

#Appended Data Frame Non Native Balance
df1 = pd.read_csv('Non_Native_Balance_Historical.csv')
if list(df1['Non Native Balance'])[-1] == lvd_non_nativeBal_sum:
	df1_temp = df1
else:
	df1_temp = df1['Non Native Balance'].append(pd.Series(lvd_non_nativeBal_sum), ignore_index =True)

lvd_non_Native_balance = pd.DataFrame(df1_temp, columns = ['Non Native Balance'])


#Line Chart
st.line_chart(lvd_native_balance['Native Balance'])

st.line_chart(lvd_non_Native_balance['Non Native Balance'])

#Updating the csv files
lvd_native_balance.to_csv('Native_Balance_Historical.csv')
lvd_non_Native_balance.to_csv('Non_Native_Balance_Historical.csv')

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
