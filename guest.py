filename = 'text_files/guest.txt'


while True:
    print("Please enter your name for the guest book.")
    print("To quit please enter 'q' at any time.")

    guest = input("Guest Name: ")
    if guest == 'q':
        break


    with open(filename, 'a') as guest_book:
        guest_book.write(guest.title() + "\n")





