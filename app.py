from flask import Flask, render_template, request
app = Flask(__name__)
valid_username = "admin"
valid_password = "password"

@app.route('/')
def home():
  return render_template('Login.html')

@app.route('/Login', methods=['post'])
def login():
  username = request.form['username']
  password = request.form['password']
  if username == valid_username and password == valid_password:
    return f"Wlcomw {username}"
  else:
    return "Please enter a valid username and password"

if __name__ == '__main__':
  app.run(debug = True)