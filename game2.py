import streamlit as st
import random
st.header("number guessing game")
st.write("enter number 1 to 10")
num = random.randint(1,10)
user=st.number_input("enter your number")
if st.button("▶"):
    if num==user:
        st.write("computer chose:",num)
        st.write("congrats😎👌🔥")
        st.success("🎉 Congratulations! You guessed the correct number.")
        st.balloons()
    elif user>10:
          st.write("you chose too high")
          st.write("computer chose:",num)   
          st.write("you lose🚨")
          
    else:
         st.write("computer chose:",num)   
         st.error("❌ You lost! .")