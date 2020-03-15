from commands.CommonCommand import CommonCommand
from commands.parser import Parser
from entities.Points import Points
from entities.Vectors import Vectors

def print_help() -> None:
    print('введите выражение для вычислени\n')


class algebra(CommonCommand):

    def __init__(self, menu_point, v: Vectors, p: Points) -> None:
        super().__init__(menu_point, 'алгебра')
        self.vector = v
        self.points = p
        self.parser = Parser(v, p)

    def run(self):
        print_help()
        while True:
            s = input()
            try:
                print(self.parser.apply(s))
            except Exception as e:
                message = e.args[0]
                print('ERROR: ' + message)


