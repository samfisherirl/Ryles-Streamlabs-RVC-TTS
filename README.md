# Ryle-s-Streamlabs-RVC-TTS

1) get a socket_token
https://streamlabs.com/dashboard#/settings/api-settings
2)  launch bat file

3) setup commands and .env file
TOKEN='{this_is_the_alert_box_url}''
SOCKET_TOKEN='{.self}'

4) back to menu, click 2 for launch

5) open volume mixer, when you look at apps, there will be "python" or "webview" or "chrome" -> suboption 
set output to go to desired Cable-{}

6) TESTING will set random voices, allowing for testing. then in Streamlabs, use messsagetemplate for custom voice testing -> commands
By default, the delimiter is "|"

so the user will put the command between pipes. 

example

```|tomfoolery| hi im tom```

or
```|tf| hi Im tom```
