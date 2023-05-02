from flask import Flask, request
app = Flask(__name__)

@app.route('/user', methods=['GET','POST'])
def get_user():
    username = request.form['username']
    password = request.form['password']
    #login(arg,arg) is a function that tries to log in and returns true or false
    status = login(username, password)
    return status