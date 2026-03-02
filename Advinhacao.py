import random
#Cores no Terminal PY
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"

def escolher_nivel():
    print("n\Escolha o nível: ")
    print("1 -- Fácil (10t entativas)")
    print("1 -- Fácil (5 tentativas)")
    print("1 -- Difícil (3 tentativas)")

    while True:
        nivel_str = input("Digite apenas números (1, 2, 3): ")
        if not nivel_str.isdigit():
            print(VERMELHO+"Digite apenas números! "+ RESET)
            continue
        nivel_str = int(nivel_str)
        if nivel == 1:
            return  10
        elif nivel == 2:
            return 5
        elif nivel == 3:
            return 3
        else:
            print(AMARELO+"Escolha apenas 1, 2 ou 3 "+RESET)


def jogar():

    print(AZUL+'*****************************'+RESET)
    print(AZUL+'***Jogo advinhação***********'+RESET)
    print(AZUL+'*****************************'+RESET)
    total_tentativas = escolher_nivel()
    numero_secreto = random.randrange(1,51)
    pontos = 100
    historico = []



print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Escolha o nível: "))

if nivel == 1:
    total_tentativas = 1
elif nivel == 2:
    total_tentativas = 2
else:
    total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {rodada} de {total_tentativas}".format(rodada, total_tentativas))

    if not chute_str.isdigit():
        print(VERMELHO+ "Digite um número entre 1 e 100: "+RESET)
        continue

    chute = int(chute_str)

    if(chute < 1 or chute > 100):

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada,total_tentativas))

    chute_str = input("Digite o seu numero: ")
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

