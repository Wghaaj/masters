import re

def normalize_phone(tel):
    """
    Normalize a phone number to the format +380XXXXXXXXX.

    args: tel(str): A phone number string

    function: 
        - remove all non-digit characters from the input string
        - check if country code is present, if not add +38
        - check if the number has 12 digits, if not return an error message

    returns: The normalized phone number as str in the format +380XXXXXXXXX or an error message if the input is invalid.
    """

    digits = re.sub(r"\D", "", tel) 

    if len(digits) == 10 and digits.startswith("0"):
        digits = "+38" + digits
    elif len(digits) == 12 and digits.startswith("380"):
        digits = "+" + digits
    else:
        return "Invalid phone number format. Please provide a valid phone number."

    return digits


print ("Normalized phone number:", normalize_phone("0501234567")) # +380501234567
print ("Normalized phone number:", normalize_phone("+38(050)123-32-34")) # +380501233234
print ("Normalized phone number:", normalize_phone("38050-111-22-22")) # +380501112222
print ("Normalized phone number:", normalize_phone("  (095) 234-5678 ")) # +380952345678
print ("Normalized phone number:", normalize_phone("123")) # "Invalid phone number format..."


