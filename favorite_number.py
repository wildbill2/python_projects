# Module imports
import json



def check_for_number():
    """Checks if a favorite number is already stored."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number


def get_number():
    """Get favorite number if it does not exist."""
    number = check_for_number()
    if number:
        print("I know your favorite number! It's " + number + ".")
    else:
        number = input("What is your favorite number? ")
        filename = 'favorite_number.json'
        with open(filename, 'w') as f_obj:
            json.dump(number, f_obj)


get_number()



