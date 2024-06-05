class ConvertorMedidas:
    def __init__(self):
        pass

def centimetrosParaMetros(centimetros):
    metros = centimetros / 100
    return metros

valor_em_centimetros = 1000
valor_em_metros = centimetrosParaMetros(valor_em_centimetros)
print(f"{valor_em_centimetros} centímetros equivalem a {valor_em_metros:.2f} metros.")

def centimetrosParaMetros(metros):
    centimetros = metros * 100
    return centimetros

valor_em_metros = 100
valor_em_centimetros = centimetrosParaMetros(valor_em_metros)
print(f"{valor_em_metros} metros equivalem a {valor_em_centimetros:.2f} centimetros.")

