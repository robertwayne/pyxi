from typing import Any, Dict


class TileReference:
    __slots__ = ('reference_id', 'index', 'flipped', 'rot')

    def __init__(self, n: int, data: Dict[str, Any]):
        self.reference_id = n
        self.index = data['index']
        self.flipped = data['flipX']
        self.rot = data['rot']
