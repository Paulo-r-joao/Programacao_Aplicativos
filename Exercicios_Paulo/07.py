def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
# Para definir maior ou menor
    for elemento in lista:
        if elemento > maior:
            maior = elemento
        elif elemento < menor:
            menor = elemento
        return maior, menor
lista=list()
i=1
while i<=10:
# Receber elemento da lista
 elem = int(input("Digite um elemento da lista:"))
 lista.append(elem)
 i+=1
 print(lista)
# Imprimir a lsita com o maior e menor
maior, menor = maior_menor(lista)
print("Maior:", maior)
print("Menor:", menor)