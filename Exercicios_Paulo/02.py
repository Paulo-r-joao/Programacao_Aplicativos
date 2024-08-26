deslocamento = int(input("Digite o deslocamento: "))
texto = input("Digite o texto a ser criptografado: ")
texto_criptografado = ""
for letra in texto:
    if letra.isupper():
        letra_criptografada = chr((ord(letra.lower()) + deslocamento - 97) % 26 + 65)
    elif letra.islower():
        letra_criptografada = chr((ord(letra) + deslocamento - 97) % 26 + 97)
else: letra_criptografada = letra 
texto_criptografado += letra_criptografada
print("Texto criptografado:", texto_criptografado)