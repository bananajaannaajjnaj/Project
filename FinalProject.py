from datetime import datetime, timedelta


# Option 1: Registration
def registration():
    # Patient name
    while True:
        patientName = input("Enter patient name: ")

        if patientName.replace(" ", "").isalpha():
            break
        else:
            print("ERROR! Please reenter valid name.")

    # Patient ID
    while True:
        patientID = input("Enter patient ID: ")

        if patientID.isalnum():
            break
        else:
            print("ERROR! Please reenter valid ID.")

    # Patient age
    while True:
        try:
            patientAge = int(input("Enter patient age: "))

            if patientAge >= 0:
                break
            else:
                print("ERROR! Please reenter valid details.")

        except ValueError:
            print("ERROR! Please reenter valid details.")

    print("Patient confirmed, please continue.")


# Option 2: Book Appointment
def book_appointment():
    # Department
    while True:
        department = input("Enter department (GP/Specialist): ").strip()

        if department.lower() in ["gp", "specialist"]:
            break
        else:
            print("ERROR! Please reenter valid department.")

    if department.lower() == "gp":
        print("Department: GP selected")
    else:
        print("Department: Specialist selected")

    # Appointment date
    while True:
        appointmentDate = input(
            "Enter appointment date (DD/MM/YYYY): "
        )

        try:
            appointment_date = datetime.strptime(
                appointmentDate, "%d/%m/%Y"
            ).date()

            current_date = datetime.now().date()
            minimum_date = current_date + timedelta(days=7)

            if appointment_date >= minimum_date:
                break
            else:
                print("ERROR! Appointment must be at least 7 days from today.")

        except ValueError:
            print("ERROR! Please reenter valid appointment date.")

    # Booking confirmation
    bookingConfirmation = input(
        "Would you like to confirm your booking? (Yes/No): "
    )

    if bookingConfirmation.lower() == "yes":
        print("Thank you for booking at CareBridge Hospital!")
    else:
        print("Booking cancelled.")


# Option 3: Calculate Bill
def calculate_bill():
    # Patient type
    while True:
        patientType = input(
            "Enter patient type (Subsidised/Private): "
        )

        if patientType.lower() in ["subsidised", "private"]:
            break
        else:
            print("ERROR! Please enter valid patient type.")

    # Number of lab tests
    while True:
        try:
            numberOfLabTest = int(
                input("Enter number of lab tests: ")
            )

            if numberOfLabTest >= 0:
                break
            else:
                print("ERROR! Please enter a whole number.")

        except ValueError:
            print("ERROR! Please enter a whole number.")

    # Fees
    consultationFee = 100
    labTestRate = 10

    # Calculate subtotal
    subtotal = consultationFee + (numberOfLabTest * labTestRate)

    # Calculate total
    if patientType.lower() == "subsidised":
        total = subtotal * 0.70
    else:
        total = subtotal

    print("Patient Type:", patientType)
    print("Total amount to pay: $", format(total, ".2f"))


# Option 4: Assign Triage Room
def assign_triage_room():
    while True:
        try:
            severity = int(
                input("What is your severity level? ")
            )

            if severity >= 1:
                break
            else:
                print("ERROR! Please enter a valid severity level.")

        except ValueError:
            print("ERROR! Please enter a whole number.")

    # Assign room
    if severity >= 1 and severity <= 4:
        room = "Waiting room"

    elif severity >= 5 and severity <= 7:
        room = "Room 1"

    else:
        room = "Room 2"

    print("Triage summary:")
    print("Severity level:", severity)
    print("Room:", room)


# Main Menu
def main():
    while True:
        print("\n===== CareBridge Hospital =====")
        print("Menu")
        print("1. Registration")
        print("2. Book Appointment")
        print("3. Calculate Bill")
        print("4. Assign Triage Room")
        print("5. Exit")

        option = input("Enter your option: ")

        if option == "1":
            registration()

        elif option == "2":
            book_appointment()

        elif option == "3":
            calculate_bill()

        elif option == "4":
            assign_triage_room()

        elif option == "5":
            print("End")
            break

        else:
            print("ERROR! Please select a valid option.")


# Run the program
main()