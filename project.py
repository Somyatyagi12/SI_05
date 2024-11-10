import datetime

class AttendanceSystem:
    def _init_(self):
        self.employees = {}
        self.attendance_records = {}

    def add_employee(self, employee_id, name):
        if employee_id not in self.employees:
            self.employees[employee_id] = name
            self.attendance_records[employee_id] = []
            print(f"Employee {name} added with ID: {employee_id}")
        else:
            print("Employee ID already exists.")

    def mark_attendance(self, employee_id):
        if employee_id in self.employees:
            date = datetime.date.today()
            if date not in self.attendance_records[employee_id]:
                self.attendance_records[employee_id].append(date)
                print(f"Attendance marked for {self.employees[employee_id]} on {date}")
            else:
                print("Attendance already marked for today.")
        else:
            print("Employee ID does not exist.")

    def view_attendance(self, employee_id):
        if employee_id in self.employees:
            print(f"Attendance records for {self.employees[employee_id]} (ID: {employee_id}):")
            for record in self.attendance_records[employee_id]:
                print(record)
        else:
            print("Employee ID does not exist.")

def main():
    system = AttendanceSystem()

    while True:
        print("\n1. Add Employee")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            system.add_employee(emp_id, name)
        elif choice == '2':
            emp_id = input("Enter Employee ID to mark attendance: ")
            system.mark_attendance(emp_id)
        elif choice == '3':
            emp_id = input("Enter Employee ID to view attendance: ")
            system.view_attendance(emp_id)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
