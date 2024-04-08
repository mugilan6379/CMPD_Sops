import streamlit as st
import pandas as pd

@st.cache_data
def load_csv(csv_file):
    df=pd.read_csv(csv_file)
    return df



stops=load_csv('Data/Officer_Traffic_Stops.csv')
st.dataframe(stops)