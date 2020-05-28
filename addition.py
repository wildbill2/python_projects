print("Provide two numbers and I will add them together.")
print("To exit the program enter 'q'.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("One of the values was not a valid number.  Please only enter number values.")
    else:
        print(answer)


