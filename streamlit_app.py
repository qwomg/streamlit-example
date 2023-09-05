import streamlit as st
import time
from PIL import Image
import requests
from io import BytesIO

# Simulate the generation of an image based on user input (replace with real API call)
def generate_image(theme, example):
    # Simulate a 10-second delay to mimic real API call
    st.write("Generating your coloring book...")
    time.sleep(10)

    # Normally, you'd make an API call here and get the image URL
    # For now, using a placeholder image from a public URL
    response = requests.get('https://www.w3schools.com/w3images/fjords.jpg')
    img = Image.open(BytesIO(response.content))
    return img

def main():
    st.title("Create Your Coloring Book")

    # Step 1: Introduction
    st.header("Step 1: Introduction")
    st.write("Welcome to the AI-powered Coloring Book Creator!")
    start = st.button("Start")

    # Initialize session state variables
    if 'theme_selected' not in st.session_state:
        st.session_state.theme_selected = False
    if 'example_selected' not in st.session_state:
        st.session_state.example_selected = False

    if start or st.session_state.theme_selected or st.session_state.example_selected:
        # Step 2: Choose Theme
        st.header("Step 2: Choose a Theme")
        animal = st.button("Animals", key="theme_animal")
        space = st.button("Space", key="theme_space")
        nature = st.button("Nature", key="theme_nature")
        
        theme = None
        if animal:
            theme = "Animals"
            st.session_state.theme_selected = True
        elif space:
            theme = "Space"
            st.session_state.theme_selected = True
        elif nature:
            theme = "Nature"
            st.session_state.theme_selected = True

        if st.session_state.theme_selected:
            # Step 3: Describe Image
            st.header("Step 3: Choose an Example")
            example1 = st.button("Example 1", key="example1")
            example2 = st.button("Example 2", key="example2")
            
            example = None
            if example1:
                example = "Example 1"
                st.session_state.example_selected = True
            elif example2:
                example = "Example 2"
                st.session_state.example_selected = True

            if st.session_state.example_selected:
                # Step 4: Generate and Preview Image
                st.header("Step 4: Preview Image")
                generate = st.button("Create my color book!")
                if generate:
                    generated_image = generate_image(theme, example)
                    st.image(generated_image, caption="Generated Image", use_column_width=True)

                    # Step 5: Print the Book
                    st.header("Step 5: Print the Book")
                    print_button = st.button("Print the Book")
                    if print_button:
                        st.write("Printing your coloring book...")
                        # Normally, you'd trigger a print action here. For now, showing a placeholder image.
                        st.image('https://www.w3schools.com/w3images/fjords.jpg', caption="Your Printable Coloring Book", width=600)
        
if __name__ == "__main__":
    main()
