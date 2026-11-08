from functools import wraps


def input_error(func):
    """
    Task 4: Console Assistant with Error Handling

    Functions:
    parse_input() separates the command from its arguments.
    The contact functions allow the user to add, update,
    find and display saved contacts.
    input_error() is a decorator that catches errors such as
    ValueError, KeyError and IndexError and returns a message
    instead of stopping the program.
    main() runs the bot and processes user commands.

    Result:
    The bot allows users to manage a simple contact book
    through the terminal. If the user enters an incorrect
    command or misses an argument, the program displays
    an error message and continues running.
    """

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter user name"
        except KeyError:
            return "Contact not found."

    return inner


def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError(name)
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


@input_error
def say_hello():
    return "How can I help you?"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print(say_hello())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
