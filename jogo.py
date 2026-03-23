import random
numero_secreto= random.randint(1,10)

while True:
    palpite= int(input("tente adivinhar o número (1 a 10):"))

    if palpite== numero_secreto:
        print("acertou!!")
        break
    elif palpite < numero_secreto:
        print("tente um número MAIOR")
    else:
     print("tente um numero MENOR")
