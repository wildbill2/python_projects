# List of current users
current_users = ['brian', 'angela', 'olivia', 'steve', 'michael']
# List of new users
new_users = ['Brian', 'Mario', 'Luigi', 'Michael', 'Carly']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user.title() + " needs to choose a different username.")
    else:
        print(new_user.title() + " is available!")

        
        
