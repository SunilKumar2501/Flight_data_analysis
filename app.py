import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from db import DB

db = DB()
st.sidebar.title("Flight Analysis")
user_option = st.sidebar.selectbox("Menu",["Select One" , "Check Flights" ,"Analytics"])
if user_option == "Check Flights":
    st.title("Check Flights")
    col1,col2 = st.columns(2)
    city = db.fetch_city_names()
    with col1:
        source = st.selectbox("Source",sorted (city))
    with col2:
        destination = st.selectbox("Destination", sorted(city))

    if st.button("Search"):
        result = db.fetch_all_flights(source,destination)
        if len(result) > 0:
            # Display DataFrame with Custom Styling
            st.dataframe(result,use_container_width=True)
        else:
            st.text("SORRY,NO DATA AVAILABLE")
elif user_option == "Analytics":
    st.title("Analytics")
    airline,frequency = db.fetch_airline_frequency()
    fig = px.pie(values= frequency, names= airline, title='Flights per Airline')
    st.plotly_chart(fig)

    city,frequency = db.busy_airport()
    fig = px.bar(x = city, y = frequency, title='Flights per City')
    st.plotly_chart(fig)

    date,frequency = db.daily_frequency()
    fig = px.line(x = date, y = frequency, title='Date wise Frequency')
    st.plotly_chart(fig)

else:
    st.title("Tell us about the project")
