import streamlit as st
st.header("login form")
email=st.text_input("enter your email")
password=st.text_input("enter your password")
if st.button("submit"):
   if email=="Aaryan"and password=="1234":
    st.success("your email and password are correct")
   else:("the email or password is incorrect")