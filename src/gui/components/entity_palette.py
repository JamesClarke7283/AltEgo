import tkinter as tk
from tkinter import ttk

class EntityPalette(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=5)
        label = ttk.Label(self, text="Entity Palette", anchor="center")
        label.pack(fill=tk.X)

        # Placeholder for entity list
        entity_list = tk.Listbox(self)
        entities = ["Bitcoin Cash Address", "Bitcoin Cash Block", "Bitcoin Address", "Bitcoin Block"]
        for entity in entities:
            entity_list.insert(tk.END, entity)
        entity_list.pack(fill=tk.BOTH, expand=True)
