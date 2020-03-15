from commands.CommonCommand import CommonCommand
from entities.Vectors import Vectors


class ShowAllVectorsCommand(CommonCommand):
    def __init__(self, menu_point, vectors: Vectors) -> None:
        super().__init__(menu_point, 'Показать вектора')
        self.vectors = vectors

    def run(self):
        self.vectors.show_all()
