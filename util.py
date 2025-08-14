import json

# Function: that writes the file
def write_file(file_name, data):
    with open(file_name, 'w') as file:
        string = json.dumps(data)
        file.write(string)

# Function: reads the file
def read_file(file_name):
    with open(file_name, 'r') as file:
        str_data = file.read()
        lst_data = json.loads(str_data)
        return lst_data

# Function: displays all contacts
def display_all_contact(phone_data):
    # Runs through the whole phone_data and prints every available contact
    for ind, val in enumerate(phone_data):
        print(val)

# Function: displays a contact by name from the input of the user
def display_contact_by_name(contact_to_display, phone_data):
    found = False
    found_contact = ""

    # Looks for the contact in the phone_data
    for ind, contact in enumerate(phone_data):
        if contact["name"] == contact_to_display:
            found = True
            found_contact = contact
            break

    # If found returns the contact. else returns "name not found"
    if found == True:
        print(found_contact)
    else:
        print("Name not found.")

# Function: adds a contact
def add_contact(name_to_add, number_to_add, phone_data):
    phone_data.append({"name": name_to_add, "num": number_to_add})
    print(f"Added new contact: {name_to_add}, with number: {number_to_add}")

    write_file(file_name='phone_num.json', data=phone_data)

# Function: deletes a contact
def delete_contact(name_to_delete, phone_data):

    # Creates a new list
    new_phone_data = []
    found = False

    # Searches for the "name" provided by the user, if it is not the name provided by the user it adds it to the new_phone_data
    for contact in phone_data:
        if contact["name"] != name_to_delete:
            new_phone_data.append(contact)
        else:
            found = True
            print(f"Contact deleted: {name_to_delete}")

    if found == False:
        print("Name not found.")

    # Returns the updated data with the removed "name"
    return new_phone_data

# Function: updates a contact
def update_contact(contact_to_update, phone_data, number_or_name):

    # Loops through each contact in the phone book
    for ind, contact in enumerate(phone_data):

        # Checks if the current contact's name matches the one the user wants to update
        if contact["name"].lower() == contact_to_update:

            # Checks if the user chose to edit the "name"
            if number_or_name == "name":
                name_to_edit = input("Please enter a new name: ")
                contact["name"] = name_to_edit
                print(f"New name: {name_to_edit} successfully edited")

            # Checks if the user chose to edit the "number"
            elif number_or_name == "number":
                number_to_edit = input("Please enter a new number: ")
                contact["num"] = number_to_edit
                print(f"New number: {number_to_edit} successfully edited")

            # If the option is neither "name" nor "number"
            else:
                print("Invalid number or name")
            break
        else:
            print("Name not found.")

    write_file(file_name='phone_num.json', data=phone_data)

