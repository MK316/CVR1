import streamlit as st

# Title of the app
st.title("Interactive English Conversation App")

# Introduction from the app
st.write("Hi! My name is Streamy, and I would love to chat with you. Let's start!")

# Step 1: Ask for the user's name
name = st.text_input("What's your name?", "")

if name:
    st.write(f"Nice to meet you, {name}!")
    
    # Step 2: Ask for the user's age
    age = st.text_input(f"How old are you, {name}?", "")

    if age:
        try:
            age = int(age)  # Convert age to an integer if possible
            difference = 23 - age  # Compare to your own age (23)
            if difference > 0:
                st.write(f"I'm 23, so I'm {difference} years older than you.")
            elif difference < 0:
                st.write(f"I'm 23, so you're {abs(difference)} years older than me!")
            else:
                st.write("Wow! We're the same age!")
            
            # Step 3: Ask for the user's hometown
            hometown = st.text_input(f"So, {name}, where is your hometown?", "")

            if hometown:
                st.write(f"{hometown} sounds like a great place!")
                
                # Step 4: Ask for the user's favorite singer
                favorite_singer = st.text_input(f"Who's your favorite singer, {name}?", "")

                if favorite_singer:
                    st.write(f"{favorite_singer} is amazing! I love their music too.")
                    
                    # Step 5: Ask for the user's favorite color
                    favorite_color = st.text_input(f"What's your favorite color, {name}?", "")

                    if favorite_color:
                        st.write(f"{favorite_color} is such a nice color!")

                        # Final message
                        st.write(f"It was great talking to you, {name}! Let's chat again sometime.")
        except ValueError:
            st.write("Please enter a valid number for age.")
