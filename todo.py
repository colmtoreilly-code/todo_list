import json
from datetime import date
today = date.today()

def save_tasks():
        with open('todo.json', 'w') as file:
               json.dump(tasks,file,indent=4)

def load_tasks():
	try:
	        with open('todo.json', 'r') as file:
        	        return json.load(file)
	except (FileNotFoundError, json.JSONDecodeError):
		return[]

tasks = load_tasks()

def add_task():
    new_id = len(tasks) + 1
    description = input('Enter task: ')

    tasks.append({
        'id': new_id,
        'description': description,
        'completed': False
    })
    save_tasks()

def view_tasks():
    for task in tasks:
        status = '[✓]' if task['completed'] else '[ ]'
        print(f'Task {task['id']},{task['description']},{status}')

def complete_task():
	status_change  = int(input('Which task id have you completed?:'))
	for task in tasks:
		if task['id'] == status_change:
			task['completed'] = True
			print('Task Completed, well done!')
			break
	save_tasks()

def remove_task(tasks):
	which = int(input('Which task would you like to remove?:'))
	for task in tasks:
		if task['id'] == which:
			tasks.remove(task)
			print('Task Removed Successfully!')
			break
	for task in tasks:
		if task['id'] > which:
			task['id'] -= 1
		elif task['id'] == len(tasks):
			break
	save_tasks()

while True:

	print('\n=== To-Do List ===')
	print(today)
	print('1. View tasks')
	print('2. Add task')
	print('3. Change Completion Status')
	print('4. Delete task')
	print('5. Exit')

	choice = input('Choose an option:')

	if choice == '1':
		view_tasks()
	elif choice == '2':
		add_task()
	elif choice == '3':
		complete_task()
	elif choice == '4':
		remove_task(tasks)
	elif choice == '5':
		print('Goodbye!')
		break
	else:
		print('Invalid choice. Please try again.')
