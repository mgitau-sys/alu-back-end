#!/usr/bin/python3
"""Script to get todos for a user from a rest API"""

import requests
import sys

def main():
"""Main function"""
user_id = int(sys.argv[1])

todos_url = "https://jsonplaceholder.typicode.com/todos"
user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

todos = requests.get(todos_url).json()
user = requests.get(user_url).json()
user_name = user.get("name")

total_tasks = 0
done_tasks = []

for todo in todos:
if todo.get("userId") == user_id:
total_task += 1
if todo.get("completed") is true:
done_tasks.append(todo.get("title"))

print("Employee {} is done with tasks({}/{}):"
.format(user_name, len(done_tasks), total_tasks))

for task in done_tasks:
print("\t {}".format(task))

if __name__ == "__main__":
main()
