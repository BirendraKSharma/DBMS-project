# DBMS Project: ToDo List (CRUD App with MySQL)

This is a simple ToDo list application built as a final project for the 6th semester Database Management Systems (DBMS) course. The app demonstrates basic CRUD (Create, Read, Update, Delete) operations using Python Flask for the backend and MySQL as the database.

## Features

- Add new tasks with a due date
- View all tasks
- Update existing tasks
- Delete tasks
- Simple, clean HTML interface

## Technology Stack

- **Backend:** Python (Flask)
- **Database:** MySQL
- **Frontend:** HTML (Jinja2 templates), CSS (inline)
- **ORM/DB Middleware:** Flask-MySQLdb
- **Configuration:** YAML for DB connection

## Project Structure

```
DBMS-project/
│
├── app.py                # Main Flask application (CRUD routes)
├── db.yaml               # Database configuration (YAML)
├── reqquirements.txt     # Python dependencies
├── templates/
│   ├── index.html        # Home page: add/view tasks
│   ├── show.html         # List all tasks
│   └── update.html       # Update a task
└── LICENSE               # MIT License
```

## Getting Started

### Prerequisites

- Python 3.x
- MySQL server
- Required Python packages (see `reqquirements.txt`)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/BirendraKSharma/DBMS-project.git
   cd DBMS-project
   ```

2. **Install dependencies:**
   ```sh
   pip install -r reqquirements.txt
   ```

3. **Configure MySQL:**
   - Create a database in MySQL (e.g., `todo_db`).
   - Update `db.yaml` with your MySQL credentials:
     ```yaml
     mysql_host: 'localhost'
     mysql_user: 'your_user'
     mysql_password: 'your_password'
     mysql_db: 'todo_db'
     ```

4. **Create the tasks table:**
   ```sql
   CREATE TABLE tasks (
       id INT AUTO_INCREMENT PRIMARY KEY,
       content TEXT NOT NULL,
       dueDate DATE,
       date_created DATETIME DEFAULT CURRENT_TIMESTAMP
   );
   ```

5. **Run the app:**
   ```sh
   python app.py
   ```
   The app will be available at `http://localhost:5000/`.

## Usage

- **Add Task:** Enter task content and due date on the home page, then submit.
- **View Tasks:** Click "Show Tasks" to see all tasks.
- **Update Task:** Click "Update" next to a task, edit, and save.
- **Delete Task:** Click "Delete" next to a task.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

*Project by Birendra Kumar Sharma*