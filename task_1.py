# Task #1

def read_file(path_to_file: str) -> list[str] | str:
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError as e:
        return f"Here should be some error message: {e}"


def convert_to_dict(list_of_lines: list[str]) -> dict[str, int] | str:
    result = {}
    try:
        for item in list_of_lines:
            key, value = item.split(',')
            result[key.strip()] = int(value.strip())

        print(result)
        return result
    except Exception as e:
        return f"Here should be some error message: {e}"


def total_salary(path: str) -> tuple[int, int] | str:
    """
    Function parses the TXT file with salaries and returns total and average salary

    :param path: Required. Path to TXT file
    :return: tuple(total, average) that represent total and average salary
    """
    file = read_file(path)
    employee_dict = convert_to_dict(file)
    total = sum([value for value in employee_dict.values()])
    average = int(total / len(employee_dict))

    return total, average
