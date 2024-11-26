import mysql.connector
from datetime import datetime, timedelta

# Database connection function
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Fs@bbr619",  # Replace with your MySQL password
        database="todo_app"
    )

# Add a task
def add_task(task_title):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, date) VALUES (%s, CURRENT_DATE)", (task_title,))
    conn.commit()
    print(f"Task added: {task_title}")
    conn.close()

# Fetch all tasks
def fetch_tasks(date):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE date = %s", (date,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks


# Delete a task by ID
def delete_task(task_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    print(f"Task with ID {task_id} deleted.")
    conn.close()

# Mark a task as done
def mark_task_done(task_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET stat = TRUE WHERE id = %s", (task_id,))
    conn.commit()
    print(f"Task with ID {task_id} marked as done.")
    conn.close()

# Reset tasks (delete all)
def reset_tasks():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE tasks")
    conn.commit()
    print("All tasks reset!")
    conn.close()

def import_previous_day_tasks():
    yesterday = (datetime.today() - timedelta(days=1)).date()
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM tasks WHERE date = %s", (yesterday,))
    tasks = cursor.fetchall()
    
    for task in tasks:
        title = task[0]
        cursor.execute("INSERT INTO tasks (title, date) VALUES (%s, CURRENT_DATE)", (title,))
    
    conn.commit()
    conn.close()
