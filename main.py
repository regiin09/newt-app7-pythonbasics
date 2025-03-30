import streamlit as st
st.title("Weather forecast app")
place=st.text_input("Place: ")
days=st.slider("Forecast Days",min_value=1,max_value=5,help="Select the no of forecasting days")
option=st.selectbox("Select data to view",("temperature","sky"))
st.subheader(f"{option} for the next {days} in {place}")