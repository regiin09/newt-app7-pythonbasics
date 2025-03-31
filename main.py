import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast app")
place=st.text_input("Place: ")
days=st.slider("Forecast Days",min_value=1,max_value=5,help="Select the no of forecasting days")
option=st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} in {place}")
if place:
    filtered_data=get_data(place,days)
    if option=="Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates=[dict["dt_txt"] for dict in filtered_data]
        figure=px.line(x=dates,y=temperatures,labels={"x":"dates ","y":"temperature (C)"})
        st.plotly_chart(figure)
    if option=="Sky":
        images={"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
        sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths=[images[condition] for condition in sky_condition]
        st.image(image_paths,width=115)