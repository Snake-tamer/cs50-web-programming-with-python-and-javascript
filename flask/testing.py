from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

@app.route("/<string:name>")
def david(name):
    name = name.upper()
    return f"hello {name}"

app.run(debug=True)