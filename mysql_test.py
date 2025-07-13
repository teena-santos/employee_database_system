import mysql.connector
import traceback

print("Trying to connect to MySQL...")

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="company"
    )
    print("✅ Connected to MySQL")

    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    for table in cursor:
        print("📋 Table:", table)

    connection.close()

except Exception as e:
    print("❌ Error:", e)
    traceback.print_exc()

input("\nPress Enter to exit...")