from flask import Flask,render_template,request,redirect,url_for,flash
from config import config
from flask_mysqldb import MySQL
from config import config
#importacion para el login 
from flask_login import LoginManager,login_user,logout_user,login_required

#Models
from models.ModelUser   import ModelUser
#entities
from models.entities.User  import User


app=Flask(__name__)


db=MySQL(app)
login_manager_app=LoginManager(app)



@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        #el id se lo paso porque es obligatorio en el constructor 
        user=User(0,username,password)


        logged_user=ModelUser.login( db, user)

        if logged_user:
            if logged_user.password:
                login_user(logged_user)

                return redirect(url_for('home'))
            else:
                flash('INVALID PASSWORD')
                return render_template('auth/login.html')
        else:
            flash('user no encontrado')
            return render_template('auth/login.html')
    
    else:

        return render_template('auth/login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def index():
    return redirect(url_for('login'))

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run()
