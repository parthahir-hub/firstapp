import streamlit as st
st.text("hi")
a=st.text_input("enter your name")
b=st.number_input("enter your age")
c=st.date_input("enter date of login")
e=st.text_area("write something about you")
d=st.button("show details")
if d==True:
    st.text(f"your name is {a}")
    st.text(f"your age is {b}")
    st.text(f"todays date is {c}")
    st.text(f"here is something you wrote about yourself:- \n {e}")
