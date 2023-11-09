import streamlit as st
import geocoder
import pandas as pd




df = pd.read_csv('countries.csv')

ip_address = geocoder.ip('me').ip
location = geocoder.ip(ip_address)


current_location = location.country

# Set page configuration
st.set_page_config(
    page_title="Country Book",
    page_icon=":chart_with_upwards_trend:",  # You can use an emoji as the icon
    layout="wide",  # Use "wide" layout for full-width
)
st.title("Find Information about all Countries", current_location)

st.divider()
image_urls = []
for i in df['Alpha-2 code']:
    image_urls.append(f"https://flagsapi.com/{i}/flat/64.png")
# Number of columns
num_columns = 5

# Calculate the number of rows needed
num_rows = -(-len(image_urls) // num_columns)  # Ceiling division

# Create a layout with the specified number of columns
columns = [st.columns(num_columns, gap="medium") for _ in range(num_rows)]

# Display images in the layout
for i, row in enumerate(columns):
    for j, col in enumerate(row):
        index = i * num_columns + j
        if index < len(image_urls):
            col.image(image_urls[index], caption=f"{df['Country'][index]}", width=100)
            # col.text(f"Code: {df['Alpha-2 code'][index]}")

# You can customize the layout and styling as needed