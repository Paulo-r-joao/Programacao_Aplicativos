#Calculo para o mdc
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)
#Recebe os números
num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))
#Resultado do mdc
resultado = mdc(num1, num2)
print("MDC:", resultado)