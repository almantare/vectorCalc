from entities.Points import Points
from entities.VectorAlgebra import scalar_product, vector_product, vector_angle
from entities.Vectors import Vectors
from entities.pointAndVector import Vector


class Parser:
    def __init__(self, v: Vectors, p: Points) -> None:
        self.vectors = v
        self.points = p

    def calc_scalar_product(self, a: Vector, b: Vector) -> float:
        return scalar_product(a, b)

    def calc_vector_product(self, a: Vector, b: Vector) -> str:
        return vector_product(a, b)

    def calc_vector_angle(self, a: Vector, b: Vector) -> str:
        return vector_angle(a, b)

    operations = {
        '*': calc_scalar_product,
        'x': calc_vector_product,
        '^': calc_vector_angle
    }

    def parse_str(self, x) -> Vector:
        if len(x) == 1:
            return self.vectors.get_vector_by_name(x)
        if len(x) == 2:
            return Vector.from_points(self.points.get_point_by_name(x[0]), self.points.get_point_by_name(x[1]))
        raise AttributeError('Got vector from more than two point: ' + x)

    def apply(self, s: str):
        x, op, y = s.split()
        v_x = self.parse_str(x)
        v_y = self.parse_str(x)
        return self.operations[op](self, v_x, v_y)
