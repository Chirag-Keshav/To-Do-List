from db import add_task, fetch_tasks, delete_task, mark_task_done, reset_tasks

# Add tasks
add_task("Complete project")
add_task("Review PRs")

# Fetch and display tasks
tasks = fetch_tasks()
print("Tasks:")
for task in tasks:
    print(task)

# Mark a task as done
mark_task_done(1)

# Delete a task
delete_task(2)

# Fetch tasks again
print("Updated Tasks:")
tasks = fetch_tasks()
for task in tasks:
    print(task)

# Reset tasks
reset_tasks()
