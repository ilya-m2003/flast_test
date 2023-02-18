from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def new_command():
  return "<h1> Получилось. Молодец! </h1>"
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)