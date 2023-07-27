mkdir -p ~/.streamlit/
echo "[general]
email = \"hello@growave.it\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
