from flask import Flask,render_template,request,redirect,url_for
from config import config
from flask_mysqldb import MySQL
from config import config


app=Flask(__name__)


db=MySQL(app)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
        return 'datos procesados '
    
    else:

     return render_template('auth/login.html')

@app.route('/')
def index():
   return redirect(url_for('login'))

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run(debug=True)
