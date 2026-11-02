def total_salary(path):
    """
    Total and Average Salary

    The total_salary() function reads salaries from a text file and calculates
    the total and average salary of all employees.

    The function returns a tuple with the total and average salary.

    """



    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0

        average = total / count
        return total, average

    except FileNotFoundError:
        print("Error: File not found.")
        return 0, 0

    except (ValueError, UnicodeError):
        print("Error: Invalid file data.")
        return 0, 0


total, average = total_salary("salary_file.txt")

print(f"Total salary: {total}")
print(f"Average salary: {average:g}")
