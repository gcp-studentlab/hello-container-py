from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, from inside thsae pull request application!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
