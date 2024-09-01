from dotenv import load_dotenv, set_key  # Required to manage .env file easily
from tkinter import ttk
import os
import tkinter as tk
from tkinter import ttk  # Import ttk module for themed widgets
import sv_ttk
from pathlib import Path
import shutil
import threading
import subprocess
import threading
import time
import os
import json
import tkinter as tk
from tkinter import messagebox


class FileViewer:
    def __init__(self):
        self.file_dict = {
            'weights': {},
            'logs': {}
        }
        self.selected_index = ""
        self.selected_pth = ""
        self.env_path = Path('.env')   # Set the path of .env file
        self.load_dotenv_file()        # Load or create .env file
        self.commands = {}

        # Load files into Listboxes
        self.load_files()

        file_thread = threading.Thread(target=self.check_and_process_file, daemon=True)
        file_thread.start()

    def error_log(self, message):
        messagebox.showinfo("Command Error", f"There was an error in the command list json file:\n{message}")

    def check_and_process_file(self):
        while True:
            if os.path.exists("speaker.txt"):
                with open("speaker.txt", "r") as file:
                    content = file.read()
                    print(content)  # Process the content as needed
                self.selected_index = self.commands[content]['index']
                self.selected_pth = self.commands[content]['weight']
                os.remove("speaker.txt")
                self.buttonCall()
            time.sleep(1)
    def on_file_select(self, event):
        x = 1
        printer = True
        while x < 3:
            x += 1
            try:
                widget = event.widget
                index = int(widget.curselection()[0])
                file_name = widget.get(index)

                if widget == self.listbox_pth:
                    self.selected_pth = self.file_dict['weights'][file_name]
                    self.display_selected_pth.delete(
                        0, tk.END)  # Clear current contents
                    self.display_selected_pth.insert(
                        0, self.selected_pth)  # Show selected path
                    printer = False
                    print(f'success! {self.selected_pth}')
                else:
                    self.selected_index = self.file_dict['logs'][file_name]
                    self.display_selected_index.delete(
                        0, tk.END)  # Clear current contents
                    self.display_selected_index.insert(
                        0, self.selected_index)  # Show selected index
                    printer = False
                    print(f'success! {self.selected_index}')

                x = 5  # Break the loop after successful operation
            except Exception as e:
                if printer:
                    print('click failure, don\'t fret, trying again')


    def launch_tts(self):
        if self.tts_process and self.tts_process.poll() is None:
            self.tts_process.terminate()  # Terminate the process if it is still running
        self.tts_process = subprocess.Popen(
            ["path/to/tts_executable.exe"])  # Adjust path to your exe

    def on_closing(self):
        if self.tts_process:
            self.tts_process.terminate()
        self.root.destroy()

    def buttonCall(self):
        with open('config.txt', 'w') as file:
            json.dump({'model': self.selected_pth,
                      'index': self.selected_index}, file)
        print(f"Selected Index: {self.selected_index}")
        print(f'Selected Pth: {self.selected_pth}')
        return True

    def load_files(self):
        self.file_dict['weights'] = self.list_files('assets/weights', '.pth')

        self.file_dict['logs'] = self.list_files('logs', '.index')

        # Dump the model indexes
        with open("model_index.json", "w") as f:
            json.dump(self.file_dict, f, indent=4)

        # Read or create commands.json with template if it does not exist
        commands_file_path = 'commands.json'
        if not os.path.exists(commands_file_path):
            # Writing an empty file with a template as commented example
            with open(commands_file_path, 'w') as f:
                f.write("""{
        \"PUT_EXACT_COMMAND_HERE, FIND PATHS IN model_index.json_NEXT_TO_THIS_FILE\": {
           \"weight\": \"path\\\\to\\\\tomfoolery\\\\.pth\",
           \"index\": \"path\\\\to\\\\tomfoolery\\\\.index\",
           \"optional_PITCH_CHANGE_VALUE\": \"-3\"
        }
}""")
        else:
            with open(commands_file_path, 'r') as f:
                commands = json.load(f)
                # Process commands and map them to the files loaded in file_dict
                for command, paths in commands.items():
                    if command == "THIS_IS_A_SAMPLE_COMMAND_CHECK_model_index.json_NEXT_TO_THIS_FILE":
                        continue
                    weight_path = paths.get('weight')
                    if weight_path in self.file_dict['weights'].values():
                        self.commands[command] = {
                            'weight': weight_path,
                            'index': paths.get('index')
                        }
                    else:
                        self.error_log(f"Weight file not found: {weight_path}")
                    log_path = paths.get('index')
                    if log_path in self.file_dict['logs'].values():
                        self.commands[command] = {
                            'weight': weight_path,
                            'index': paths.get('index')
                        }
                    else:
                        self.error_log(f"Log file not found: {log_path}")
                    
                     
        
    def list_files(self, directory, extension):
        directory_path = Path.cwd() / directory
        files = [f for f in os.listdir(
            directory_path) if f.endswith(extension)]
        files_with_path = {f: str(directory_path / f) for f in files}
        return files_with_path

    def update_token(self):
        new_token = self.token_entry.get()
        # Update the TOKEN environment variable
        set_key(self.env_path, "ALERT_URL", new_token)
        print("Token updated:", new_token)

    def load_dotenv_file(self):
        """Load or create the .env file."""
        if not self.env_path.exists():
            self.env_path.write_text("ALERT_URL=")
        load_dotenv(self.env_path)



# Example usage
if __name__ == "__main__":
    app = FileViewer()
