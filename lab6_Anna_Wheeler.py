# Anna Wheeler menu function, encode function, and main function

# defines the menu to be printed and used later
def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

    menu_selection = int(input('Please enter an option: '))

    return menu_selection

# creates a function that encodes a user inputed password
def encode(user_input):
    # converts user password to list
    user_inputed_password = list(user_input)
    encoded_password_list = []

    # adds 3 to each digit in the password by iterating through the list
    for digit in user_inputed_password:
        encoded_digit = int(digit) + 3
        encoded_password_list.append(str(encoded_digit))

    # converts the encoded password list back to a sting
    global encoded_password
    encoded_password = ''.join(encoded_password_list)

    return encoded_password


#def decode(encoded_password):
    # to be written by partner

def main():
    global menu_selection
    menu_selection = 0

    # creates a loop that will reprint the menu until the user selects option 3. Quit
    while menu_selection != 3:

        menu_selection = menu()

        # calls encode function if option 1 is selected
        if menu_selection == 1:
            user_input = input('Please enter your password to encode: ')
            encoded_password = encode(user_input)
            print("Your password has been encoded and stored!")

        # calls decode function is option 3 is selected
        #elif menu_selection == 2:
            #decoded_password = decode(encoded_password)
            #print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')

if __name__ == '__main__':
    main()