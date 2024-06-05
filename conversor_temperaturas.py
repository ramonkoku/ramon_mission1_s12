class conversorTemperaturas:
    def __init__(self):
        pass
    
def celsiusParaFahrenheit(celsius):
    Fahrenheit = (9/5*celsius)-32
    return Fahrenheit

valor_em_celsius = 32
valor_em_Fahrenheit = celsiusParaFahrenheit(valor_em_celsius)
print(f"{valor_em_celsius} celsius equivalem a {valor_em_Fahrenheit:.2f} Fahrenheit.")

def centimetrosParaFahrenheit(Fahrenheit):
    celsius = 5/9 *(Fahrenheit - 32)
    return celsius

valor_em_Fahrenheit = 57
valor_em_celsius = centimetrosParaFahrenheit(valor_em_Fahrenheit)
print(f"{valor_em_Fahrenheit} Fahrenheit equivalem a {valor_em_celsius:.2f} celsius.")

