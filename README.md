# Employee Database System (Python + MySQL)

A simple command-line Python application that allows users to manage employee records using a MySQL database.

## 📌 Features

- Add new employee records (name, department, salary)
- View all stored employees
- MySQL database integration via `mysql-connector-python`
- Input validation and clean error handling
- CLI-based menu interface

## 🛠 Technologies Used

- Python 3.11
- MySQL (via XAMPP & phpMyAdmin)
- mysql-connector-python
- Git & GitHub

## 🧪 How to Run

1. Start **MySQL** using XAMPP
2. Ensure your MySQL has:
   - Database: `company`
   - Table:
     ```sql
     CREATE TABLE employees (
         id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(50),
         department VARCHAR(50),
         salary INT
     );
     ```
3. Run the app:

   ```bash
   python employee_system.py