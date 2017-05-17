from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  return "jojnet"

@app.route("/user/<username>")
def showUser(username):
  return render_template('profile.html', un=username)

@app.route("/about/")
def aboub():
  return "jojent is hepatitis c"

if __name__ == "__main__":
  app.run(host='0.0.0.0')
