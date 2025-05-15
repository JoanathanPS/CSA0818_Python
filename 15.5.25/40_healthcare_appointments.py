appointments = {}

def show_slots():
    for hour in range(9, 17):
        if hour not in appointments:
            print(f"{hour}:00 - Available")
        else:
            print(f"{hour}:00 - Booked by {appointments[hour]}")

def book_slot(hour, patient):
    if hour in appointments:
        return "Slot already booked"
    appointments[hour] = patient
    return "Appointment booked"

def cancel_slot(hour):
    if hour in appointments:
        del appointments[hour]
        return "Appointment cancelled"
    return "No appointment found"

show_slots()
print(book_slot(10, "John"))
print(cancel_slot(10))