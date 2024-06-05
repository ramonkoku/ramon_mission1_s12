from conversor_medidas import ConvertorMedidas


def menu_principal():
    print("\n**calculadora de conversão de unidades**")
    print("1. converter comprimento")
    print("3. sair")

    opcao=input("digite A opição desejada: ")
    return opcao

def sair():
    print("encerrando o progama...")

escolha =menu_principal()

if escolha =='3':
    sair()
