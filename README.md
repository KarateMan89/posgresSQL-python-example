
## README

### YouTube video
https://youtu.be/i2cistmFPOg

### Overview
This Python script is designed to manage student records in a PostgreSQL database. It includes functions to connect to the database, add, update, and delete student records, as well as retrieve and display all student records.

### Prerequisites
- Python
- PostgreSQL
- `psycopg2` library
- `tabulate` library

### Setup
1. Ensure Python is installed on your system.
2. Install PostgreSQL and set up your database.
3. Install required Python libraries:
   ```
   pip install psycopg2 tabulate
   ```

### Configuration
- Modify the `db_params` in the script with your PostgreSQL database credentials.
- The script expects a `students` table in your database with the following schema:
  - `student_id` (Integer)
  - `first_name` (String)
  - `last_name` (String)
  - `email` (String)
  - `enrollment_date` (Date)

### Usage
Run the script using Python. The script will automatically connect to your database and execute the functions as per your commands.

### Functions
- `getAllStudents()`: Retrieves and displays all student records.
- `addStudent(first_name, last_name, email, enrollment_date)`: Adds a new student record.
- `updateStudentEmail(student_id, new_email)`: Updates the email of an existing student.
- `deleteStudent(student_id)`: Deletes a student record.
