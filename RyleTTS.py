"""used for setting commands for the TTS"""

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
import tkinter.font as tkFont
import traceback


class FileViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Viewer")

        self.file_dict = {
            'weights': {},
            'logs': {}
        }
        self.selected_index = ""
        self.selected_pth = ""
        self.env_path = Path('.env')   # Set the path of .env file
        self.load_dotenv_file()        # Load or create .env file
        self.commands = {}
        listbox_font = tkFont.Font(family="Arial", size=14)
        header_font = tkFont.Font(family="Arial", size=20)
        self.info_label = ttk.Label(
            self.root, text="This GUI allows you to set commands yourself.", font=header_font)
        self.info_label.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.token_label = ttk.Label(self.root, text="Alert Box Token URL:")
        self.token_label.grid(row=1, column=0, sticky="ew")

        self.token_entry = ttk.Entry(self.root, width=80)
        self.token_entry.insert(0, os.getenv("TOKEN", ""))
        self.token_entry.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.update_button = ttk.Button(
            self.root, text="Update Token", command=self.update_token)
        self.update_button.grid(row=3, column=0, columnspan=2, sticky="ew")

        self.launch_tts_button = ttk.Button(
            self.root, text="Launch TTS Alert Box", command=self.launch_tts)
        self.launch_tts_button.grid(row=4, column=0, columnspan=2, sticky="ew")

        # Listboxes for displaying files
        self.listbox_pth = tk.Listbox(
            self.root, height=10, width=40, font=listbox_font)
        self.listbox_pth.grid(row=5, column=0, sticky="ew")
        self.listbox_index = tk.Listbox(
            self.root, height=10, width=40, font=listbox_font)
        self.listbox_index.grid(row=5, column=1, sticky="ew")
        self.listbox_pth.bind('<<ListboxSelect>>', self.on_file_select)
        self.listbox_index.bind('<<ListboxSelect>>', self.on_file_select)

        # Display Entries for selected paths
        self.display_selected_pth = ttk.Entry(self.root, width=40)
        self.display_selected_pth.grid(row=6, column=0, sticky="ew")
        self.display_selected_index = ttk.Entry(self.root, width=40)
        self.display_selected_index.grid(row=6, column=1, sticky="ew")
        # Add ListView for commands
        self.commands_listbox = tk.Listbox(self.root, height=10, width=40, font=listbox_font)
        self.commands_listbox.grid(row=8, column=0, columnspan=2, sticky="ew")

        # Delete Button for commands
        self.delete_command_button = ttk.Button(self.root, text="Delete Command", command=self.delete_command)
        self.delete_command_button.grid(row=9, column=0, columnspan=2, sticky="ew")

        self.load_commands()


        # Load files into Listboxes
        self.load_files()

        # Input field for new command names
        # Spinbox for pitch input
        self.pitch_value = ttk.Entry(self.root, width=40)
        self.pitch_value.grid(row=8, column=0, sticky="ew")
        self.pitch_value.insert(0, "0")
        # Add command Button
        self.pitcher = ttk.Button(self.root, text="<- Pitch Change",
                                             command=self.add_command)
        self.pitcher.grid(row=8, column=1, sticky="ew")
        # Input field for new command names
        self.new_command_name_entry = ttk.Entry(self.root, width=40)
        self.new_command_name_entry.grid(row=9, column=0, sticky="ew")

        self.add_command_button = ttk.Button(self.root, text="<- Add Command",
                                             command=self.add_command)
        self.add_command_button.grid(row=9, column=1, sticky="ew")

        # Shift existing Listbox and Delete button down to row 9 and 10
        self.commands_listbox.grid(row=10, column=0, columnspan=2, sticky="ew")
        self.delete_command_button.grid(
            row=11, column=0, columnspan=2, sticky="ew")

        # Handle clean exit
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind("<Escape>", lambda event: self.root.destroy())

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
        
    def load_commands(self):
        # Load commands from the file
        with open('commands.json', 'r') as f:
            self.commands = json.load(f)
        # Display commands keys in listbox
        for command in self.commands:
            self.commands_listbox.insert(tk.END, command)

    def delete_command(self):
        # Get selected command
        try:
            command_index = int(self.commands_listbox.curselection()[0])
            command_key = self.commands_listbox.get(command_index)
            # Remove command from dictionary and update file
            if command_key in self.commands:
                del self.commands[command_key]
                with open('commands.json', 'w') as f:
                    json.dump(self.commands, f, indent=4)
                # Remove from listbox
                self.commands_listbox.delete(command_index)
        except IndexError:
            messagebox.showerror("Selection Error", "No command selected")

    def add_command(self):
        command_name = self.new_command_name_entry.get()
        index_path = self.display_selected_index.get()
        weight_path = self.display_selected_pth.get()
        weight_path = self.display_selected_pth.get()
        pitch = self.pitch_value.get()
        if command_name and index_path and weight_path:
            # Add to commands dictionary
            self.commands[command_name] = {
                "index": index_path,
                "weight": weight_path,
                "pitch": pitch
            }
            # Update JSON file
            with open('commands.json', 'w') as f:
                json.dump(self.commands, f, indent=4)
            # Add to listbox
            self.commands_listbox.insert(tk.END, command_name)
            # Clear input field
            self.new_command_name_entry.delete(0, tk.END)
        else:
            messagebox.showerror(
                "Input Error", "Please fill all fields correctly")


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
        for file_name in self.file_dict['weights']:
            self.listbox_pth.insert(tk.END, file_name)

        self.file_dict['logs'] = self.list_files('logs', '.index')
        for file_name in self.file_dict['logs']:
            self.listbox_index.insert(tk.END, file_name)

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
           \"pitch\": \"-3\"
        }
}""")
        else:
            with open(commands_file_path, 'r') as f:
                commands = json.load(f)
                # Process commands and map them to the files loaded in file_dict
                for command, paths in commands.items():
                    if command == "SAMPLE_COMMANDS":
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
    root = tk.Tk()
    sv_ttk.set_theme("dark")
    app = FileViewer(root)
    root.mainloop()
