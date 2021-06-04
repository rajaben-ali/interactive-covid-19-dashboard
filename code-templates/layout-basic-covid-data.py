import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# This line needs to be the first one to be called in the script
# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.title('Dashboard for Covid19 data')

# Load the csv files
df_confirmed = pd.read_csv("./data/time_series_covid19_confirmed_global.csv")
df_deaths = pd.read_csv("./data/time_series_covid19_deaths_global.csv")
df_recovered = pd.read_csv("./data/time_series_covid19_recovered_global.csv")

# Data Preparation - Cumulative data
# Confirmed cases
df_confirmed_cumul = df_confirmed.melt(id_vars=["Province/State", "Country/Region",'Lat', "Long"], var_name='Date', value_name='Count')
# Death cases
df_deaths_cumul = df_deaths.melt(id_vars=["Province/State", "Country/Region",'Lat', "Long"], var_name='Date', value_name='Count')
# Recovered cases
df_recovered_cumul = df_recovered.melt(id_vars=["Province/State", "Country/Region",'Lat', "Long"], var_name='Date', value_name='Count')

# Plot for the confirmed, deaths and recovered and for one selected country
# Prepare Data
options_csv_country = np.unique(np.concatenate((df_confirmed_cumul["Country/Region"].unique(),
  df_deaths_cumul["Country/Region"].unique(),
  df_recovered_cumul["Country/Region"].unique()),0))

s_csv_country = st.selectbox('Select one country to see the number of confirmed cases, deaths cases and recovered cases',
  options_csv_country)

# TODO: plot the selected country's death line chart, confirmed chart and recovered line chart in one
s_csv_country

# Space out the maps
c1, c2, c3 = st.beta_columns((1, 1, 1))

with c1:
  with st.beta_expander('Cumulative number of confirmed cases'):
    st.write('Expanded contant C1')

with c2:
  with st.beta_expander('Cumulative number of death cases'):
    selected_country_d = st.multiselect('Select country for cumulative total deaths', df_deaths_cumul["Country/Region"].unique())
    if selected_country_d:
      countries_cumul = df_deaths_cumul[df_deaths_cumul['Country/Region'].isin(selected_country_d)]
      countries_cumul = countries_cumul.groupby(['Country/Region', 'Date']).sum() \
        .groupby("Date").cumsum().reset_index()

      chart_death_cumul = alt.Chart(countries_cumul).mark_line().encode(
        x=alt.X('Date:T'),
        y=alt.Y('Count:Q'),
        color=alt.Color("Country/Region:N")
      ).properties(title="Cumulative deaths number")
      st.altair_chart(chart_death_cumul, use_container_width=True)
    else:
      st.write("No country was selected. Please select at lease one country to display the plot.")

with c3:
  with st.beta_expander('Cumulative number of recovered cases'):
    st.write('Expanded contant C3')


# Space out the maps so the second one is 2x the size of the other three
c5, c6, c7, c8 = st.beta_columns((1, 2, 1, 1))

with c5:
  with st.beta_expander('c5'):
    st.write('Expanded contant C5')

with c6:
  with st.beta_expander('c6'):
    st.write('Expanded contant C6')

with c7:
  with st.beta_expander('c7'):
    st.write('Expanded contant C7')

with c8:
  with st.beta_expander('c8'):
    st.write('Expanded contant C8')
