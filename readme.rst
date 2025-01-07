=============
Instructions
=============
https://streamlit.io/

virtualenv -p python3 venv
source venv/bin/activate

pip install streamlit
pip install watchdog

streamlit run streamlit_app.py


pip3 freeze > requirements.txt
pip install -r requirements.txt





Optionally, add a .streamlit folder to customize the app's server settings. 
Create a config.toml file inside .streamlit with the following content:

[server]
port = $PORT
headless = true
enableCORS = false


