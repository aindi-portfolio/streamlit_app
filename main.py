import streamlit as st
import pandas as pd

# read the csv file
df = pd.read_csv('data/example.csv')

st.dataframe(df)