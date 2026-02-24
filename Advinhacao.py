import random
print('*****************************')
print('***Jogo advinhação***********')
print('*****************************')

numero_secreto = random.randrange(1,51)
total_tentativas = 15
rodada = 1

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada,total_tentativas))

    chute_str = input("Digite o seu numero: ")
    print("Seu numero é ", chute_str)
    chute = int(chute_str)

    if(chute<1 or chute > 50):
       print("Você deve digitar entre um número 1 e 50! ")
       continue
     
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você Acertou!! ")
        break
    else:
        if(maior):
          print("O seu chute foi maior que o número_secreto")
        elif(menor):
          print("O seu chute foi menor que o número_secreto")

print("Fim de jogo!")

