import streamlit as st
from openai import OpenAI


st.title("Translator")

with st.form("my_form"):
    client = OpenAI(api_key=st.secrets["OPEN_API_KEY"])



    # input_language = input("Select ")


    # output_language = input("Select output language (Spanish / Japanese / Mandarin/ English): ")
    input_lang = st.text_input(f"Enter input language")
    output_lang = st.text_input(f"Enter output language")
    text = st.text_area(f'Enter text to translate')
    submitted = st.form_submit_button("Submit")
    if submitted:
        user_prompt = f"""
        Input Language: {input_lang}
        Output Language: {output_lang}
        Text to translate: {text}
        """
        system_prompt = """
        The user will input text they want to translate. The user will also put in the language they want it to be translated in. Please translate the input language text into the output language. 
        """
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )


        st.write(response.choices[0].message.content)
