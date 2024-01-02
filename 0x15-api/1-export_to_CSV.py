#!/usr/bin/python3
"""
Export data to CSV format
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} employee_id'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get('name')

    with open('{}.csv'.format(employee_id), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            taskwriter.writerow([employee_id, employee_name,
                                 task.get('completed'), task.get('title')])
