tasks = []

tasks.append({
    'id':1,
    'description': 'Learn Python',
    'completed': False
})
tasks.append({
    'id':2,
    'description': 'Build a web app',
    'completed': False
})
tasks.append({
    'id':3,
    'description': 'Practice SQL',
    'completed': False
})
tasks.append({
    'id':4,
    'description': 'Go to the gym',
    'completed': False
})
tasks.append({
    'id':5,
    'description': 'Shoot around',
    'completed': False
})

def add_task():
    new_id = len(tasks) + 1
    description = input('Enter task: ')

    tasks.append({
        'id': new_id,
        'description': description,
        'completed': False
    })
def view_tasks():
    for task in tasks:
        status = 'Completed' if task['completed'] else 'Not Completed'
        print(f'ID: {task['id']}, Description: {task['description']}, Status: {status}')

def complete_task():
	status_change  = int(input('Which task id have you completed?:'))
	for task in tasks:
		if task['id'] == status_change:
			task['completed'] = True
			print('Task Completed, well done!')
			break
		
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
while True:
    
    print('\n=== To-Do List ===')
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
