expences = []
expence=0
concept = ""
amount = 0
total = 0
option = 0
index = 0
highest_expence = 0

def add_expence():
    global expences, concept, amount, total, highest_expence
    concept = input("Ingrese el concepto del gasto: ")
    amount = float(input("ingrese el monto del gasto: "))
    expences.append((concept, amount))
    total += amount
    if amount > highest_expence:
        highest_expence = amount
    print("Gasto agregado exitosamente.")

def view_expences():
    global expences, total, highest_expence
    if not expences:
        print("No hay gastos registrados.")
    else:
        print("Gastos registrados:")
        for concept, amount in expences:
            print(f"{concept}: ${amount:.2f}")
        print(f"total de gastos: ${total:.2f}")
        print(f"Gasto más alto: ${highest_expence:.2f}")

def view_total():
    global total, highest_expence
    print(f"Total de gastos: ${total:.2f}")
    print(f"Gasto más alto: ${highest_expence:.2f}")


def main():
    while True:
        print("1. Agregar gasto")
        print("2. Ver gastos")
        print("3. Ver total de gastos")
        print("4. Salir")
        option = int(input("Seleccione una opción:"))
        if option == 1:
            add_expence()
        elif option == 2:
            view_expences()
        elif option == 3:
            view_total()
        elif option == 4:
            print("Gracias por usar el gestor de gastos. ¡Hasta luego!")
            break
        else:
            print("Opción no valida. Por favor, selecione una opción válida.")


if __name__ == "__main__":
    main()

