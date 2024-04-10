from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"

# Creating a database instance
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False) 
    desc = db.Column(db.String(200), nullable=False)  
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/')
def hello_world():
    todo = Todo(title="First Todo", desc="Start investing in Stock Market")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')
    #return 'Hello, World!!'

@app.route('/products')
def products():
    return 'This is the product page'

if __name__ == "__main__":
    # Creating database tables
    with app.app_context():
        db.create_all()
    
    # Running the Flask application
    app.run(debug=True, port=8000)
