import json
from util import write_file
from util import read_file
from util import display_all_contact
from util import display_contact_by_name
from util import add_contact
from util import delete_contact
from util import update_contact


phone_data = read_file(file_name='phone_num.json')
write_file(file_name='phone_num.json', data=phone_data)


print("Hello!")

# Loop is used in order for the program to not close, unless the user wants to
while True:
    print("What would you like to do: ")
    choice_lst = ["1. Dispaly all contacts",
                  "2. Dispaly contact by name",
                  "3. Update existing contact",
                  "4. Add contact",
                  "5. Del contact ",
                  "6. Exit application"]

    # Loops through the option and prints them in line
    for ind, val in enumerate(choice_lst):
        print(val)
    number_choice = int(input("Please enter a number for what you would like to do: "))
    print("\n")

    # Dispaly all contacts
    if number_choice == 1:
        display_all_contact(phone_data)

        # Asks the user if he would like to continue using the app
        inp_do_something_else = input("Would you like to do something else: yes/no: ").lower()
        print("\n")

        # If the user says "no" the app closes automatically
        if inp_do_something_else == "no":
            break
        # Checks whether the input is in the desired value "Yes / No", if not then closes automatically
        elif inp_do_something_else != "yes" and inp_do_something_else != "no":
            print("Invalid input. App will close automatically.")
            break

    # Dispaly contact by name
    elif number_choice == 2:
        contact_to_display = input("Enter the name of the contact you would like to display: ")
        display_contact_by_name(contact_to_display, phone_data)

        # Asks the user if he would like to continue using the app
        inp_do_something_else = input("Would you like to do something else: yes/no: ").lower()
        print("\n")

        # If the user says "no" the app closes automatically
        if inp_do_something_else == "no":
            break
        # Checks whether the input is in the desired value "Yes / No", if not then closes automatically
        elif inp_do_something_else != "yes" and inp_do_something_else != "no":
            print("Invalid input. App will close automatically.")
            break

    # Update existing contact
    elif number_choice == 3:
        contact_to_update = input("Enter the name of the contact you would like to edit: ").lower()
        number_or_name = input("Would you like to change the number or the name: ").lower()
        update_contact(contact_to_update, phone_data, number_or_name)

        # Asks the user if he would like to continue using the app
        inp_do_something_else = input("Would you like to do something else: yes/no: ").lower()
        print("\n")

        # If the user says "no" the app closes automatically
        if inp_do_something_else == "no":
            break
        # Checks whether the input is in the desired value "Yes / No", if not then closes automatically
        elif inp_do_something_else != "yes" and inp_do_something_else != "no":
            print("Invalid input. App will close automatically.")
            break

    # Add contact
    elif number_choice == 4:
        name_to_add = input("Enter a name: ").lower()
        number_to_add = int(input("Enter a number: "))
        add_contact(name_to_add, number_to_add, phone_data)

        # Asks the user if he would like to continue using the app
        inp_do_something_else = input("Would you like to do something else: yes/no: ").lower()
        print("\n")

        # If the user says "no" the app closes automatically
        if inp_do_something_else == "no":
            break
        # Checks whether the input is in the desired value "Yes / No", if not then closes automatically
        elif inp_do_something_else != "yes" and inp_do_something_else != "no":
            print("Invalid input. App will close automatically.")
            break

    # Del contact
    elif number_choice == 5:
        name_to_delete = input("Enter the name you want to delete: ")
        phone_data = delete_contact(name_to_delete, phone_data)
        write_file(file_name='phone_num.json', data=phone_data)

        # Asks the user if he would like to continue using the app
        inp_do_something_else = input("Would you like to do something else: yes/no: ").lower()
        print("\n")

        # If the user says "no" the app closes automatically
        if inp_do_something_else == "no":
            break
        # Checks whether the input is in the desired value "Yes / No", if not then closes automatically
        elif inp_do_something_else != "yes" and inp_do_something_else != "no":
            print("Invalid input. App will close automatically.")
            break

    # Exit application
    elif number_choice == 6:
        break

    # If the chosen input from the user is invalid, it asks the user if he would like to try again
    else:
        try_again = input("Invalid choice, would you like to try again: yes/no ").lower()
        if try_again == "no":
            break
