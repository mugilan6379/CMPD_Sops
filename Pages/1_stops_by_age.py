import streamlit as st
import pandas as pd
import altair as alt
import main


stops=main.load_csv('Data/Officer_Traffic_Stops.csv')
st.dataframe(stops)
chart = alt.Chart(stops).mark_bar().encode(
    x='Was_a_Search_Conducted',
    y='count()',
    color='Was_a_Search_Conducted'
).properties(
    width=600,
    height=400
)

st.altair_chart(chart)

