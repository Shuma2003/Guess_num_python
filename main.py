import random
print("Программа загадала число от 1 до 10")
secret = random.randint(1,5)
hp = 100
while hp > 0:
    guess = int(input("Попробуйте угадать число"))
    if guess == secret:
        
       print("Число отгадано")
       break
    else:
        hp = hp - 10
        print(f"Не отгадал, Осталось HP: {hp} ")
        if hp <= 0:
            print(f"Загаданное число {secret}")
