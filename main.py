#Contando o número de palavras:

frase = str(input("Digite uma frase: "))
numero_de_palavras = len(frase.split()) # Utilizo o metodo split() para dividir a frase em palavras. Utilizo len() para contar o número de palavras resultantes.
print(f"Número de palavras na frase: {numero_de_palavras}")

#Substituindo as vogais por asteriscos:

resultado = ""
for caractere in frase:
    if caractere.lower() in "aeiou":
        resultado += "*"
    else:
        resultado += caractere
print(f"Frase com vogais substituidas: {resultado}")

#Contar o número de letras da frase:

frase_sem_espaco = frase.replace(" ", "".lower())
numero_de_letras = len(frase_sem_espaco)
print(f"Número de letras na frase: {numero_de_letras}")

#Verificar se a frase é um palíndromo:

frase_sem_espaco = frase.replace(" ", "".lower())
if frase_sem_espaco == frase_sem_espaco[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")

fsp = frase.strip()
print(fsp)
