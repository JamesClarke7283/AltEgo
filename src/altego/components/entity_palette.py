import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from altego.backend.entities import ENTITIES  # Import the ENTITIES list

class EntityPaletteItem(toga.Box):
    def __init__(self, entity):
        super().__init__(style=Pack(direction=ROW, padding=5))
        self.icon = toga.Image(entity.icon_path)
        self.icon_view = toga.ImageView(self.icon, style=Pack(width=20, height=20))
        self.label = toga.Label(entity.name, style=Pack(padding_left=5))
        self.add(self.icon_view)
        self.add(self.label)

class EntityPalette(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN, background_color="#2b2b2b", width=250))
        self.create_content()

    def create_content(self):
        entity_palette_label = toga.Label("Entity Palette", style=Pack(padding=5, color="white"))
        entity_scroll = toga.ScrollContainer(style=Pack(flex=1))
        entity_box = toga.Box(style=Pack(direction=COLUMN))

        for entity in ENTITIES:
            entity_box.add(EntityPaletteItem(entity))

        entity_scroll.content = entity_box
        self.add(entity_palette_label, entity_scroll)
