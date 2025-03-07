import json

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print(f"\n{name} added successfully!\n")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found!\n")
            return
        print("\nContact List:")
        for name, details in self.contacts.items():
            print(f"{name} - {details['Phone']}")
        print()

    def search_contact(self, search_key):
        found = False
        for name, details in self.contacts.items():
            if search_key.lower() in name.lower() or search_key in details["Phone"]:
                print(f"\nFound: {name} - {details['Phone']}, {details['Email']}, {details['Address']}\n")
                found = True
        if not found:
            print("\nContact not found!\n")

    def update_contact(self, name):
        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            print(f"\n{name} updated successfully!\n")
        else:
            print("\nContact not found!\n")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"\n{name} deleted successfully!\n")
        else:
            print("\nContact not found!\n")

    def save_contacts(self, filename="contacts.json"):
        with open(filename, "w") as file:
            json.dump(self.contacts, file)
        print("\nContacts saved successfully!\n")

    def load_contacts(self, filename="contacts.json"):
        try:
            with open(filename, "r") as file:
                self.contacts = json.load(file)
            print("\nContacts loaded successfully!\n")
        except FileNotFoundError:
            print("\nNo saved contacts found. Starting fresh!\n")


def main():
    contact_book = ContactBook()
    contact_book.load_contacts()

    while True:
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_key = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_key)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            contact_book.update_contact(name)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            contact_book.save_contacts()
            print("\nExiting Contact Book. Have a great day!\n")
            break

        else:
            print("\nInvalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
