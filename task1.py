from datetime import datetime

def get_days_from_today(date):
    """
        Calculate the number of days from given date to today.

        args: date(str): A date string in the format 'YYYY-MM-DD'.

        returns: int: The number of days from the given date to today.
        error message: invalid date format
    """


    try:
        now = datetime.today().date()
        timeline = datetime.strptime(date, "%Y-%m-%d").date() 
        difference = now - timeline
        return difference.days
    except(ValueError, TypeError):
        return "Invalid date format. Please use 'YYYY-MM-DD'."

print("Days from today:", get_days_from_today("2026-12-12")) #-48
print("Days from today:", get_days_from_today("2026-10-17")) #5
print("Days from today:", get_days_from_today("lala")) # invalid date format. Please use 'YYYY-MM-DD'.