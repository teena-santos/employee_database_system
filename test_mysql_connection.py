import mysql.connector
import traceback
import time

print("✅ SCRIPT STARTED!")

try:
    print("Connecting to MySQL...")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # If you set a password in XAMPP, put it here
        database="company"
    )

    print("✅ Connected successfully!")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    print("\n📋 Employee Table:")
    for row in rows:
        print(row)

    connection.close()

except Exception as e:
    print("\n❌ Exception occurred:")
    print(e)
    traceback.print_exc()

finally:
    input("\n🔚 Press Enter to exit...")