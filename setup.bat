CALL .\venv\Scripts\python.exe -m pip install --upgrade setuptools pyinstaller sv-ttk
CALL .\venv\Scripts\pyinstaller --windowed --icon=app.ico --noconfirm --add-data "venv\lib\site-packages\sv_ttk;sv_ttk"  --clean RyleTTS.py

CALL .\venv\Scripts\pyinstaller --windowed --icon=app.ico --noconfirm --add-data "venv\Lib\site-packages\webview;webview" --clean webviewer.py
CALL .\venv\Scripts\pyinstaller --console --icon=app.ico --noconfirm --clean sock.py
