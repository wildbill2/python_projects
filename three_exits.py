prompt = "What would you like on your pizza?:"
prompt += "\nEnter toppings here:"

active = True

while active:
    toppings = []
    topping = input(prompt)
    toppings.append(topping)

    if topping == 'quit':
        active = False
    elif len(toppings) > 3:
        active = False
    else:
        print("\nI will put " + topping + " on your pizza.")

    