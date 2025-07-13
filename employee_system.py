import mysql.connector
import traceback

# 1. Connect to MySQL
def connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # ← Replace with your MySQL password if you have one
            database="company"
        )
        print("✅ Connected to MySQL.")
        return connection
    except Exception as e:
        print("❌ Failed to connect to MySQL:", e)
        traceback.print_exc()
        return None

# 2. Add Employee
def add_employee():
    try:
        print("\n--- Add Employee ---")
        name = input("Enter employee name: ")
        print("✅ Name entered:", name)

        department = input("Enter department: ")
        print("✅ Department entered:", department)

        salary_input = input("Enter salary: ")
        print("✅ Salary input received:", salary_input)

        if not salary_input.isdigit():
            print("❌ Salary must be a number.")
            return

        salary = int(salary_input)

        db = connect()
        if db is None:
            print("❌ Connection failed. Cannot insert data.")
            return

        cursor = db.cursor()
        print("📥 Executing INSERT statement...")
        cursor.execute(
            "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)",
            (name, department, salary)
        )

        db.commit()
        db.close()
        print("✅ Employee added successfully!")

    except Exception as e:
        print("❌ Error while adding employee:", e)
        traceback.print_exc()

# 3. View Employees
def view_employees():
    try:
        db = connect()
        if db is None:
            print("❌ Connection failed.")
            return

        cursor = db.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()

        print("\n📋 Employee List:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Salary: {row[3]}")

        db.close()
    except Exception as e:
        print("❌ Error viewing employees:", e)
        traceback.print_exc()

# 4. Menu
def menu():
    while True:
        print("\n=== Employee System ===")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# 5. Start the app
menu()