from typing import Any, Dict

from pyxi.layer import Layer


class Canvas:
    __slots__ = ('width', 'height', 'tile_width', 'tile_height', 'layer_count', 'layers')

    def __init__(self, data: Dict[str, Any]):
        self.width = data['width']
        self.height = data['height']
        self.tile_width = data['tileWidth']
        self.tile_height = data['tileHeight']

        # Layers
        self.layer_count = data['numLayers']
        self.layers = {n: Layer(n, data['layers'][str(n)]) for n in range(self.layer_count)}
