import sys
from pathlib import Path
from colorama import Fore, Style, init


def print_directory_tree(path, indent=""):
    for p in path.iterdir():
        if p.is_dir():
            print(f"{indent}{Fore.BLUE}📁{p.name}{Style.RESET_ALL} /")
            print_directory_tree(p, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}📄{p.name}{Style.RESET_ALL}")


def main():
    init(autoreset=True)
    if len(sys.argv) != 2:
        print("Використання: python task_3.py <шлях до директорії>")
        sys.exit(1)

    directory = Path(sys.argv[1])

    if not directory.is_dir():
        print(f"Помилка: {directory} не є директорією або не існує.")
        sys.exit(1)

    print(f"📦Структура директорії для {directory}:")
    print_directory_tree(directory)


if __name__ == "__main__":
    main()
