def sum_list(*numbers):
    total = 0
    for n in numbers:
        total += n
    
    return total

def main():
    numbers = input("Ingrese los numeros separados por comas: ")

    while True:
        enter: input("Number: ")
        if enter == "":
            break
        numbers.append(float(enter))
    
    if numbers:
        print(f"Result: {sum_list(numbers)}")
    else:
        print("No numbers entered.")

if __name__ == "__main__":
    main()



