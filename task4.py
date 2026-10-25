from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
        Find birthdays occurring within the next 7 days.

        Move weekend congratulations to the following Monday.

        Args:
            users (list): List of dictionaries containing names and birthdays.

        Returns:
            list: Dictionaries containing names and congratulation dates.eturn a list of dictionaries with the person's name and when to congratulate them 

    """

    today  = datetime.today().date()

    new_users = []

    for user in users:
        birthday  = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        next_birthday = birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        difference = (next_birthday - today).days
        if 0 <= difference <= 7:
            if next_birthday.weekday() == 5:  # Saturday
                next_birthday += timedelta(days=2) 
            elif next_birthday.weekday() == 6:  # Sunday
                next_birthday += timedelta(days=1) 

            new_users.append({"name": user["name"], "congratulation_date": next_birthday.strftime("%Y.%m.%d") })

    return new_users


users = [
    {"name": "Alice", "birthday": "1990.12.15"},
    {"name": "Bob", "birthday": "1985.12.20"},
    {"name": "Charlie", "birthday": "1992.12.25"},
    {"name": "David", "birthday": "1988.12.30"},
    {"name": "Eve", "birthday": "1995.01.02"}
] # no upcoming 

users = [
    {"name": "Alice", "birthday": "1990.10.27"},
    {"name": "Bob", "birthday": "1985.11.01"},
    {"name": "Charlie", "birthday": "1992.10.31"},
    {"name": "David", "birthday": "1988.12.30"},
    {"name": "Eve", "birthday": "1995.01.02"}
] # 3 upcoming


upcoming_birthdays = get_upcoming_birthdays(users)

print("Upcoming birthdays within a week: ")

if not upcoming_birthdays:
    print("No upcoming birthdays") 
else:
    for user in upcoming_birthdays:
        print(f"{user['name']} : {user['congratulation_date']}") 

