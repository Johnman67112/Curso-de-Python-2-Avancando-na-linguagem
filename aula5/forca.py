def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "pokemon".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Essa letra não está na palavra, faltam {} tentativa(s).".format(6 - erros))
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if(acertou):
        print("Você acertou, parabéns!")
    else:
        print("Você errou, que pena!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
