import streamlit as st
import joblib
model = joblib.load("Sector of farmers queries")
html_temp="""
<div style="background-color:white;padding:10px">
<h1 style="color:green;text-aling:center;">WELCOME TO KISAN CALL CENTER </h1>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)


st.subheader('Here we will help you to find the sector of your queries')
name = st.text_input("Please enter your name:","Type Here")
state = st.text_input("Please enter your state","Type Here")
ip = st.text_input("Please enter your query:","Type Here")
op = model.predict([ip])
if st.button('NEXT'):
 
  st.title(f"HELLO {name}!")
  st.title(f"You should consult to {op[0]} Department for your query")
  st.text(" ")
  st.subheader("please contact to  toll free number:1800-180-1551 and for BSNL landline Toll-Free number: 1551")
 
  
st.write(" ")  
st.write("This is the Machine Learning webapp of accuracy level 90% ")
st.write("THANKYOU")

  
  
 
