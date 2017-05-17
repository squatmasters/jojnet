from flask import Flask, render_template
app = Flask(__name__)

url_for('static', 'main.css')

@app.route("/")
def hello():
  return "jojnet"

@app.route("/user/<username>")
def showUser(username):
  return render_template('profile.html', un=username)

@app.route("/about/")
def about():
  return "JOJNET is the hip new social network."

if __name__ == "__main__":
  app.run(host='0.0.0.0')
