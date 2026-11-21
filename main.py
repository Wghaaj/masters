from collections import UserDict
from datetime import date, datetime, timedelta
from functools import wraps
from colorama import Fore, Style, init
import pickle

init(autoreset=True)

"""
HW 11: Address Book Bot with Data Saving

Classes:
Field, Name and Phone store and validate contact information.
Birthday validates dates in DD.MM.YYYY format.
Record manages phone numbers and birthdays.
AddressBook stores contacts and finds upcoming birthdays.

Functions:
The bot supports adding, changing and viewing contacts,
managing birthdays, and displaying upcoming birthdays.
Input errors and missing contacts are handled with messages.
Pickle is used to save and load the address book from a file.

Result:
Console-based address book using OOP that saves contacts
when closing and restores them when the program starts again.
"""



class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isascii() or not value.isdigit():
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            birthday = datetime.strptime(value, "%d.%m.%Y")
            if birthday.strftime("%d.%m.%Y") != value:
                raise ValueError
            super().__init__(birthday)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)
        if found_phone is not None:
            self.phones.remove(found_phone)

    def edit_phone(self, old_phone, new_phone):
        found_phone = self.find_phone(old_phone)
        if found_phone is None:
            raise ValueError("Phone number not found.")
        found_phone.value = Phone(new_phone).value

    def find_phone(self, phone):
        for saved_phone in self.phones:
            if saved_phone.value == phone:
                return saved_phone
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = "; ".join(str(phone) for phone in self.phones)
        result = f"Contact name: {self.name.value}, phones: {phones}"
        if self.birthday is not None:
            result += f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}"
        return result


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)

    def get_upcoming_birthdays(self):
        today = date.today()
        upcoming = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday = record.birthday.value.date()
            try:
                next_birthday = birthday.replace(year=today.year)
            except ValueError:
                next_birthday = birthday.replace(year=today.year, day=28)

            if next_birthday < today:
                try:
                    next_birthday = birthday.replace(year=today.year + 1)
                except ValueError:
                    next_birthday = birthday.replace(year=today.year + 1, day=28)

            if 0 <= (next_birthday - today).days <= 7:
                if next_birthday.weekday() >= 5:
                    next_birthday += timedelta(days=7 - next_birthday.weekday())

                upcoming.append({
                    "name": record.name.value,
                    "congratulation_date": next_birthday.strftime("%d.%m.%Y")
                })

        return upcoming


def input_error(func):
    @wraps(func)
    def inner(args, book):
        try:
            return func(args, book)
        except ValueError as error:
            return f"Error: {error}"
        except (IndexError, KeyError):
            return Fore.RED + "Error: Invalid command arguments."
    return inner


def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


@input_error
def add_contact(args, book):
    if len(args) != 2:
        raise ValueError(Fore.RED + "Usage: add [name] [phone]")

    name, phone = args
    record = book.find(name)

    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return Fore.GREEN + "Contact added."

    record.add_phone(phone)
    return Fore.GREEN + "Contact updated."


@input_error
def change_contact(args, book):
    if len(args) != 3:
        raise ValueError(Fore.RED + "Usage: change [name] [old phone] [new phone]")

    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise ValueError(Fore.MAGENTA + f"Contact '{name}' not found.")

    record.edit_phone(old_phone, new_phone)
    return Fore.GREEN + "Contact updated."


@input_error
def show_phone(args, book):
    if len(args) != 1:
        raise ValueError( Fore.RED + "Usage: phone [name]")

    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError(Fore.MAGENTA + f"Contact '{name}' not found.")

    return Fore.GREEN + "; ".join(str(phone) for phone in record.phones) or Fore.YELLOW + "No phone numbers saved."


@input_error
def show_all(args, book):
    if args:
        raise ValueError(Fore.RED + "Usage: all")
    if not book.data:
        return Fore.GREEN + "Address book is empty."
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book):
    if len(args) != 2:
        raise ValueError(Fore.RED + "Usage: add-birthday [name] [DD.MM.YYYY]")

    name, birthday = args
    record = book.find(name)
    if record is None:
        raise ValueError(Fore.MAGENTA + f"Contact '{name}' not found.")

    record.add_birthday(birthday)
    return Fore.GREEN + "Birthday added."


@input_error
def show_birthday(args, book):
    if len(args) != 1:
        raise ValueError(Fore.RED + "Usage: show-birthday [name]")

    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError(Fore.MAGENTA + f"Contact '{name}' not found.")
    if record.birthday is None:
        return Fore.YELLOW + "Birthday not set."

    return record.birthday.value.strftime("%d.%m.%Y")


@input_error
def birthdays(args, book):
    if args:
        raise ValueError(Fore.RED + "Usage: birthdays")

    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return Fore.GREEN + "No birthdays in the next 7 days."

    return "\n".join(
        f"{person['name']}: {person['congratulation_date']}"
        for person in upcoming
    )

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input(
                    Fore.CYAN + Style.BRIGHT + "Enter a command: " + Style.RESET_ALL
                )
        except (EOFError, KeyboardInterrupt):
            print("\nGood bye!")
            break

        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        elif command:
            print("Invalid command.")

    save_data(book)


if __name__ == "__main__":
    main()
