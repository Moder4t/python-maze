from typing import List


class Coordinates:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def pointer_equality(self, other) -> bool:
        return id(self) == id(other)

    def coord_equality(self, other) -> bool:
        return isinstance(other, Coordinates) and self.x == other.x and self.y == other.y


class TestEquality:
    def test_state_equality(self):
        state = Coordinates(0, 0)
        states: List[Coordinates] = [Coordinates(0, 0)]
        Coordinates.__eq__ = Coordinates.pointer_equality
        assert state not in states
        Coordinates.__eq__ = Coordinates.coord_equality
        assert state in states
