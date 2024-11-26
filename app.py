from flask import Flask, render_template, request, redirect
from db import add_task, fetch_tasks, delete_task, mark_task_done, reset_tasks, import_previous_day_tasks
from datetime import datetime
import webview
from threading import Thread
from playsound import playsound  
import os


app = Flask(__name__, template_folder="./templates")


@app.route('/')
def index():
    tasks = fetch_tasks(datetime.today().date())
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    add_task(task)
    return redirect('/')


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    delete_task(task_id)
    #sound_path = os.path.join(os.path.dirname(__file__), 'sounds/erase.mp3')
    #playsound(sound_path)
    return redirect('/')


def done(task_id):
    mark_task_done(task_id)
    #sound_path = os.path.join(os.path.dirname(__file__), 'sounds/ding.mp3')
    #print(f"Playing sound from: {sound_path}")  
    #playsound(sound_path)  # Play the sound with absolute path
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    reset_tasks()
    return redirect('/')


@app.route('/import', methods=['POST'])
def import_tasks():
    import_previous_day_tasks()
    return redirect('/')


def run_flask():
    # Run the Flask app
    app.run(host="127.0.0.1", port=5000, debug=False)


def run_webview():
    # Run the PyWebView window
    webview.create_window("To-Do List App", "http://127.0.0.1:5000/")
    webview.start()


if __name__ == '__main__':
    # Start Flask and PyWebView in separate threads
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Start PyWebView in the main thread
    run_webview()
