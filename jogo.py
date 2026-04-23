import random

nivel = 1

while True:
    print(f"\nNível {nivel}")
    limite = nivel * 10
    numero_secreto = random.randint(1, limite)
    tentativas = 5

    print(f"Tente adivinhar o número entre 1 e {limite}")
    print("Você tem até 5 tentativas")

    while tentativas > 0:
        palpite = int(input("Digite um número: "))

        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print("Acertou!! 🎉")
            nivel += 1
            break

        tentativas -= 1
        print(f"Você ainda tem: {tentativas}")

    if tentativas == 0:
        print("Você perdeu 😢")
        break