import os

palavra_secreta = input("Insira a palavra secreta: ")
palavra_secreta_c = ""

chances = 3
dica = input("Dica (deixe em branco caso não queira deixar uma dica): ")
jogando = True
letras_usadas = ""

for cont in range(len(palavra_secreta)):
    palavra_secreta_c += "-"

while(jogando):
    os.system("cls")

    print("<-- QUAL A PALAVRA? -->\n")
    print(f"Palavra: {palavra_secreta_c}")
    print(f"Letras digitadas: {letras_usadas}")

    print(f"Nº de chances: {chances}")
    print(f"Dica: {dica}")
    letra = input("\nEu escolho a letra: ")
    letra_usada = letras_usadas.__contains__(letra)

    while (letra_usada):
        letra = input("Você ja tentou está letra, tente outra: ")
        letra_usada = letras_usadas.__contains__(letra)

    index = 0
    letras_usadas += f"{letra} "

    acertou = False
    for strg in palavra_secreta:
        if letra == strg:
            acertou = True
            palavra_secreta_c = list(palavra_secreta_c)
            palavra_secreta_c[index] = letra
            palavra_secreta_c_n = ""
            
            for strg in palavra_secreta_c:
                palavra_secreta_c_n += strg

            palavra_secreta_c = palavra_secreta_c_n
        index += 1
    if acertou:
        ganhou = not palavra_secreta_c.__contains__("-")
        if ganhou:
            print("\nVocê acertou a última letra e descobriu a palavra secreta!\n")
            print(f"Palavra secreta: {palavra_secreta}")
            jogando = False
        else:
            print("\nVocê acertou uma letra!\n")
    else:
        chances -= 1
        if chances > 0:
            print("\nErrou! Menos uma chance!")
        else:
            print("\nErrou! Suas chances acabaram...")
            jogando = False
    press = input("press enter...\n")

# Desenvolvido por Ernando
# Este código é o resultado de um resto de noite sem internet