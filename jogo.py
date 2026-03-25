import random
numero_secreto= random.randint(1,10)
tentativas = 5

print ("Bem vindos ao jogo de adivinhação!")
print ("Tente adivinhar o número entre 1 e 10")
print ("Você tem até 5 tentativas")

while tentativas > 0:
    chute = int(input("digite um número:"))

    if chute == numero_secreto:
        print("acertou!!")
        break 

    elif chute > numero_secreto:
        print("muito alto!")
    else:
     print("muito baixo!")

      
    tentativas -= 1
    print(f"você ainda tem:{tentativas}")

if tentativas == 0:
   print (f"você perdeu! o número era  {numero_secreto}")