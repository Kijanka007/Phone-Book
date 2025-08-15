# Phone Book Application

A simple **Phone Book application** written in Python.  
It allows you to **store, search, update, and delete contacts** that are saved in a JSON file so your data is persistent between sessions.

---

## About the project
This Phone Book app is a project to practice Python basics like file handling, JSON, and CRUD operations. 

--- 

## Features
- Display all contacts  
- Search contact by name  
- Update an existing contact (name or number)  
-  Add new contacts  
-  Delete contacts  
-  Persistent storage with JSON  

---

## Requirements

You need **Python 3.8+** installed.

Install dependencies with:

- ruff
```bash
  pip install -r requirements.
```
##  Project Structure

--- 

```text
phone-book
 ┣ main.py              # menu & program loop (user interaction)
 ┣ util.py              # Helper functions (read/write JSON + CRUD operations)
 ┣ phone_num.json       # Data store (list of {"name","num"})
 ┣ requirements.txt     # Dependencies: ruff
 ┗ README.md
```
---

## 🔑 Key Functions

### `write_file(file_name, data)`
- Saves the given `data` (list) into a JSON file.  
- Uses `json.dumps` to convert Python objects into JSON strings.

```python
write_file("phone_num.json", [{"name": "alice", "num": 123}])
```
---
### `read_file(file_name)`
- Reads a JSON file and returns it as a Python object (`list`/`dict`).  
- Used to load the contacts when the app starts.

```python
phone_data = read_file("phone_num.json")
```
---
### `display_all_contact(phone_data)`
- Prints all contacts in the phone book.  
- Loops through the list of contacts and shows each one.
---
### `display_contact_by_name(contact_to_display, phone_data)`
- Searches for a contact by name.  
- Prints the contact if it exists.  
- Prints `"Name not found."` if no match is found.

---
### `check_already_exist(name_to_add, phone_data)`
- Checks if the given name already exists in the phone book.  
- Returns `True` if the name exists, otherwise `False`.  
- Used internally by `add_contact`.

---
### `add_contact(name_to_add, number_to_add, phone_data)`
- Adds a new contact if it doesn’t already exist.  
- Writes the updated list back into the JSON file.  
- If the contact already exists, prints `"Contact already exists."`.
---
### `delete_contact(name_to_delete, phone_data)`
- Deletes a contact by name.  
- Returns the updated list without the deleted contact.  
- If the name is not found, prints `"Name not found."`.
---
### `update_contact(contact_to_update, phone_data, number_or_name)`
- Updates either the **name** or the **number** of an existing contact.  
- Prompts the user to enter the new value.  
- Saves the updated contacts back into the JSON file.  
- If the name doesn’t exist, prints `"Name not found."`.
