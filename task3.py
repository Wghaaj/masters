import sys
from collections import Counter
from datetime import datetime


LEVELS = ("INFO", "DEBUG", "ERROR", "WARNING")


def parse_log_line(line: str) -> dict:
    """
    Task 3: Log File Analysis

    Functions:
    parse_log_line() splits each log entry into its details.
    load_logs() reads the log file and stores the entries.
    filter_logs_by_level() selects logs of a specific level.
    count_logs_by_level() counts how many entries belong
    to each level, and display_log_counts() prints the results
    in a table.

    Result:
    The program reads a log file and displays the number
    of INFO, DEBUG, ERROR and WARNING entries.
    It also allows the user to filter logs by level
    and handles errors if the file cannot be read.
    """

    parts = line.strip().split(maxsplit=3)
    if len(parts) != 4:
        raise ValueError("Invalid log line format")

    date, time, level, message = parts
    try:
        datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
    except ValueError as error:
        raise ValueError("Invalid date or time in log") from error

    if level not in LEVELS:
        raise ValueError("Unknown log level")

    return {"date": date, "time": time, "level": level, "message": message}


def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, "r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                logs.append(parse_log_line(line))
            except ValueError as error:
                raise ValueError(f"Line {number}: {error}") from error
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    # Match the level even if the user types it in lowercase.
    return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    counts = Counter(log["level"] for log in logs)
    return {level: counts[level] for level in LEVELS}


def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<17}| Кількість")
    print(f"{'-' * 17}|{'-' * 10}")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: python task3.py logfile.log [level]")
        return

    try:
        logs = load_logs(sys.argv[1])
    except (FileNotFoundError, PermissionError, UnicodeError, OSError, ValueError) as error:
        print(f"Error: {error}")
        return

    display_log_counts(count_logs_by_level(logs))

    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        if level not in LEVELS:
            print("Unknown level. Use INFO, DEBUG, ERROR or WARNING.")
            return

        print(f"\nДеталі логів для рівня '{level}':")
        for log in filter_logs_by_level(logs, level):
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
