import os
import streamlit as st
import openai
import time


# Get API key from environment variable
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"] 
api_key = os.environ["OPENAI_API_KEY"]
openai.api_key = api_key
# 设置页面配置
st.set_page_config(page_icon=None, layout="wide", initial_sidebar_state="collapsed")

# 隐藏streamlit标识
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)






# 设置标题
st.title("FUKUROKUJU AI")

# Set the placeholder
placeholder = st.empty()

# Set the CSS style
st.markdown(
    f"""
    <style>
        .my-text {{
            width: 30%;
            text-align: left;
            overflow-wrap: break-word;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Add the text to the placeholder with the CSS class
placeholder.markdown("<p class='my-text'>Fuk Luk Sau, are regarded in the East as symbols of wealth, longevity, and good fortune, and are also believed to protect people's health and promote longevity.</p>", unsafe_allow_html=True)


# Define a function to generate a response from OpenAI
def generate_response(prompt):
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt="According to the latest research in the field of biological sciences, can you explain...", 
        max_tokens=300, 
        n=1, 
        stop=None, 
        temperature=0.7,
    )
    # Extract the first choice from the response
    choice = response.choices[0].text.strip()
    # Return the choice
    return choice



def main():
    # Set the title and sidebar
    st.title("AI health consultant will answer your concerns.")

    # Get the user's question
    question = st.text_input("Enter your question:")

   # Check if the user has entered a question
    if question:
        # Display a "thinking" message to the user
        with st.spinner(text="Thinking..."):
            # Generate a response from OpenAI
            response = generate_response(question)

        # Display the response to the user
        st.write("Answer:")
        st.write(response)

    # Add a copy button for the user's question and answer
    if st.button("Consult with the FuKUROKUJU AI "):
        # Create empty frames for the question and answer
        public_question = st.empty()
        public_answer = st.empty()

        # Set the value of the public question
        public_question.text("Question: " + question)

        # Display a spinner while the AI generates a response
        with st.spinner(text="Thinking..."):
            # Generate a response from OpenAI
            response = generate_response(question)

        # Replace the spinner with the AI's response
        public_answer.text("Answer: " + response)












# Run the Streamlit app
if __name__ == "__main__":
    main()


    