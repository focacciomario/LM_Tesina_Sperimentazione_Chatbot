import os
import openai
from PIL import Image
import streamlit as st

openai.api_key = "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"
#openai.api_key = os.environ.get('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')
#openai.api_key = st.secrets[]

st.set_page_config(
    page_title="Tesina LM Mario Focaccio",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
)

#@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=False)
def openai_completion(prompt):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=150,
      temperature=0.5
    )
    return response['choices'][0]['text']

#@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=False)
def openai_image(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=2,
      size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url

top_image = Image.open('static/banner_top.png')
bottom_image = Image.open('static/banner_bottom.png')
main_image = Image.open('static/main_banner.png')

st.sidebar.image(top_image,use_column_width='auto')
format_type = st.sidebar.selectbox('Quale engine vuoi utilizzare? 😉',["ChatGPT (Testo)","DALL-E 2 (Immagini)"])
st.sidebar.image(bottom_image,use_column_width='auto')

st.image(main_image,use_column_width='auto')
st.title("📄 :green[Mario Focaccio] - _ChatBot: Sperimentazione_ ")

if format_type == "ChatGPT (Testo)":
    input_text = st.text_area("Inserisci una descrizione testuale... 🙋",height=50)
    chat_button = st.button("Dammi una risposta ✨")

    if chat_button and input_text.strip() != "":
        with st.spinner("Ci sto pensando...💫"):
            openai_answer = openai_completion(input_text)
            st.success(openai_answer)
    else:
        st.warning("Inserisci una descrizione! ⚠")

else:
    input_text = st.text_area("Inserisci una descrizione testuale... 🙋",height=50)
    image_button = st.button("Crea un'immagine fantastica 🚀")

    if image_button and input_text.strip() != "":
        with st.spinner("Caricamento...💫"):
            image_url = openai_image(input_text)
            st.image(image_url, caption='Generated by OpenAI')
    else:
        st.warning("Inserisci una descrizione! ⚠")

st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:mario.focaccio@studenti.unicz.it'><strong>Mario Focaccio</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<center><a href='https://medicina.unicz.it' style='color:White;text-decoration:none;font-weight:800;'>Università degli Studi Magna Graecia di Catanzaro</a> — <strong>A.A. 2022 - 2023</strong></center>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)

