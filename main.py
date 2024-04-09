import streamlit as st
import pandas as pd

@st.cache_data
def load_csv(csv_file):
    df=pd.read_csv(csv_file)
    return df



stops=load_csv('Data/Officer_Traffic_Stops.csv')
st.dataframe(stops)

## Box plot
box = alt.Chart(stops).mark_boxplot().encode(
    x = alt.X('Was_a_Search_Conducted'),
    y = alt.Y('Driver_Age')
).properties(
    width = 500,
    title = 'Boxplot between Search Conducted vs Driver Age')
