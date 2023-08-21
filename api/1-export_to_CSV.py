#!/usr/bin/python3
"""A Python script that, using REST API, for a given employee ID,
returns a CSV file with all related tasks"""


import csv
import requests
import sys

if __name__ == "__main__":
    """GET response from URL"""
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    employees_response = requests.get(
        "https://jsonplaceholder.typicode.com/users")

    """Convert response to json file"""
    todos = todos_response.json()
    employees = employees_response.json()

    """Requierements"""
    employee_id = int(sys.argv[1])

    for employee in employees:
        if employee.get("id") == employee_id:
            our_employee = employee

    filename = str(our_employee.get("id")) + ".csv"

    with open(filename, 'w', newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            if task.get("userId") == employee_id:
                writer.writerow([our_employee.get("id"),
                                our_employee.get("username"),
                                task.get("completed"),
                                task.get("title")])
