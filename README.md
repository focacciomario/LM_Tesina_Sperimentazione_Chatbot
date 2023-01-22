# ✨ Streamlit ChatGPT/DALLE-2 ChatBot [![Progetto: Università](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Mario-Focaccio-dkgreen.svg?colorB=ff0000)](https://github.com/focacciomario/LM_Tesina_Sperimentazione_Chatbot)

Una semplice webapp sviluppata utilizzando Streamlit e integrata con le APIs di OpenAI per la generazione di immagini (DALL-E) e testi (GPT-3), entrambi a partire da descrizioni testuali anche complesse. 

![demo_txt](https://github.com/focacciomario/LM_Tesina_Sperimentazione_Chatbot/blob/main/static/screen_recording.gif)



## Installazione:
* Dal terminale eseguire il comando ***pip install -r requirements.txt*** per installare i pacchetti e le dipendenze descritte nel file *requirements.txt* 

## Come usare la repository:
1. Clona questa repository (o effettua semplicemente il download) e installa le dipendenze come descritto sopra
2. Naviga all'interno della tua [area personale di OpenAI API](https://beta.openai.com/account/api-keys), effettua la login e genera la tua chiave API. Assicurati di inserire la chiave API generata nella sezione **"OpenAI_API_Key"*** che trovi nel file app.py. Questa sarà utilizzata dalla web application per il funzionamento di base.
***( Nel mio caso sto utilizzando la versione Free Trial che fornisce 18$ di credito gratuito. )***
2. Avvia il comando: 
```
streamlit run app.py
```
3. Naviga nel tuo browser all'indirizzo http://localhost:8501


## Il risultato finale può essere visualizzato in questi due link: 
1. [OnRender](https://streamlit-gpt3-walle-chatbot.onrender.com/) - Web App Deploy Free using OnRender
2. [Streamlit](https://focacciomario-lm-tesina-sperimentazione-chatbot-app-70f0r2.streamlit.app/) - Web App Deploy Free using Streamlit

