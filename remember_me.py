import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
    return username    


def greet_user():
    """Greet the user by name."""
    """If not current user prompt for a new username."""
    username = get_stored_username()
    if username:
        message = input("Are you " + username + "? (y or n) ")
        if message == 'n':
            username = get_new_username()
        else:
            print("Welcome back, " + username + "!")
    else:
        get_new_username()


greet_user()