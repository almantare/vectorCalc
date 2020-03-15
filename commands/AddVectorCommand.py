from commands.CommonCommand import CommonCommand
from entities.Vectors import Vectors


class AddVectorCommand(CommonCommand):

    def __init__(self, menu_point, v: Vectors) -> None:
        super().__init__(menu_point, 'Добавить вектор')
        self.vector = v

    def run(self):
        print("Enter vector(name(min len = 1), x, y, z)")
        self.vector.add_vector()
