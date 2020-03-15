from entities.pointAndVector import Vector


class Vectors:

    def __init__(self):
        self.all = {}

    def add_vector(self, v: Vector = None):
        if v is None:
            name, x, y, z = input().split()
            v = Vector(name, float(x), float(y), float(z))
        self.all[v.name] = v

    def show_all(self):
        if self.all == {}:
            print('список векторов пуст!')
        else:
            for v in self.all.values():
                print(v)

    def get_vector_by_name(self, name):
        try:
            return self.all[name]
        except KeyError:
            raise Exception("Can't find vector " + name + " in vector storage")

