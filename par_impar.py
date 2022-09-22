import random

def play():
    options = ["par", "impar"]
    user_score = 0
    computer_score = 0
    winner = ""

    while True:
        print(f"user: {user_score} | computer: {computer_score}")
        print('- '*15)
        user_mode = input("Par ou ímpar: ").lower()

        if user_mode not in options:
            print("Escolha inválida!\n")
            continue

        user_pick = input("Seu número: ")

        try:
            user_pick = int(user_pick)
        except ValueError:
            print("Número inválido!\n")
            continue

        if user_pick > 10 or user_pick < 0:
            print("Número inválido!\n")
            continue

        computer_pick = random.randint(0, 10)

        result = (user_pick + computer_pick) % 2

        if user_mode == "impar":
            if result == 1:
                user_score += 1
                winner = "Você"
            else:
                computer_score += 1
                winner = "Computador"
        else:
            if result == 0:
                user_score += 1
                winner = "Você"
            else:
                computer_score += 1
                winner = "Computador"

        print(f"Computador: {computer_pick}")
        print(f"\033[35m{winner} venceu!\033[m\n")

play()