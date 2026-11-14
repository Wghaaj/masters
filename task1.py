from collections import UserDict

"""
Task: Address Book Using OOP

Classes:
Field and Name store contact information.
Phone validates 10-digit numbers.
Record manages contacts and their phone numbers.
AddressBook stores, finds and deletes contacts.

Result:
The program manages an address book using OOP,
supports multiple phone numbers and validates
phone numbers before saving them.
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
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain exactly 10 digits.")

        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

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

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)




if __name__ == "__main__":
    book = AddressBook()

    john = Record("John")
    john.add_phone("1234567890")
    john.add_phone("5555555555")
    book.add_record(john)

    jane = Record("Jane")
    jane.add_phone("9876543210")
    book.add_record(jane)

    print("1. All contacts:")
    for record in book.data.values():
        print(record)

    print("\n2. Find John:")
    print(book.find("John"))

    print("\n3. Find a phone number:")
    print(john.find_phone("5555555555"))

    print("\n4. Edit John's phone:")
    john.edit_phone("1234567890", "1112223333")
    print(john)

    print("\n5. Remove John's phone:")
    john.remove_phone("5555555555")
    print(john)

    print("\n6. Add another phone to John:")
    john.add_phone("2223334444")
    print(john)

    print("\n7. Delete Jane:")
    book.delete("Jane")
    for record in book.data.values():
        print(record)

    print("\n8. Find deleted contact:")
    print(book.find("Jane"))

    print("\n9. Test invalid phone number:")
    try:
        john.add_phone("12345")
    except ValueError as error:
        print(error)

    print("\n10. Test editing a missing phone:")
    try:
        john.edit_phone("0000000000", "3334445555")
    except ValueError as error:
        print(error)
