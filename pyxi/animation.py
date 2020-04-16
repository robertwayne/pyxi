from typing import Any, Dict


class Animation:
    __slots__ = ('frame_id', 'name', 'length', 'base_tile', 'duration_multipliers', 'frame_duration')

    def __init__(self, n: int, data: Dict[str, Any]):
        self.frame_id = n
        self.name = data['name']
        self.length = data['length']
        self.base_tile = data['baseTile']
        self.duration_multipliers = data['frameDurationMultipliers']
        self.frame_duration = data['frameDuration']
