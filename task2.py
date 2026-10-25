from random import random

def get_numbers_ticket(min, max, quantity):
    """
        Get min, max, quantity values for lotery tickets 
        
        args: min(int): not less than 1 
            max(int): not greater than 1000 
            quantity(int): between min and max 
        
        returns: sorted list of unique random numbers
                empty list if invalid input
    """

    if not all(type (x) is int for x in(min, max, quantity)):
        return []

    if min <1 or max > 1000 or min > max:
        return []

    if quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = set()
    while len(numbers) < quantity:
        number = int(random() * (max - min + 1)) + min
        numbers.add(number)
    
    return sorted(list(numbers))

print("Lottery ticket numbers:", get_numbers_ticket(1, 50, 5)) # [1, 2, 3, 4, 5] (example output)
print("Lottery ticket numbers:", get_numbers_ticket(4, 30, 3)) # [4, 5, 6] (example output)
print("Lottery ticket numbers:", get_numbers_ticket(10, 5, 3)) #[] (invalid input)
print("Lottery ticket numbers:", get_numbers_ticket(2, "5", 3)) #[] 


