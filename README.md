# Ryle's Streamlabs RVC TTS

Have celebrities or friends of the stream read out donations. 

### Hear it in action:

https://github.com/user-attachments/assets/a4a4987c-b577-4a85-a10e-0bb01f383e26

Requirements:

  This Project https://github.com/samfisherirl/Ryles-Streamlabs-RVC-TTS/releases
  
  RVC Studio (4gb; direct download links)
  
-  Nvidia:
    https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/RVC1006Nvidia.7z 
-  Intel/AMD:
    https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/RVC1006AMD_Intel.7z

  Socket Token:
    https://streamlabs.com/dashboard#/settings/api-settings
    - click "API tokens" tab

1) Download Requirements and get a socket_token. Place my application in the main dir for RVC 

3) define .env file



```env

ALERT_URL='{this_is_the_alert_box_url}' # THIS CAN BE FOUND HERE https://streamlabs.com/dashboard#/alertbox/general/tipping
SOCKET_TOKEN='{.self}'
```


2)  launch bat file and press 1 to set commands

3) back to menu, click 2 for launch

4) Run a single TEST donation by visiting the Tipping url for your popup donations page, run TEST once to have Webview configured 
https://streamlabs.com/dashboard#/alertbox/general/tipping
![image](https://github.com/user-attachments/assets/0ef10639-e7c9-4ab0-9d74-33ef3d705101)

5) open volume mixer, when you look at apps, there will be "python" or "webview" or "edge" (with denotation for webview) or "chrome" (with denotation for webview) ->  
set output to go to desired virtual Cable-{}.  Warning - Webview might not show up on volume mixer until a TTS is played. 

![image](https://github.com/user-attachments/assets/906c2f91-a2ae-4ecc-9e1c-01ffab6206d9)

6) TESTING will set random voices, you cannot customize the TTS test message. By default, the delimiter is "|" for user commands via tts. the listener window will print the model chosen prior to audio playing.

________________

example command: 

```tomfoolery```

example user donation:

```|tomfoolery| hi im tom```



example command: 

```tf```

example user donation:

```|tf| hi Im tom```
________________



6) Use Streamlabs Tipping Alertbox Test https://streamlabs.com/dashboard#/alertbox/general/tipping. Update the message delay for TTS under Message Template (set message template enable) and add 5s to text delay.

7) For the Browser Alert Box, to reduce resources, you can use the provided Browser window and capture with a chroma/color key (white background).

________________

- the commands are set by launching the bat file and selecting 1

![image](https://github.com/user-attachments/assets/79f6f47f-2125-43c3-ab2e-74862ed8966e)
