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
