# Id: FMS/0002/19

contact_list = []  # A list containing all lists of contacts
lines = []  # A list contain all lines in contacts.txt


def main_menu():
    print("CONTACTS BOOK")
    while True:
        option = input("1. Create a Contact\n2. Update an Existing Contact\n3. Browse Contacts\n4. Delete a Contact "
                       "\n5. Delete All Contacts \n6. Exit\n")
        if option == '1':
            create_contact()
        elif option == '2':
            update_contact()
        elif option == '3':
            browse_contacts()
        elif option == '4':
            delete_contact()
        elif option == '5':
            delete_contacts()
        elif option == '6':
            exit()
        else:
            print('Invalid input. Please try again....')


def create_contact():
    while True:
        first_name = input("Enter First Name: ").lower()
        last_name = input("Enter Last Name: ").lower()
        tel = input("Enter Telephone Number: ")
        email = input("Enter Email: ").lower()
        print("\nFirst Name: ", first_name.capitalize())
        print("Last Name: ", last_name.capitalize())
        print("Telephone Number: ", tel)
        print("Email: ", email)
        option = input("1. Save Contact\n2. Reenter info\n3. Cancel\n")

        if option == '1':
            with open('contacts.txt', 'a+') as file_object:
                file_object.seek(0)
                data = file_object.read()  # to check if file is empty
                if len(data) > 0:
                    file_object.write('\n')  # append a new line before writing to file if not empty
                file_object.write(first_name)
                file_object.write('\n')
                file_object.write(last_name)
                file_object.write('\n')
                file_object.write(tel)
                file_object.write('\n')
                file_object.write(email)
                file_object.write('\n')
                file_object.write('-')  # This is to separate the different contacts stored in the file.
            print('Contact has been saved successfully.')
            break
        elif option == '3':
            break


def browse_contacts():
    get_contacts()
    if len(contact_list) != 0:
        print('\tAll Contacts')
        for contact in contact_list:
            print('First Name: ' + contact[0].capitalize(), end='')
            print('Last Name: ' + contact[1].capitalize(), end='')
            print('Telephone Number: ' + contact[2], end='')
            print('Email: ' + contact[3], end='')
            print('\t-------\t')
    else:
        print('You have no contacts yet.')


def get_contacts():
    contact_list.clear()
    with open('contacts.txt', 'r') as reader:
        contact_lines = []
        reader.seek(0)
        for line in reader.readlines():
            if line == '-\n' or line == '-':
                contact_list.append(contact_lines[:])
                contact_lines.clear()
            else:
                contact_lines.append(line)


def get_specific_contact():
    global lines
    index = -1
    option = input('Enter the first name of contact: \n').lower()
    with open('contacts.txt', 'r') as reader:
        lines = reader.readlines()

    try:
        index = lines.index(option + '\n')
    except ValueError:
        print('Sorry. Contact not found')
        return index
    if not index % 5 or index == 0:
        return index
    else:
        print('Sorry. Contact not found')
        return -1


def update_contact():
    index = get_specific_contact()
    if index != -1:
        while True:
            print('Click Enter if you do not want to change a particular field.')
            first_name = input("Enter New First Name: ").lower()
            last_name = input("Enter New Last Name: ").lower()
            tel = input("Enter New Telephone Number: ")
            email = input("Enter New Email: ").lower()
            if len(first_name) == 0:
                first_name = lines[index]
            else:
                first_name = first_name + '\n'
            if len(last_name) == 0:
                last_name = lines[index + 1]
            else:
                last_name = last_name + '\n'
            if len(tel) == 0:
                tel = lines[index + 2]
            else:
                tel = tel + '\n'
            if len(email) == 0:
                email = lines[index + 3]
            else:
                email = email + '\n'
            print("\nFirst Name: ", first_name.capitalize(), end='')
            print("Last Name: ", last_name.capitalize(), end='')
            print("Telephone Number: ", tel, end='')
            print("Email: ", email, end='')
            option = input("1. Save Contact\n2. Reenter info\n3. Cancel\n")

            if option == '1':
                lines[index] = first_name
                lines[index + 1] = last_name
                lines[index + 2] = tel
                lines[index + 3] = email
                with open('contacts.txt', 'w') as file_object:
                    file_object.writelines(lines)
                    print('Contact has been edited successfully.')
                break
            elif option == '3':
                break


def delete_contact():
    index = get_specific_contact()
    if index != -1:
        lines.pop(index)
        lines.pop(index)
        lines.pop(index)
        lines.pop(index)
        lines.pop(index)
        with open('contacts.txt', 'w') as writer:
            writer.writelines(lines)
        print('Contact has been deleted successfully')


def delete_contacts():
    option = input('Are you sure you want to delete all your contacts? You wont be able to restore them again'
                   '. [Y/N]: ').lower()

    if option == 'y':
        with open('contacts.txt', 'w') as writer:
            writer.write('')
        print('All your contacts have been deleted successfully.')


main_menu()
