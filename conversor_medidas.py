class ConvertorMedidas:
    def __init__(self):
        pass

def centimetrosParaMetros(centimetros):
    metros = centimetros / 100
    return metros

valor_em_centimetros = 1000
valor_em_metros = centimetrosParaMetros(valor_em_centimetros)
print(f"{valor_em_centimetros} centímetros equivalem a {valor_em_metros:.2f} metros.")
