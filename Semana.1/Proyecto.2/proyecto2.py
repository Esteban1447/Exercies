import random as rm

print("Bienvenido al juego de adivinar el número")
print("Estoy pensando en un número entre 1 y 100")

while True:
    num = rm.randint(1, 100)
    intentos = 0
    while True:

        try:
            guess = int(input("¿Qué número crees que es? "))
            if guess < 1 or guess > 100:
                print("Por favor, ingresa un número entre 1 y 100")
                continue
            intentos += 1
            if guess < num:
                print("El número es mayor, try again")
            elif guess > num:
                print("El numero es menor, try again")
            else:
                print("¡Felicidades! Acertaste el número en", intentos, "intentos")
                break

            

        except ValueError:
            print("Por favor, ingresa un número válido")

    play_again = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
    if play_again != "s" and play_again != "si":
        print("Gracias por jugar. ¡Hasta luego!")
        break



