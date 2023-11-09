import streamlit as st
import geocoder
import pandas as pd


df = pd.read_csv('countries.csv')

ip_address = geocoder.ip('me').ip
location = geocoder.ip(ip_address)


current_location = location.country
st.title("Know the Weather of the major cities in the world", current_location)
st.info("Sponsored by weather.api")

mask = df['Alpha-2 code'] == current_location


# Get the index of the first occurrence of the target value
row_index = df.index[mask].tolist()[0]
# Get the index of the first occurrence of the target value
selected_location = st.selectbox(label="Select a City", options=df['Country'], index=row_index)

newmask = df['Country'] == selected_location
row_number = df.index[newmask].tolist()[0]

image_col, text_col = st.columns(2)
image_col.image(f"https://flagsapi.com/{df['Alpha-2 code'][row_number]}/flat/64.png")
text_col.info(df['Country'][row_number])