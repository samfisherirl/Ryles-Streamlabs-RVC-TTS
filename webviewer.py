import webview
import os
from dotenv import load_dotenv, set_key 
load_dotenv('.env')
token = os.getenv("ALERT_URL")
window = webview.create_window("AlertBox", url=token)
webview.start()
