import pyodbc

# Establish a connection to the SQL Server database
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=your_server_name;'
    'DATABASE=your_database_name;'
    'UID=your_username;'
    'PWD=your_password'
)

# Function to create a new guest booking
def create_booking(name, room_type, nights):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Bookings (Name, RoomType, Nights) VALUES (?, ?, ?)",
                   (name, room_type, nights))
    conn.commit()
    print("Booking created successfully.")

# Function to calculate and display the bill for a guest
def generate_bill(name):
    cursor = conn.cursor()
    cursor.execute("SELECT RoomType, Nights FROM Bookings WHERE Name=?", (name,))
    result = cursor.fetchone()

    if result:
        room_type, nights = result
        # Calculate the total bill based on the room type and number of nights
        if room_type == "Standard":
            rate = 100
        elif room_type == "Deluxe":
            rate = 150
        elif room_type == "Suite":
            rate = 200
        else:
            print("Invalid room type.")
            return

        total_bill = rate * nights
        print(f"Guest Name: {name}")
        print(f"Room Type: {room_type}")
        print(f"Number of Nights: {nights}")
        print(f"Total Bill: ${total_bill}")
    else:
        print("No booking found for the guest.")

# Function to check guest's booking status
def check_booking_status(name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Bookings WHERE Name=?", (name,))
    result = cursor.fetchall()

    if result:
        print("Booking found for the guest:")
        for row in result:
            print(f"Guest Name: {row.Name}")
            print(f"Room Type: {row.RoomType}")
            print(f"Number of Nights: {row.Nights}")
            print()
    else:
        print("No booking found for the guest.")

# Function to cancel a guest's booking
def cancel_booking(name):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Bookings WHERE Name=?", (name,))
    conn.commit()
    print("Booking canceled successfully.")

# Example usage of the functions
create_booking("John Doe", "Deluxe", 3)
generate_bill("John Doe")
check_booking_status("John Doe")
cancel_booking("John Doe")
check_booking_status("John Doe")

# Close the database connection
conn.close()
