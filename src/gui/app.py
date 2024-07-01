import tkinter as tk
from tkinter import ttk
from .components.menu import Menu
from .components.entity_palette import EntityPalette
from .components.graph_area import GraphArea
from .components.overview import Overview
from .components.detail_view import DetailView
from .components.property_view import PropertyView
from .components.run_view import RunView

def main():
    root = tk.Tk()
    root.title("AltEgo")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    menu_bar = Menu(root)

    main_paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
    main_paned_window.pack(fill=tk.BOTH, expand=True)

    left_paned_window = ttk.PanedWindow(main_paned_window, orient=tk.VERTICAL)
    main_paned_window.add(left_paned_window, weight=1)

    entity_palette_frame = EntityPalette(left_paned_window)
    run_view_frame = RunView(left_paned_window)

    left_paned_window.add(entity_palette_frame, weight=3)
    left_paned_window.add(run_view_frame, weight=1)

    center_frame = GraphArea(main_paned_window)
    main_paned_window.add(center_frame, weight=3)

    right_paned_window = ttk.PanedWindow(main_paned_window, orient=tk.VERTICAL)
    main_paned_window.add(right_paned_window, weight=1)

    overview_frame = Overview(right_paned_window)
    detail_view_frame = DetailView(right_paned_window)
    property_view_frame = PropertyView(right_paned_window)

    right_paned_window.add(overview_frame, weight=1)
    right_paned_window.add(detail_view_frame, weight=1)
    right_paned_window.add(property_view_frame, weight=1)

    root.update_idletasks()
    main_paned_window.sashpos(0, 300)
    main_paned_window.sashpos(1, root.winfo_screenwidth() - 600)

    root.mainloop()

if __name__ == "__main__":
    main()
