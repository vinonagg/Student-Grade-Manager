import streamlit as st

st.title("My Streamlit Application")
st.write("Welcome to my Streamlit app! This is a simple example to demonstrate how to use Streamlit for building interactive web applications.")    

name = st.text_input("Enter your name:")
st.write(f"Hello, {name}! Nice to meet you.")

age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

if st.button("Click me!"):
    st.write("Button clicked! You can add more functionality here.")

number = st.slider("Select a number:", 0, 100, 50)
st.write(f"You selected the number: {number}")

city = st.selectbox("Select your city:", ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])
st.write(f"You selected: {city}")   

agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing to the terms and conditions.") 

