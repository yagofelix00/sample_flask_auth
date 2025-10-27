from flask import Flask, request, jsonify
from models.user import User
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
@app.route('/login', methods="POST")
def login():
    data = request.json 
    username = data.get("username")
    password = data.get("password")

    if username and password:
        # Login
        pass

    return jsonify({"message": "Credenciais Inválidas"}), 400


@app.route("/hello-world", methods=['GET'])
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)