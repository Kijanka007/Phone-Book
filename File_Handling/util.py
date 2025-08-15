import json

# Function: that writes the file
def write_file(file_name, data):
    with open(file_name, "w") as file:
        string = json.dumps(data)
        file.write(string)


# Function: reads the file
def read_file(file_name):
    with open(file_name, "r") as file:
        str_data = file.read()
        lst_data = json.loads(str_data)
        return lst_data