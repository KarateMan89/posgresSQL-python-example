import psycopg2
from psycopg2 import sql
from tabulate import tabulate

# connection parameters
db_params = {
    'dbname': 'assignment 4',
    'user': 'postgres',      
    'password': 'kyokushin',  
    'host': 'localhost'
}

# connect to the database
def connect():
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except (Exception) as error:
        print("Error connecting to the database:", error)
        return None

# get all the students and display them using tabulate
def getAllStudents():
    conn = connect()

    if conn is None:
        print("getAllStudents(): Failed to connect to the database.")
        return
    
    try:
        # this will close the connection automatically 
        with conn:
            # this is like a control object that we can use to execute queries
            with conn.cursor() as cur:
                # create headers and empty list for student data
                headers = ["Student ID", "First Name", "Last Name", "Email", "Enrollment Date"]
                student_data = []

                # get all the students from the database
                cur.execute("SELECT * FROM students")
                students = cur.fetchall()

                # if we had students, add them to the student_data list
                if students:
                    student_data = [(row[0], row[1], row[2], row[3], row[4]) for row in students]
                
                # create table for tabulate and print it 
                table = tabulate(student_data, headers, tablefmt="pretty")
                print(table)
    except (Exception) as error:
        print(f"Error getting students from the database: {error}")
    

# add a student to the database
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()

    if conn is None:
        print("addStudent(): Failed to connect to the database.")
        return

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"),
                    (first_name, last_name, email, enrollment_date)
                )
            print("Student added successfully.")
            
    except (Exception, psycopg2.Error) as error:
        print(f"Error adding student to the database: {error}")


# update student's email
def updateStudentEmail(student_id, new_email):
    conn = connect()

    if conn is None:
        print("updateStudentEmail(): Failed to connect to the database.")
        return

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    sql.SQL("UPDATE students SET email = %s WHERE student_id = %s"),
                    (new_email, student_id)
                )

            if cur.rowcount > 0:
                print("Student email updated successfully.")
            else:
                print("Student not found with the given ID.")

    except (Exception) as error:
        print(f"Error updating student email: {error}")


# delete a student 
def deleteStudent(student_id):
    conn = connect()

    if conn is None:
        print("deleteStudent(): Failed to connect to the database.")
        return

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    sql.SQL("DELETE FROM students WHERE student_id = %s"),
                    (student_id,)
                )
            if cur.rowcount > 0:
                print("Student deleted successfully.")
            else:
                print("Student not found with the given ID.")
        conn.close()

    except (Exception) as error:
        print(f"Error deleting student: {error}")

# test the functions
if __name__ == "__main__":
    getAllStudents()

    addStudent("Yordan", "Slavchev", "yordan.slavchev@example.com", "1989-06-02")

    updateStudentEmail(7, "yoyo@example.com") # change the ID to test the function

    deleteStudent(7) # change the ID to test the function