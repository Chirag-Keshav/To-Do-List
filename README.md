# 📝 Daily To-Do List App

A simple and efficient daily To-Do List application designed to help you manage and track your daily tasks effortlessly. Built with **Flask**, **HTML/CSS**, and integrated with a **MySQL** database, this app offers a seamless user experience and customizable features.

---

## 🚀 Features

- 🕒 **Daily Reset**: Automatically resets the task list every 24 hours.
- ✅ **Task Management**: Add, edit, delete, and mark tasks as done.
- 🔄 **Carry Over Tasks**: Option to import unfinished tasks from the previous day.
- 💬 **Motivational Message**: Get a congratulatory message upon completing all tasks.
- 🎨 **Clean UI**: Responsive and user-friendly interface with custom styling.

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: MySQL
- **Desktop Integration**: PyWebView (for native desktop app support)
- **Packaging**: PyInstaller (to generate `.exe` file)


## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/todo-list-app.git
cd todo-list-app
```

### 2. Install Dependencies
Ensure you have Python 3.10+ installed, and then install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Configure the Database
Create a MySQL database and update the `db.py` file with your database credentials:
```python
db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "todo_db"
}
```
Run the script to initialize the database:
```bash
python db.py
```

### 4. Run the Application
Start the Flask server:
```bash
python app.py
```
Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 💻 Desktop Version
The app can run as a native desktop application using **PyWebView**. To build the `.exe` file:
```bash
pyinstaller --onefile app.py
```
For a desktop-like experience, the app opens in a PyWebView window.

---

## 📂 Project Structure
```
├── app.py               # Main Flask application
├── db.py                # Database initialization and operations
├── templates/           # HTML templates
│   └── index.html       # Main To-Do List page
├── static/              # Static files (CSS, JS, images)
│   └── style.css        # Custom styles
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

---

## 🎉 How It Works

1. **Add Tasks**: Start your day by adding tasks to the list.
2. **Mark as Done**: Check off completed tasks.
3. **Carry Over Tasks**: Optionally import tasks from the previous day.
4. **Motivational Message**: Get inspired to maintain a streak of daily task completion!

---

## 📜 License

This project is licensed under the MIT License. Feel free to fork, modify, and use it in your projects.

---

## 🙌 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

---

## 📧 Contact

For any inquiries or suggestions, reach out to:
- **Email**: chiragkeshav.ck@gmail.com
- **GitHub**: [Chirag Keshav](https://github.com/Chirag-Keshav)

