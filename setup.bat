CALL venv\Scripts\activate 

venv\Scripts\pip.exe install pyinstaller setuptools

.\venv\Scripts\pyinstaller --windowed --icon=app.ico --noconfirm --add-data "D:\RVC1006Nvidia\venv\Lib\site-packages\webview*;webview" --clean webviewer.py
.\venv\Scripts\pyinstaller --windowed --icon=app.ico --noconfirm --add-data "D:\RVC1006Nvidia\venv\Lib\site-packages\sv_ttk*;sv_ttk"  --clean RyleTTS.py
.\venv\Scripts\pyinstaller --console --icon=app.ico --noconfirm --clean sock.py
