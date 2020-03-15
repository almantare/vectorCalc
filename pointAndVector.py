import math


class Point:

    def __init__(self, name: str, x: float, y: float, z: float):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return self.name + "(" + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ")"


class Vector:

    def __init__(self, name: str, x: float, y: float, z: float):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def from_points(p1: Point, p2: Point):
        return Vector(
            p1.name + p2.name,
            p2.x - p1.x,
            p2.y - p1.y,
            p2.z - p1.z,
        )

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __repr__(self) -> str:
        return self.name + "(" + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ")"



