######################################
########                      ########
# https://github.com/halilumutyalcin #
########                      ########
######################################


import json


class NotAPhoneNumberException(ValueError):
    pass


def save_contacts(contacts, filename):
    with open(filename, 'w') as f:
        json.dump(contacts, f)


def print_contact(contact_info):
    print("{0[name]:<30} {0[phone]:^30} {0[email]:>30}".format(contact_info))


def create_contact(name=None):
    if name is None:  # Name not provided, so we need to ask for it
        name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ").lower()

    if len(phone) != 10:  # Very simple validation
        raise NotAPhoneNumberException

    return {'name': name, 'phone': phone, 'email': email}


def address_book(filename):
    try:
        with open(filename) as f:
            contacts = json.loads(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        # File not found or empty, use a default container
        contacts = {}

    while True:
        print('''Greetings user! Let's make an addressbook!

Would you like to:
 1.) Add a New Contact
 2.) List All Contacts
 3.) Search Contacts
 4.) Edit A Contact
 5.) Delete A Contact
 6.) Quit Program''')

        choice = input("Select an option: ")

        if choice == "1":
            try:
                new_contact = create_contact()
            except NotAPhoneNumberException:
                print("The phone number entered is invalid, creation aborted!")
            else:
                contacts[new_contact['name']] = new_contact
                save_contacts(contacts, filename)

        elif choice == "2":
            print_contact({'name': 'NAME', 'phone': 'PHONE', 'email': 'EMAIL'})
            for contact in contacts.values():
                print_contact(contact)

        elif choice == "3":
            search = input("Please enter name (case sensitive): ")
            try:
                print_contact(contacts[search])
            except KeyError:
                print("Contact not found")

        elif choice == "4":
            search = input("Please enter name (case sensitive): ")
            try:
                print_contact(contacts[search])
            except KeyError:
                print("Contact not found")
            else:
                try:
                    contacts[search] = create_contact(search)
                except NotAPhoneNumberException:
                    print("Invalid phone number. Contact was not edited!")
                else:
                    save_contacts(contacts, filename)

        elif choice == "5":
            search = input("Please enter name (case sensitive): ")
            try:
                contacts.pop(search)
            except KeyError:
                print("Contact not found")
            else:
                save_contacts(contacts, filename)

        elif choice == "6":
            print("Ending Contact Book.\nHave a nice day!")
            break

        else:
            print("Invalid Input! Try again.")


if __name__ == "__main__":
    address_book('contact.txt')