import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

st.title("World bank data-India")
dataset=pd.read_csv('World_Bank_India_assignment.csv',skiprows=4)
dataset=dataset[['Indicator Name','2010','2011','2012','2013','2014','2015','2016','2017','2018']]
dataset=dataset.T

f=open('simplified.csv','w')
df=pd.DataFrame(dataset)
df.to_csv('simplified.csv',mode='a', header=False)

dataset=pd.read_csv('simplified.csv')
dataset=dataset[['Indicator Name','Physicians (per 1,000 people)','Number of deaths ages 5-9 years','People using safely managed sanitation services, rural (% of rural population)']]
dataset.set_index('Indicator Name',inplace=True)

st.write(dataset)
