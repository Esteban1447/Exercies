
contacts = []

def addContact(name, phone):
    contact = {"name": name, "phone": phone}
    contacts.append(contact)

def viewContacts():
    if not contacts:
        print("It's empty.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"name: {contact['name']}, phone: {contact['phone']}")

def searchContact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"name: {contact['name']}, phone: {contact['phone']}")
            return
    print(f"{name} not found.")

def deleteContact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"{contact['name']} has been deleted.")
            return
    print(f"{name} not found.")


def main():
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")

        option = input("Select an option: ")
        if option == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            addContact(name, phone)
        elif option == "2":
            viewContacts()
        elif option == "3":
            name = input("Enter contact name to search: ")
            searchContact(name)
        elif option == "4":
            name = input("Enter contact name to delete: ")
            deleteContact(name)
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()




    