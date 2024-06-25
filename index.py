from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def func():
    return "project is working"
if __name__ == "__main__":
    app.debug = True
    app.run()