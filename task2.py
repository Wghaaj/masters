def get_cats_info(path):
    """
    Cats Information

    The get_cats_info() function reads information about cats from a text file.

    It uses with open() to read the file and split() to separate the cat's
    ID, name and age. Each cat is stored as a dictionary with three keys.

    The function returns a list of dictionaries and uses try/except
    to handle missing files or invalid data.
    """


    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat)

        return cats

    except FileNotFoundError:
        print("Error: File not found.")
        return []

    except (ValueError, UnicodeError):
        print("Error: Invalid file data.")
        return []


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
