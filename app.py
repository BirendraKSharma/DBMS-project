from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
from datetime import datetime
import yaml
import MySQLdb.cursors

app = Flask(__name__)

# Load MySQL configuration from YAML
db_config = yaml.safe_load(open('db.yaml'))

# Configure MySQL
app.secret_key = 'abc123!@#'
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        due_date = request.form['dueDate']
        
        # Connect to MySQL and insert the task
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("INSERT INTO tasks (content,dueDate,date_created) VALUES (%s,%s,NOW())", (task_content,due_date))
        mysql.connection.commit()
        cur.close()
    return render_template('index.html')


@app.route('/show', methods=['GET'])
def show():
    # Connect to MySQL and fetch all tasks
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM tasks ORDER BY date_created DESC;")
    tasks = cur.fetchall()
    cur.close()

    # Render the template and pass the tasks to it
    return render_template('show.html', tasks=tasks)
 
    
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    # Connect to MySQL and delete the task
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()

    # Redirect to the index route
    return redirect('/')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    # Fetch the task to be updated
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM tasks WHERE id = %s", (id,))
    task = cur.fetchone()
    cur.close()
    
    if request.method == 'POST':
        new_content = request.form['content']
        new_due_date = request.form['dueDate']  # Retrieve the new due date from the form data
        
        # Connect to MySQL and update the task
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tasks SET content = %s, dueDate = %s WHERE id = %s", (new_content, new_due_date, id))
        mysql.connection.commit()
        cur.close()
        
        return redirect('/')
    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)
