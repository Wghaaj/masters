def parse_input(user_input):
    """
    Task 4 - Assistant Bot

    This program is a simple console bot that stores names and phone numbers.

    The parse_input() function separates the command from its arguments.
    The add_contact() function saves a new contact, change_contact() updates
    an existing number, and show_phone() finds a phone number by name.
    The show_all() function displays all saved contacts.

    The main() function runs the bot and processes user commands until
    the user enters "exit" or "close".
    """

    
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    name = name.lower()

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command."

    name = args[0].lower()

    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    if not contacts:
        return "No contacts found."

    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            print("Invalid command.")
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            if args:
                print("Invalid command.")
                continue
            print("Good bye!")
            break

        elif command == "hello":
            if args:
                print("Invalid command.")
            else:
                print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            if args:
                print("Invalid command.")
            else:
                print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
