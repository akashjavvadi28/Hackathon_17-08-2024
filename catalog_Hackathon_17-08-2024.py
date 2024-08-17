import json
from datetime import datetime, timedelta

class Patient:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.reports = []

    def add_report(self, diagnosis, result):
        current_date = datetime.now().date()
        for report in self.reports:
            if report['diagnosis'] == diagnosis and (current_date - report['date']).days < 30:
                return "A similar diagnosis was made recently. No need to re-diagnose."
        self.reports.append({
            'diagnosis': diagnosis,
            'result': result,
            'date': current_date
        })
        return "Report added successfully."

    def view_reports(self):
        if not self.reports:
            return "No reports found."
        return [
            f"Diagnosis: {report['diagnosis']}, Result: {report['result']}, Date: {report['date']}"
            for report in self.reports
        ]

    def remind_checkup(self):
        reminders = []
        for report in self.reports:
            if (datetime.now().date() - report['date']).days >= 30:
                reminders.append(f"Reminder: Follow-up checkup needed for {report['diagnosis']}.")
        return reminders

class HealthMonitoringSystem:
    def __init__(self):
        self.patients = {}

    def register(self, username, password):
        if username in self.patients:
            return "Username already exists. Please choose another."
        self.patients[username] = Patient(username, password)
        return "Registration successful."

    def login(self, username, password):
        patient = self.patients.get(username)
        if patient and patient.password == password:
            return patient
        else:
            return None

    def save_data(self):
        with open('patient_data.json', 'w') as file:
            json_data = {
                username: {'password': patient.password, 'reports': patient.reports}
                for username, patient in self.patients.items()
            }
            json.dump(json_data, file)
            return "Data saved successfully."

    def load_data(self):
        try:
            with open('patient_data.json', 'r') as file:
                json_data = json.load(file)
                for username, data in json_data.items():
                    patient = Patient(username, data['password'])
                    patient.reports = data['reports']
                    self.patients[username] = patient
                return "Data loaded successfully."
        except FileNotFoundError:
            return "No data file found. Starting fresh."

# Initialize system and load data
system = HealthMonitoringSystem()
print(system.load_data())
# Continuing from the previous code...

def main_menu(system):
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(system.register(username, password))

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            patient = system.login(username, password)
            if patient:
                print("Login successful.")
                patient_menu(patient)
            else:
                print("Invalid credentials.")

        elif choice == '3':
            print(system.save_data())
            break

def patient_menu(patient):
    while True:
        print("\nPatient Menu:")
        print("1. Add Report")
        print("2. View Reports")
        print("3. Checkup Reminders")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            diagnosis = input("Enter diagnosis: ")
            result = input("Enter result: ")
            print(patient.add_report(diagnosis, result))

        elif choice == '2':
            reports = patient.view_reports()
            if isinstance(reports, list):
                for report in reports:
                    print(report)
            else:
                print(reports)

        elif choice == '3':
            reminders = patient.remind_checkup()
            if reminders:
                for reminder in reminders:
                    print(reminder)
            else:
                print("No reminders.")

        elif choice == '4':
            break

# Run the program
if __name__ == "__main__":
    main_menu(system)