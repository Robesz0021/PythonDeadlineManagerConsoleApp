from operations import Operations
import datetime

def main():
    operations = Operations()
    choice = ""
    menu = """
    - Main menu -

    - Deadline Modifications -
    1. New Deadline
    2. Delete Deadline
    3. Modify Deadline

    - Search Deadline -
    4. Search Deadline by Name

    - Listing Deadline -
    5. List Deadlines by Date
    6. List Deadlines by Week
    7. List Deadlines by Month

    0. Stop program
    """

    while choice != 0:
        
        print(menu)

        try:
            choice = int(input("Please select a menu item: "))
        except:
            print("Invalid choice. Please enter a valid option.")
            continue

        if choice == 1:

            #Create new Deadline
            name = input("Enter the deadline's name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            location = input("Enter location: ")
            note = input("Enter a note or message if you want (else please write a \'-\'): ")

            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use (YYYY-MM-DD).")
                continue

            try:
                datetime.datetime.strptime(time, "%H:%M")
            except ValueError:
                print("Invalid time format. Please use (HH:MM).")
                continue

            if date != "" and time != "" and location != "" and name != "" and note != "":
                operations.createDeadline(name, date, time, location, note)
            else:
                print("Please fill out the full form! (If there is no note, please write a \"-\" to the note question.)")

        elif choice == 2:

            #Delete existing Deadline - Search by name
            name = input("Enter the name of the Deadline you want to delete: ")

            if name != "" and name != int:
                operations.deleteDeadline(name)

        elif choice == 3:

            #Modify existing Deadline - Search by name
            name = input("Enter the deadline's name you want to modify: ")
            nameChange = input("Enter the new name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            location = input("Enter location: ")
            note = input("Enter a note or message if you want (else please write a \'-\'): ")

            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use (YYYY-MM-DD).")
                continue

            try:
                datetime.datetime.strptime(time, "%H:%M")
            except ValueError:
                print("Invalid time format. Please use (HH:MM).")
                continue

            operations.modifyDeadline(name, nameChange, date, time, location, note)

        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 0:
            print("Program stopped!")
        elif choice < 0 and choice > 7:
            print("Invalid choice. Please enter a valid option.")

main()