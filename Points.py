from entities.pointAndVector import Point


class Points:

    def __init__(self):
        self.all = {}

    def add_point(self, p: Point = None):
        if p is None:
            name, x, y, z = input().split()
            p = Point(name, float(x), float(y), float(z))
        self.all[p.name] = p

    def show_all(self):
        if self.all == {}:
            print('список точек пуст!')
        else:
            for p in self.all.values():
                print(p)

    def get_point_by_name(self, name):
        try:
            return self.all[name]
        except KeyError:
            raise Exception("Can't find point " + name + " in point storage")

