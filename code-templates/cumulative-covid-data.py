import streamlit as st
import pandas as pd
import altair as alt

# Execute this python file from root of this project for this line to work
df_confirmed = pd.read_csv("./data/time_series_covid19_confirmed_global.csv")
df_deaths = pd.read_csv("./data/time_series_covid19_deaths_global.csv")
df_recovered = pd.read_csv("./data/time_series_covid19_recovered_global.csv")

st.title("""
Cumulative examples for covid data
""")

# Death Cases plots
st.write("""
# Death Number from Covid19
""")
st.write("""
## Cumulative deaths number
""")
df_deaths_by_country_cumul=df_deaths.melt(id_vars=["Province/State", "Country/Region",'Lat', "Long"], var_name='Date', value_name='Count')
df_deaths_by_country_cumul

selected_country_deaths = st.multiselect('Select country for cumulative total deaths', df_deaths_by_country_cumul["Country/Region"].unique())
if selected_country_deaths:
  mask_countries_cumul = df_deaths_by_country_cumul['Country/Region'].isin(selected_country_deaths)
  countries_cumul = df_deaths_by_country_cumul[mask_countries_cumul]

  countries_cumul = countries_cumul.groupby(['Country/Region', 'Date']).sum() \
    .groupby("Date").cumsum().reset_index()

  st.write("countries_cumul=", countries_cumul)

  chart_death = alt.Chart(countries_cumul).mark_line().encode(
    x=alt.X('Date:T'),
    y=alt.Y('Count:Q'),
    color=alt.Color("Country/Region:N")
  ).properties(title="Cumulative deaths number")
  st.altair_chart(chart_death, use_container_width=True)
else:
  st.write("No country was selected. Please select at lease one country to display the plot.")

# Confirmed Cases plots
st.write("""
# Confirmed number from covid19
""")
st.write("""
## Cumulative confirmed number
""")
df_confirmed_by_country_cumul=df_confirmed.melt(id_vars=["Province/State", "Country/Region",'Lat', "Long"], var_name='Date', value_name='Count')
df_confirmed_by_country_cumul

selected_country_confirmed = st.multiselect('Select country for cumulative total confirmed', df_confirmed_by_country_cumul["Country/Region"].unique())
if selected_country_confirmed:
  mask_countries_cumul_conf = df_confirmed_by_country_cumul['Country/Region'].isin(selected_country_confirmed)
  countries_cumul_conf = df_confirmed_by_country_cumul[mask_countries_cumul_conf]

  countries_cumul_conf = countries_cumul_conf.groupby(['Country/Region', 'Date']).sum() \
    .groupby("Date").cumsum().reset_index()

  countries_cumul_conf

  chart_confirmed = alt.Chart(countries_cumul_conf).mark_line().encode(
    x=alt.X('Date:T'),
    y=alt.Y('Count:Q'),
    color=alt.Color("Country/Region:N")
  ).properties(title="Cumulative confirmed number")
  st.altair_chart(chart_confirmed, use_container_width=True)
else:
  st.write("No country was selected. Please select at lease one country to display the plot.")

# Recovered Cases plots
st.write("""
# Recovered number from covid19
""")
st.write("""
## Cumulative recovered number
""")
df_recovered_by_country_cumul=df_recovered.melt(id_vars=["Province/State", "Country/Region",'Lat', "Long"], var_name='Date', value_name='Count')
df_recovered_by_country_cumul

selected_country_recovered = st.multiselect('Select country for cumulative total recovered', df_recovered_by_country_cumul["Country/Region"].unique())
if selected_country_recovered:
  mask_countries_cumul_recov = df_recovered_by_country_cumul['Country/Region'].isin(selected_country_recovered)
  countries_cumul_recov = df_recovered_by_country_cumul[mask_countries_cumul_recov]

  countries_cumul_recov = countries_cumul_recov.groupby(['Country/Region', 'Date']).sum() \
    .groupby("Date").cumsum().reset_index()

  countries_cumul_recov

  chart_recovered = alt.Chart(countries_cumul_recov).mark_line().encode(
    x=alt.X('Date:T'),
    y=alt.Y('Count:Q'),
    color=alt.Color("Country/Region:N")
  ).properties(title="Cumulative recovered number")
  st.altair_chart(chart_recovered, use_container_width=True)
else:
  st.write("No country was selected. Please select at lease one country to display the plot.")