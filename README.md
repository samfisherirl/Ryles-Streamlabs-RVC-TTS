# Ryle-s-Streamlabs-RVC-TTS
0) download https://github.com/samfisherirl/Ryles-Streamlabs-RVC-TTS/releases/download/v0.9/RyleTTS.7z

1) get a socket_token
https://streamlabs.com/dashboard#/settings/api-settings
2)  launch bat file

3) setup commands and .env file
```env

TOKEN='{this_is_the_alert_box_url}'
SOCKET_TOKEN='{.self}'
```
5) back to menu, click 2 for launch

6) open volume mixer, when you look at apps, there will be "python" or "webview" or "edge" or "chrome" -> suboption 
set output to go to desired Cable-{}. 


7) TESTING will set random voices, you cannot customize the TTS test message. By default, the delimiter is "|" for user commands via tts. the listener window will print the model chosen prior to audio playing.  


example: 

```|tomfoolery| hi im tom```

or

```|tf| hi Im tom```



8) Use Streamlabs Tipping Alertbox Test https://streamlabs.com/dashboard#/alertbox/general/tipping. Update the message delay for TTS under Message Template (set message template enable) and add 5s to text delay.  


- the commands are set by launching the bat file and selecting 1

![image](https://github.com/user-attachments/assets/79f6f47f-2125-43c3-ab2e-74862ed8966e)
