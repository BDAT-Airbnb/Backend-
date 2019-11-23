from flask import Flask, request

from service import ToDoService

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)


# app.py

@app.route("/todo", method=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())


