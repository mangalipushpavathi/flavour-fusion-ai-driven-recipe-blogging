import streamlit as st
import google.generativeai as genai
import random
import os

# Set up the Google API key
API_KEY = "AIzaSyBqYMblnybqRmlNPmqEA0sggBl9KBS6m30"  # Replace with your actual API key
os.environ["AIzaSyBqYMblnybqRmlNPmqEA0sggBl9KBS6m30"] = API_KEY
genai.configure(api_key=API_KEY)

# Joke list for entertainment
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why do Python programmers prefer snakes? Because they don't need semicolons!",
    "What is a programmer's favorite place to hang out? The Stack Overflow!"
]

def get_joke():
    return random.choice(jokes)

def recipe_generation(user_input, word_count):
    """Generates a recipe based on user input and specified word count."""
    try:
        st.info("Generating your recipe... Please wait!")
        st.success(get_joke())  # Display a random joke while waiting
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Generate a {word_count}-word recipe for {user_input}.")
        
        if response and hasattr(response, 'text'):
            return response.text
        else:
            return "Sorry, something went wrong. Please try again."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Flavour Fusion: AI-Driven Recipe Blogging")
st.write("Generate unique and customized recipe blogs using AI!")

# User Input
user_input = st.text_input("Enter a Recipe Topic:", placeholder="e.g., Vegan Chocolate Cake")
word_count = st.number_input("Word Count:", min_value=100, max_value=2000, value=500, step=100)

generate_btn = st.button("Generate Recipe")

if generate_btn and user_input:
    recipe = recipe_generation(user_input, word_count)
    st.subheader("Generated Recipe:")
    st.write(recipe)

# Footer
st.write("Powered by Google Generative AI - Gemini 1.5 Flash")
