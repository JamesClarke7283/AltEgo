import toga
from toga.style import Pack

class MainContent(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(flex=1, background_color="white"))
        self.create_content()

    def create_content(self):
        # Add your main content here
        pass