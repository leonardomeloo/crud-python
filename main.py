import controllers.ClienteController as ClienteController
import models.Cliente as cliente
from models.menu import menu

op = menu()

if op == 1:
    cliente.fullname = input("Fullname: ")
    cliente.age = input("Age: ")
    cliente.profession = input("Profession: ")
    cliente.email = input("E-mail: ")

    ClienteController.Creat(cliente)

elif op == 2:
    print(ClienteController.Read())

elif op == 3:
    print('O que deseja atualizar:\nA - Nome\nB - idade\nC - Profissão\nD - E-mail')
    apply = input("->").upper()

    ClienteController.Update(apply)