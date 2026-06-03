import streamlit as st
num1=int(st.number_input("enter number"))
if st.button("click"):
    for i in range(1,11):
        st.write(f"{num1} * {i} = {num1*i}")