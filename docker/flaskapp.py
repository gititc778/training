#install flask before running
#pip3 install flask
#pip3 list | grep flask
#pip3 show flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Dockerized Flask App!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)