import streamlit as st
import pandas as pd

# Execute this python file from root of this project for this line to work
df_deaths = pd.read_csv("./data/time_series_covid19_deaths_global.csv")

st.write("""
Deaths counts for each country and each date time - Variable count
""")
# Prepare data
df_deaths_by_country=df_deaths.melt(id_vars=["Province/State", "Country/Region",'Lat', "Long"], var_name='Date', value_name='Count')
# Display dataframe
df_deaths_by_country