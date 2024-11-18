#mini project - Module 3, Contact Management System

def display_contacts(contacts):
    for name, contact_info in contacts.items():
        print(f"Contact : {name}, Email / Phone: {contact_info['contact_info']}")

def add_contact(contacts, name, contact_info):
    if name not in contacts:
        contacts[name] = {"contact_info": contact_info}
        print(f"New contact: {name}, {contact_info} added.")
    else:
        print(f"Contact {name} already exists in our system.")

def edit_contact(contacts, name, new_contact_info):
    if name in contacts: 
        contacts[name]["contact_info"] = new_contact_info
        print(f"Contact information updated: {name}, {contact_info}")
    else:
        print(f"{name} is not listed in our directory and cannot be edited.")

def delete_contact(name, contacts):
    if name in contacts: 
        del contacts[name]
        print(f"Deleted from your contacts: {name}.")
    else: 
        print(f"Contact not found in directory")

def search_contact(name, contacts):
    if name in contacts:
        print(f"Contact information as follows: {name}: {contacts[name]['contact_info']}")
    else:
        print(f"Contact {name} not found.")

#name, contact_info

contacts = {"alice" : {"contact_info": "alice@gmail.com"}}

while True:
    print("\nContact Management System")
    print("1. Display Contacts\n2. Add Contact\n3. Edit Contact Information \n4. Delete Contact\n5. Search Contacts\n6. Exit System")
    choice = input("Enter your choice:   ")

    if choice == '1':
        display_contacts(contacts)

    elif choice =='2':
        name = input("Please enter the contacts name:    ")
        contact_info = input("Please enter contact information for our records:   ")
        add_contact(contacts, name, contact_info)

    elif choice == '3':
        name = input("Please enter the contacts name:    ")
        new_contact_info = input("Please enter new contact information:  ")
        edit_contact(contacts, name, new_contact_info)

    elif choice == '4':
        name = input("Please enter the name of the contact you would like to delete:    ")
        delete_contact(name, contacts)

    elif choice == '5':
        name = input("Please enter the name of the contact you would like to search for:    ")
        search_contact(name, contacts)

    elif choice == '6':
        print("Exiting System.")
        break

    else:
        print("Invalid choice. Please try again.")
