Health Monitoring System
Overview
The Health Monitoring System is a Python-based application designed to manage patient records and medical reports. 
It allows users to register, log in, add medical reports, view reports, and receive reminders for follow-up checkups. 
This project demonstrates basic functionalities like user management, report handling, and data persistence using JSON files.

Features
Registration & Login: Users can register with a username and password and log in to access their accounts.
Add Medical Reports: Users can add medical reports with diagnosis and results.
View Reports: Users can view their medical reports along with the date they were added.
Checkup Reminders: The system automatically reminds users if a follow-up checkup is due based on the report's date(if the report is 30 days older).
Data Persistence: Patient data is saved and loaded from a JSON file to ensure data is retained between sessions.

Requirements
Python 3.x
json library (standard in Python)
datetime library (standard in Python)

Clone the Repository:
git clone https://github.com/akashjavvadi28/Hackathon_17-08-2024.git
