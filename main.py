def menu_principal():
    print("\n**calculadora de conversão de unidades**")
    print("1. converter de comprimento")
    print("2. converter de temperaturas")
    print("3. sair ")

    opcao=input("digite A opição desejada: ")
    return opcao
def sair():
    print("encerrando o progama...")


escolha =menu_principal()

if escolha =='3':
    sair()
elif escolha == '2':
    from conversor_temperaturas import conversorTemperaturas
elif escolha == '1' :
    from conversor_medidas import ConvertorMedidas
else :
    print("vai tomar no cu, é só seguir a regras")