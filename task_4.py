def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().casefold()
        return cmd, *args
    except Exception as e:
        return f"Invalid command: {e}"


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except Exception as e:
        return f"Invalid command: {e}"


def change_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact updated."
    except Exception as e:
        return f"Invalid command: {e}"


def show_phone(args, contacts):
    try:
        return f"{contacts[args[0]]}"
    except Exception as e:
        return f"Contact not found: {e}"


def show_all_phones(contacts):
    contact_dict = contacts
    if len(contact_dict) == 0:
        return "Contact list is empty"
    result = ""
    for contact, phone in contact_dict.items():
        result += f"{contact}: {phone}"
    return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "hello":
                print("How can I help you?")

            case "close" | "exit":
                print("Good bye!")
                break

            case "add":
                print(add_contact(args, contacts))

            case "change":
                print(change_contact(args, contacts))

            case "phone":
                print(show_phone(args, contacts))

            case "all":
                print(show_all_phones(contacts))

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
