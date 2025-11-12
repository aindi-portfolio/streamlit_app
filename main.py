import streamlit as st
import pandas as pd

# load csv that has str and int columns
df = pd.read_csv("data/example.csv")

# display the dataframe
st.dataframe(df)