# Task #2

def read_file(path_to_file: str) -> list[str] | str:
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError as e:
        return f"Here should be some error message: {e}"


def convert_to_dict(list_of_lines: list[str]) -> list | str:
    result = []
    try:
        for item in list_of_lines:
            cat_id, name, age = item.split(',')
            result.append({"id": cat_id.strip(), "name": name.strip(), "age": age.strip()})
        return result
    except Exception as e:
        return f"Here should be some error message: {e}"


def get_cats_info(path: str) -> tuple[int, int] | str:
    """
    Function parses the TXT file with cat info and returns dict with cat info

    :param path: Required. Path to TXT file
    :return: dict that represents cat info
    """
    file = read_file(path)
    result = convert_to_dict(file)

    return result


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
