#!/usr/bin/python3
"""exporting data gathered from an API to json"""
import json
import requests
import sys

if __name__ == '__main__' and len(sys.argv) > 1:
    id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
    user = user.json()
    if not user.get('name'):
        exit()
    name = user.get('username')
    tasks = requests.get('https://jsonplaceholder.typicode.com'
                         '/todos?userId=' + id)
    tasks = tasks.json()
    for task in tasks:
        task['task'] = task.get('title')
        task['username'] = name
        del task['title'], task['id'], task['userId']

    with open(id + '.json', 'w') as file:
        obj = {id: tasks}
        json.dump(obj, file)
