from conversor_temperaturas import ConversorTemperaturas
from conversor_medidas import ConvertorMedidas


print("1. Centímetros a Metros")
print("2. Metros a centímetros")
print("3. Celsius para Fahrenheit")
print("4. Fahrenheit para Celsius")
print("5. sair ") 

escolha = input("Escolha uma opção: ")

valor = float(input('Digite um valor: '))

if escolha == '1':
    result = ConvertorMedidas.centimetros_para_metros(valor)
elif escolha == '2':
    result = ConvertorMedidas.metros_para_centimetros(valor)
elif escolha == '3':
    result = ConversorTemperaturas.celsius_para_fahrenheit(valor)
elif escolha == '4':
    result = ConversorTemperaturas.fahrenheit_para_celsius(valor)
else:
    print("Encerrando o programa...")
    
print("Resultado:", result)
