# parte principal 
from modulo import *

# programa principal
if __name__ == "__main__":

    while True:
        nome = input("Qual o seu nome? ")
        mostrar_menu()
        opcao = input("Qual opcao deseja? ")

        match opcao:
            case "0":
                break
            case "1":
                base = int(input("Qual número representará sua base? "))
                expoente = int(input("Qual o número representará seu expoente? "))
                print(resultado_potencia(base, expoente))
                continue
            case "2":
                numero = float(input("Qual o número você quer calcular a raiz quadrada? "))
                print(resultado_raiz(numero))

            case _:
                print("Opção inválida")
                continue




