import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .components import EntityPalette, MainContent, RightSidebar

class AltEgo(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))
        content_box = toga.Box(style=Pack(direction=ROW, flex=1))

        left_sidebar = EntityPalette()
        main_content = MainContent()
        right_sidebar = RightSidebar()

        content_box.add(left_sidebar, main_content, right_sidebar)
        main_box.add(content_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return AltEgo('AltEgo', 'org.beeware.altego')

if __name__ == '__main__':
    main().main_loop()