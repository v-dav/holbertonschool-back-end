#!/usr/bin/python3
"""A Python script that, using REST API
records all tasks from all employees to JSON format"""


import json
import requests

if __name__ == "__main__":
    """GET response from URL"""
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    employees_response = requests.get(
        "https://jsonplaceholder.typicode.com/users")

    """Convert response to list"""
    todos = todos_response.json()
    employees = employees_response.json()

    """Requierements"""
    json_object = {}

    for employee in employees:
        task_list = []
        for task in todos:
            if employee.get("id") == task.get("userId"):
                task_dict = {}
                task_dict["username"] = employee.get("username")
                task_dict["task"] = task.get("title")
                task_dict["completed"] = task.get("completed")
                task_list.append(task_dict)
        json_object[str(employee.get("id"))] = task_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(json_object, file)
