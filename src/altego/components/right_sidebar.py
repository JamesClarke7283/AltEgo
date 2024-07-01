import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class RightSidebar(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN, background_color="#2b2b2b", width=300))
        self.create_content()

    def create_content(self):
        self.add(self.create_view_box("Overview"))
        self.add(self.create_view_box("Detail View"))
        self.add(self.create_view_box("Property View"))

    def create_view_box(self, title):
        box = toga.Box(style=Pack(direction=COLUMN, padding=5, flex=1))
        label = toga.Label(title, style=Pack(padding=5, color="white"))
        content = toga.Box(style=Pack(background_color="white", flex=1))
        box.add(label, content)
        return box