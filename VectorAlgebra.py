from entities.pointAndVector import Vector


def scalar_product(v1: Vector, v2: Vector) -> float:
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


def vector_product(v1: Vector, v2: Vector) -> str:
    return "({i}, {j}, {k})".format(i=str(v1.y * v2.z - v2.y * v1.z), j=str(v1.x * v2.z - v2.x * v1.z), k=str((v1.x * v2.y - v2.x * v1.y)))


def vector_angle(v1: Vector, v2: Vector) -> str:
    return "cos a = " + str(abs(scalar_product(v1, v2) / (v1.length() * v2.length())))



