from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

with app.app_context():
    db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{id} - {self.body} created at {self.date_created}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task_body']
        print(task)
        new_task = Todo(body=task)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "ERROR"

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        print(tasks)
        return render_template('index.html', tasks=tasks)

if __name__ == "__name__":
    app.run(debug=True)
