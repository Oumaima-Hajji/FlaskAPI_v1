from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/<name>')
def print_name(name):
    return f"Hi , {name} "


if __name__ == "__main__":
    app.run(debug=True)


