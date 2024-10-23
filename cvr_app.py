import streamlit as st

# Title of the app
st.title("Simple Conversation App")

# Introduction
st.write("Hello! Let's have a simple conversation.")

# Step 1: Ask for user's age
age = st.text_input("How old are you?", "")

# Respond to the user's age
if age:
    try:
        age = int(age)  # Convert age to an integer if possible
        st.write(f"I'm {age + 2} years older than you!")
    except ValueError:
        st.write("Please enter a valid number for age.")

# Step 2: Ask for user's hometown
hometown = st.text_input("Where is your hometown?", "")

# Respond to the user's hometown
if hometown:
    st.write(f"I'm from {hometown} too!")

# Step 3: Ask for the user's favorite singer
favorite_singer = st.text_input("Who is your favorite singer?", "")

# Respond to the favorite singer
if favorite_singer:
    st.write(f"I love listening to {favorite_singer} too!")

# Step 4: Ask for the user's favorite color
favorite_color = st.text_input("What is your favorite color?", "")

# Respond to the favorite color
if favorite_color:
    st.write(f"{favorite_color} is a beautiful color!")

# Final message
st.write("It was nice talking to you!")
