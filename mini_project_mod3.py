#mini project - Module 3, Contact Management System

import re

email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

phone_regex = r'^(?:\(\d{3}\)\s?|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}$'

address_regex = r'^[a-zA-Z0-9\s,.-]+$'

def validate_email(email):
    return bool(re.match(email_regex, email))

def validate_phone(phone_number):
    return bool(re.match(phone_regex, phone_number))

def validate_address(address):
    return bool(re.match(address_regex, address)) or not address

def validate_identifier(identifier):
    if validate_email(identifier):
        return "email"
    elif validate_phone(identifier):
        return "phone"
    else:
        return None

def add_contact(contacts, identifier, name, phone_number, email, address=None, notes=None):
    identifier_type = validate_identifier(identifier)
    if not name:
        print("Name is required.")
        return
    if not phone_number and not email:
        print("Eiter phone number or email is required.")
        return

    if not identifier_type:
        print("Invalid identifier. Please provide a valid email or phone number.")
        return
    if identifier in contacts:
        print(f"Contact with identifier {identifier} already exists.")
        return
    if identifier_type == "email" and not validate_email(email):
        print("Invalid email format. Please enter a valid email address. ie. emily@hotmail.com ")
    if identifier_type == "phone" and not validate_phone(phone_number):
        print("Invalid phone number format. Please enter a valid phone number. ie 555-555-5555 / (555) 555-5555")
        return
    if address and not validate_address(address):
        print("Invalid address format. Please enter a valid address.")
        return

    contacts[identifier] = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "address": address,
        "notes": notes
    }
    print(f"New contact: {name}, {identifier} added.")

def edit_contact(contacts, identifier, name=None, phone_number=None, email=None, address=None, notes=None):
    if identifier not in contacts: 
        print(f"{identifier} not found in our directory and cannot be edited.")

    identifier_type = validate_identifier(identifier)

    if identifier_type == "email" and email and not validate_email(email):
        print("Invalid email format. Please enter a valid email address. ie. emily@hotmail.com ")
    if identifier_type == "phone" and phone_number and not validate_phone(phone_number):
        print("Invalid phone number format. Please enter a valid phone number.ie 555-555-5555 / (555) 555-5555")
        return
    if address and not validate_address(address):
        print("Invalid address format. Please enter a valid address.")
        return

    if name:
        contacts[identifier]["name"] = name
    if phone_number:
        contacts[identifier]["phone_number"] = phone_number
    if email:
        contacts[identifier]["email"] = email
    if address:
        contacts[identifier]["address"] = address
    if notes:
        contacts[identifier]["notes"] = notes
    print(f"Contact information updated for {identifier}")

def delete_contact(contacts, identifier):
    if identifier in contacts: 
        del contacts[identifier]
        print(f"Deleted from your contacts: {identifier}.")
    else: 
        print(f"{identifier} not found in directory")

def search_contact(contacts, identifier):
    if identifier in contacts:
        contact_info = contacts[identifier]
        print(f"Contact information for {contact_info['name']}:")
        print(f" Identifier: {identifier}")
        print(f" Phone Number: {contact_info['phone_number']}")
        print(f" Email: {contact_info['email']}")
        print(f" Address: {contact_info.get('address', 'Not available')}")
        print(f" Notes:  {contact_info.get('notes', 'No additional notes')}")
    else:
        print(f"Contact {identifier} not found.")

def display_contacts(contacts):
    if not contacts: 
        print("No contacts available.")
        return
    for identifier, contact_info in contacts.items():
        print(f"Contact info for {contact_info['name']}:")
        print(f"  Identifier: {identifier}")
        print(f"  Phone Number: {contact_info['phone_number']}")
        print(f"  Email: {contact_info['email']}")
        print(f"  Address: {contact_info.get('address', 'Not available')}")
        print(f"  Notes:  {contact_info.get('notes', 'No notes')}\n")


def export_to_text(contacts):
    with open("contacts.txt", "w") as file:
        for identifier, contact_info in contacts.items():
            file.write(f"Contact Info for {contact_info['name']}:\n")
            file.write(f"  Identifier: {identifier}\n")
            file.write(f"  Phone Number: {contact_info['phone_number']}\n")
            file.write(f"  Email: {contact_info['email']}\n")
            file.write(f"  Address: {contact_info.get('address', 'Not available')}\n")
            file.write(f"  Notes: {contact_info.get('notes', 'No additional notes')}\n\n")
    print("Contacts exported to contacts.txt")

contacts = {"alice@gmail.com": {
    "name": "Alice",
    "phone_number": "333-555-6666",
    "email": "alice@gmail.com",
    "address": "1 Colton Ct.",
    "notes": "yoga friend"
}}

while True:
    print("\nContact Management System")
    print("""\n1. Add Contact\n2. Edit Existing Contact Information \n3. Delete a Contact\n4. Search for a Contact\n5. Display all Contacts\n6. Export contacts to a text file\n7. Exit System""")
    choice = input("Enter your choice:   ")

    if choice =='1': #add contact
        identifier = input("Please enter identifier for your contact (email / phone number)")
        name = input("Please enter the contact's name:   ")
        phone_number = input("Please enter the contacts phone number:   ")
        email = input("Please enter the contact's email address:   ")
        address = input("Please enter the contact's address (if available):  ")
        notes = input("Please enter any additional notes (optional)")
        add_contact(contacts, identifier, name, phone_number, email, address, notes)

    elif choice == '2': #edit contact info
        identifier = input("Please enter the contact's identifier (email / phone number):  ")
        name = input("Please enter a new name for the contact (leave blank to leave unchanged):  ") or None
        phone_number = input("Please enter new phone number (leave blank to leave unchanged):   ") or None
        email = input("Please enter new email address (leave blank to leave unchanged):  ") or None
        address = input("Please enter new address (leave blank to leave unchanged):  ") or None
        notes = input("Please enter new notes (leave blank to keep current):   ") or None
        edit_contact(contacts, identifier, name, phone_number, email, address, notes)

    elif choice == '3': #delete contact
        identifier = input("Please enter the identifier (email / phone number) of contact you would like to delete:    ")
        delete_contact(contacts, identifier)

    elif choice == '4': #search for contact
        identifier = input("Please enter the identifier (email / phone number) of the contact you would like to search for:    ")
        search_contact(contacts, identifier)

    elif choice == '5': #display contact
        display_contacts(contacts)

    elif choice == '6': #Export to text file
        export_to_text(contacts)

    elif choice == '7':
        print("Exiting System.")
        break

    else:
        print("Invalid choice. Please try again.")
