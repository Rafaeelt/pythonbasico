print('*****************************')
print('***Jogo advinhação***********')
print('*****************************')

numero_secreto = 39

chute_str = input("Digite o seu numero: ")

print("Seu numero é ", chute_str)

churte = int(chute_str)

if(numero_secreto == chute_str):
    print("Você Acertou!! ")
else:
    print("Você errou    :(")
