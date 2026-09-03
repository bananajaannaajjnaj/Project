def register_patient():
    print("\n--- Patient Registration ---")

    # Input patient name
    while True:
        name = input("Enter patient's name: ")

        if name.replace(" ", "").isalpha():
            break
        else:
            print("ERROR! Please reenter valid name.")

    # Input patient age
    while True:
        try:
            age = int(input("Enter patient's age: "))

            if age > 0:
                break
            else:
                print("ERROR! Please reenter valid age.")

        except ValueError:
            print("ERROR! Please reenter valid age.")

    # Input patient ID
    while True:
        patient_id = input("Enter patient's ID: ")

        if patient_id.strip() != "":
            break
        else:
            print("ERROR! Please reenter valid ID.")

    print("\nPatient confirmed, please continue.")

    return name, age, patient_id
