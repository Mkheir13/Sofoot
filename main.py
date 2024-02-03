import streamlit as st
import pandas as pd

st.title('Sofascore data')
st.write('This is a simple example of using Streamlit to create a data explorer')


df = pd.read_json('playersdata.json')
df.to_csv('data.csv', index=False)

df = pd.read_csv('data.csv')


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

