import tkinter as tk
from tkinter import ttk

class Overview(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=5)
        label = ttk.Label(self, text="Overview", anchor="center")
        label.pack(fill=tk.X)

        # Placeholder for overview content
        text = tk.Text(self, height=5)
        text.pack(fill=tk.BOTH, expand=True)
