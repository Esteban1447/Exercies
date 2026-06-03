import random as rm

rango = 0

print("Bienvenido al juego de adivinar el número")
while True:
    print("¿En qué rango quieres jugar? (1-100, 1-1000, etc.)")
    try:
        rango = int(input("Ingresa el límite superior del rango: "))
        if rango <= 0:
            print("Por favor, ingresa un número válido mayor que 0")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido")


print("Estoy pensando en un número entre 1 y", rango)

while True:
    num = rm.randint(1, rango)
    intentos = 0
    while True:

        try:
            guess = int(input("¿Qué número crees que es? "))
            if guess < 1 or guess > rango:
                print("Por favor, ingresa un número entre 1 y", rango)
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



