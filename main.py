from commands.AddPointCommand import AddPointCommand
from commands.ShowAllPointCommand import ShowAllPointCommand
from commands.ShowAllVectorsCommand import ShowAllVectorsCommand
from commands.menu import Menu
from entities.Points import Points
from entities.Vectors import Vectors
from commands.AddVectorCommand import AddVectorCommand
from commands.V_Algebra import algebra

menu = Menu()
point_storage = Points()
vector = Vectors()
menu.add_command(AddPointCommand('2', point_storage))
menu.add_command(ShowAllPointCommand('3', point_storage))
menu.add_command(AddVectorCommand('4', vector))
menu.add_command(ShowAllVectorsCommand('5', vector))
menu.add_command(algebra('6', vector, point_storage))


menu.print_menu_points()
while True:
    choice = input("select option: ")
    if choice == '1':
        menu.print_menu_points()
    else:
        menu.run_command(choice)
