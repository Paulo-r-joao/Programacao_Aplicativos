def converter_quilometros_para_metros(quilometros):
    metros = quilometros * 1000
    return metros
try:
quilometros = float(input(“Digite a distância em quilômetros: “))
metros = converter_quilometros_para_metros(quilometros)
print(“metros:”, metros)
except ValueError:
print(“Entrada inválida!”)