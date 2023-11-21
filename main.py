import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search of Happiness")

df = pd.read_csv("Data/happy.csv")

x_axis = st.selectbox("Select data for the X-axis", ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select data for the Y-axis", ("GDP", "Happiness", "Generosity"))

st.subheader(f"{x_axis} and {y_axis}")

figure = px.scatter(x=df[x_axis.lower()], y=df[y_axis.lower()], labels={"x":x_axis, "y":y_axis})

st.plotly_chart(figure)