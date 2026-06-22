def sum_list(*numbers):
    total = 0
    for n in numbers:
        total += n
    
    return total

def subtract_list(*numbers):
    if not numbers:
        return 0
    total = numbers[0]
    for n in numbers[1:]:
        total -= n
    return total

def multiply_list(*numbers):
    if not numbers:
        return 0
    total = numbers[0]
    for n in numbers[1:]:
        total *= n
    return total

def divide_list(*numbers):
    if not numbers:
        return 0
    total = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            print("Error: división por cero.")
            return None
        total /= n
    return total

def main():
    numbers = []

    print("Ingrese los números (Enter vacío para terminar)")
    while True:
        enter = input("Número: ")
        if enter == "":
            break
        numbers.append(float(enter))

    if not numbers:
        print("No ingresaste números.")
        return

    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    option = input("Seleccione una operación: ")

    if option == "1":
        print(f"Resultado: {sum_list(*numbers)}")
    elif option == "2":
        print(f"Resultado: {subtract_list(*numbers)}")
    elif option == "3":
        print(f"Resultado: {multiply_list(*numbers)}")
    elif option == "4":
        result = divide_list(*numbers)
        if result is not None:
            print(f"Resultado: {result}")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()



