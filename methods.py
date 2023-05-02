from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
      login_user = login #what am I doing
      return login
  elif request.method == 'GET':
       server_login_page = request.form.get('server_login_page') #weeping
       return server_login_page
       