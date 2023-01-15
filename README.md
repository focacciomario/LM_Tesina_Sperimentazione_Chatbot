# ✨ Streamlit based ChatGPT/DALLE-2 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Mario-Focaccio-dkgreen.svg?colorB=ff0000)](https://github.com/focacciomario/LM_Tesina_Sperimentazione_Chatbot)

Una semplice webapp sviluppata utilizzando Streamlit e integrata con le APIs di OpenAI per la generazione di immagini e testi a partire da descrizioni testuali. 

![demo_txt](https://github.com/focacciomario/LM_Tesina_Sperimentazione_Chatbot/blob/main/static/screen_recording.gif)

![demo_img](https://user-images.githubusercontent.com/29462447/212479452-3d59ed7b-cbc3-43f1-bdb9-5e9d3b37dadc.gif)

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


## Risultato:

![1](https://user-images.githubusercontent.com/29462447/212479438-b2774381-122c-40b3-8380-5a7fa1336483.png)

![2](https://user-images.githubusercontent.com/29462447/212479439-6e6ce078-e61b-4430-9eba-0931b1b199d5.png)
