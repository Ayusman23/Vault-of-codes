import json

def load_todos(filepath="todos.json"):
    """Loads to-do list from JSON file."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading the todo file. Starting with an empty list.")
        return []

def save_todos(todos, filepath="todos.json"):
    """Saves to-do list to JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(todos, f)
    except IOError:
        print("Error saving the todo file.")

def add_todo(todos):
    """Adds new to-do items, up to a maximum of 8."""
    count = 0
    while count < 20:
        description = input("Enter to-do description (or type 'done' to finish): ")
        if description.lower() == 'done':
            break
        todos.append({"description": description, "completed": False})
        count += 1
        print("To-do added!")
    
    if count == 8:
        print("Maximum of to-dos reached. Returning to the main menu.")

def list_todos(todos):
    """Lists all to-do items."""
    if not todos:
        print("No to-dos yet!")
        return

    for index, todo in enumerate(todos):
        prefix = "[x]" if todo["completed"] else "[ ]"
        print(f"{index + 1}. {prefix} {todo['description']}")

def mark_complete(todos):
    """Marks a to-do item as complete."""
    try:
        index = int(input("Enter to-do index to mark complete: ")) - 1
        if 0 <= index < len(todos):
            todos[index]["completed"] = True
            print("To-do marked complete!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Please enter a valid number.")

def remove_todo(todos):
    """Removes a to-do item."""
    try:
        index = int(input("Enter to-do index to remove: ")) - 1
        if 0 <= index < len(todos):
            del todos[index]
            print("To-do removed!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    todos = load_todos()

    while True:
        print("\nChoose an action:")
        print("1. Add to-do")
        print("2. List to-dos")
        print("3. Mark complete")
        print("4. Remove to-do")
        print("5. Exit")

        choice = input("> ")

        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            list_todos(todos)
        elif choice == "3":
            mark_complete(todos)
        elif choice == "4":
            remove_todo(todos)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

    save_todos(todos)
