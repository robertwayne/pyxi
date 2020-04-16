from typing import Any, Dict


class Palette:
    __slots__ = ('width', 'height', 'color_count', 'colors')

    def __init__(self, data: Dict[str, Any]):
        self.width = data['width']
        self.height = data['height']
        self.color_count = data['numColors']
        self.colors = {k: v for k, v in data['colors'].items()}
