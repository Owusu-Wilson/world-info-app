import streamlit as st
import geocoder
import pandas as pd
import requests

df = pd.read_csv('countries.csv')
# cities_data = pd.read_csv('world-cities.csv')/

ip_address = geocoder.ip('me').ip
location = geocoder.ip(ip_address)


current_location = location.country
st.title("Know the Weather of the major cities in the world", current_location)
st.info("Sponsored by weather.api")

mask = df['Alpha-2 code'] == current_location


# Get the index of the first occurrence of the target value
row_index = df.index[mask].tolist()[0]
# Get the index of the first occurrence of the target value
# selected_location = st.selectbox(label="Select a City", options=cities_data['name'], index=row_index)
# st.dataframe(cities_data.head())

cityName = st.text_input("Enter the name of a City")
goBtn = st.button("Search City")

if goBtn:
    params = {
        'apiKey': '262823828195400eb18143315231311',
        'city':cityName
    }
    url = f"https://api.weatherapi.com/v1/search.json?key={params['apiKey']}&q={params['city']}"

    res = requests.get(url)
# print(res.json())

    for i in res.json():
        choice = st.button(f"{i['name']}, {i['country']}", key=i)
    st.json(res.json())