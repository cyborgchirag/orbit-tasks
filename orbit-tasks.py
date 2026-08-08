"""
==================================================
                 ORBIT TASKS

            Powered by CYBORG

Version      : 1.0
Developer    : Chirag
Release Date : 09-08-2026
Release Time : 00:15

"Organize. Focus. Achieve."

==================================================
"""

"""
Version History

v1.0
- Added Task
- View Tasks
- Remove Tasks
- Count Tasks
- Clear All
- Exit Confirmation

------------------------------------------
Future Plans

v2.0
- File Saving
- Task Editing
- Search Tasks

v3.0
- GUI

v4.0
- Web Application

v5.0
- AI Assistant
"""

import time
# Creating list
tasks = []
# Formalities
print("=" * 45)
print("        ORBIT TASKS v1.0")
print("        Powered by CYBORG")
print("=" * 45)
print("Welcome! Let's organize your day.")
print()
#printing options
print("options: ".title())
menu = {
    '1.':'Add Task',
    '2.':'View Task',
    '3.':'Remove Task',
    '4.':'Count All',
    '5.':'Clear All',
    '6.':'Exit',
}

for key, val in menu.items():
    print(f'{key} {val}')
print()
print('TIP: For leaving a particular category instead of app then, print "exit" ')
#intializing loop 
active = True
while active:
    user = input('Enter number of task which you want to do: ') 
    if user.isdigit():
        user = int(user)
        while True:
            if user == 1:
                t = input('TASK: ').title()
                if t.lower() == 'exit':
                    break;
                else:
                    tasks.append(t)
                    print()
            elif user == 2:
                if len(tasks) != 0:
                    print(*tasks, sep='\n')
                    break;
                else:
                    print('All tasks are done')

            elif user == 3:
                t = input('TASK: ').title()
                if t.lower() == 'exit':
                    break;
                else:
                    if t in tasks:
                        tasks.remove(t)
                        print(f'Removed Task is: {t} ')
                    else:
                        print('Not found')
            elif user == 4:
                if len(tasks) != 0 :
                    if len(tasks) == 1:
                        print(f'{len(tasks)} task is pending')
                        print()
                        break;
                    else:
                        print(f'{len(tasks)}  tasks are pending')
                        print()
                    break;
                else:
                    print(f'All  tasks are complete')
                    print()
                    break;

            elif user == 5:
                r = input('Clear all tasks (yes / no): ')
                print()
                if r.lower() == 'yes':
                    time.sleep(1.75846)
                    tasks.clear()
                    print('All tasks are cleared')
                    break;
                else:
                    break;

            elif user == 6:
                r = input('Want to exit (yes / no): ')
                print()
                if r.lower() == 'yes':
                    print('Thanks for using ORBIT TASKS (Powered by CYBORG). Have a great day.')
                    active = False
                    break;

                elif r.lower() == 'no':
                    break;