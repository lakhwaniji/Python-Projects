import streamlit as st
import plotly.express as px
from backend import get_data
st.title('Weather Forecasting App')
place=st.text_input("Place :")
days=st.slider("Forecast",min_value=1,max_value=5,help="Select How many no.of days you would like to see")
option=st.selectbox("Select Temp or Sky",("Temp","Sky"))
st.subheader(f'''You have selected {place} for {option} for {days} days''')
dates=[]
if(option=="Temp" and place!=""):
    raw_data=get_data(place,days)
    temps=[d['main']['temp'] for d in raw_data]
    dates = [d['dt_txt'] for d in raw_data]
    figure=px.line(x=dates,y=temps,labels={"x":"Date","y":"Temperature(c)"})
    st.plotly_chart(figure)
if(option=="Sky" and place!=0):
    raw_data=get_data(place,days)
    dates = [d['dt_txt'] for d in raw_data]
    weather=[d['weather'][0]['main'] for d in raw_data]
    dic={"Clear":"images/Clear.png","Clouds":"images/Cloud.png","Rain":"images/Rain.png","Snow":"images/Snow.png"}
    imagepaths=[dic[i] for i in weather]
    st.image(imagepaths,width=115)