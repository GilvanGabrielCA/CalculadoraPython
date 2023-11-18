import Soma
import Subtracao
import Multiplicacao
import Divisao

def mensagemInicial():
    print("********************")
    print("*Calculadora Python*")
    print("********************")
def outraOperacao():
    repetir = input("Deseja continuar? [S/N]: ")
    repetir.upper()

    if repetir == "N":
        print("Saindo...")
    else:
        menu()
def menu():
    print("(1)Adição * (2) Multiplicação * (3) Subtração * (4) Disivão * (5) Sair")


mensagemInicial()
menu()

op = int(input("Escolha: "))

while 0 < op < 6:
    if op == 1:
        Soma.Somar()
    elif op == 2:
        Multiplicacao.Multiplicar()
    elif op == 3:
        Subtracao.Subtrair()
    elif op == 4:
        Divisao.Dividir()
    elif op == 5:
        print("Saindo...")
        break

    outraOperacao()
    op = int(input("Escolha: "))

