import tkinter as tk
from tkinter import ttk, filedialog
import requests
import os

class downloder:
    def __init__(self):
        self.saveto = ""
        self.window = tk.Tk() 
        self.window.title("Fast Downloader")
        self.url_label = tk.Label(text = " Enter URL to download")
        self.url_label.pack()
        self.url_entry = tk.Entry()
        self.url_entry.pack()
        self.brows_button = tk.Button(text="Browse", command= self.browse_file)
        self.brows_button.pack()
        self.download_button = tk.Button(text="Download", command= self.download)
        self.download_button.pack()
        self.window.geometry("800x350")
        self.progressbar = ttk.Progressbar(self.window, orient="horizontal", maximum=100, length=300 , mode="determinate")
        self.progressbar.pack()
        self.window.mainloop()
    def browse_file(self):
            filename = filedialog.asksaveasfilename(initialfile=self.url_entry.get().split("/")[-1])
            self.saveto = filename

    def download(self):
            url = self.url_entry.get()
            if url is None:
                  return
            response = requests.get(url, stream=True)
            if (response.headers.get("content-length")):
                total_size_in_bytes = int(response.headers.get("content-length"))
            print(total_size_in_bytes)
            block_size = 10000
            self.progressbar["value"] = 0
            fileName = self.url_entry.get().split("/")[-1]
            if self.saveto == "":
                  self.saveto = fileName
            with open (self.saveto, "wb") as f:
                  for data in response.iter_content(block_size):
                        f.write(data)
                        self.progressbar["value"] += (block_size / total_size_in_bytes) * 100 
                        self.window.update()





downloder()

# https://download-cdn.jetbrains.com/python/pycharm-professional-2024.2.3.exe