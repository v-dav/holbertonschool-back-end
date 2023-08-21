#!/usr/bin/python3
"""A Python script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress"""


import requests
import sys

if __name__ == "__main__":
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    employees_response = requests.get(
        "https://jsonplaceholder.typicode.com/users")

    employee_id = int(sys.argv[1])
    todos = todos_response.json()
    employees = employees_response.json()
    employee_all_task_list = []
    employee_completed_tasks = []

    for employee in employees:
        if employee.get("id") == employee_id:
            employee_name = employee.get("name")

    for task in todos:
        if task.get("userId") == employee_id:
            employee_all_task_list.append(task)
            if task.get("completed") is True:
                employee_completed_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(employee_completed_tasks),
                  len(employee_all_task_list)))

    for completed_task in employee_completed_tasks:
        print("\t", " ", completed_task.get("title"))
