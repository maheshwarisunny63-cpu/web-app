def get_todos(filepath="todos.txt"):  # Define a function that returns a list of todos
    """Returns a list of todos from the todos.txt"""  # Docstring explaining function purpose
    with open(filepath, "r") as f:  # Open the file in read mode
        todos_local = f.readlines()  # Return all lines as a list
    return todos_local

def write_todos(tasks:list) -> None:  # Define function that writes a list to file, returns nothing
    """Writes the task to the todos.txt"""  # Docstring explaining function purpose
    with open("todos.txt", "w") as f:  # Open the file in write mode (overwrites existing content)
        f.writelines(tasks)  # Write all list items to file

def show_todos() -> None:  # Define function to display todos
    """Shows the todos from the todos.txt"""  # Docstring explaining function purpose
    tasks = get_todos()  # Get the list of todos from file
    if len(tasks) > 0:
        for index, item in enumerate(tasks):  # Loop through todos with index
            print(f"{index + 1}-{item.strip()}")  # Print numbered todo after removing newline
    else:
        print("No todos available.")