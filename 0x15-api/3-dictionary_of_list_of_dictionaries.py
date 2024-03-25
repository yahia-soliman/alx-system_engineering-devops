#!/usr/bin/python3
"""exporting data gathered from an API to json"""
import json
import requests

if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    employees = {}
    usernames = {}
    for user in users:
        id = user.get('id')
        employees[id] = []
        usernames[id] = user.get('username')

    for task in tasks:
        id = task.get('userId')
        task['task'] = task.get('title')
        task['username'] = usernames.get(id)
        del task['title'], task['id'], task['userId']
        employees[id].append(task)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(employees, file)
