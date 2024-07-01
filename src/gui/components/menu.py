import tkinter as tk

class Menu(tk.Menu):
    def __init__(self, root):
        super().__init__(root)
        root.config(menu=self)

        file_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Exit", command=root.quit)

        edit_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")

        view_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Zoom In")
        view_menu.add_command(label="Zoom Out")
