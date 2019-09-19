from collections import defaultdict
import operator
from flask import Flask,render_template,request,session,logging,url_for,redirect,flash
from sqlalchemy import create_engine,and_
from sqlalchemy.orm import sessionmaker,scoped_session
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy
#from flask_whooshalchemy import wa
from sqlalchemy.sql import text
from flask_login import login_user, current_user, logout_user, login_required,LoginManager,UserMixin


engine=create_engine("mysql+pymysql://root:@localhost/register")
                    #(mysql)


db=scoped_session(sessionmaker(bind=engine))

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/register'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['WHOOSH_BASE']='whoosh'

db1=SQLAlchemy(app)

class Users(db1.Model, UserMixin):
    id = db1.Column(db1.Integer, primary_key=True)
    name = db1.Column(db1.String(20), unique=True, nullable=False)
    username= db1.Column(db1.String(120), unique=True, nullable=False)
    password = db1.Column(db1.String(60), nullable=False)

    def __iter__(self):
          for each in self.__dict__.keys():
              yield self.__getattribute__(each)

    def retuser(self):
        return self.name


    def __repr__(self):
        return f"User('{self.name}', '{self.username}')"

class Usersbook(db1.Model, UserMixin):
    id = db1.Column(db1.Integer, primary_key=True,autoincrement=True)
    username = db1.Column(db1.String(20), nullable=True,primary_key=True)
    bookname= db1.Column(db1.String(120), nullable=True)



    def __repr__(self):
        return f"Usersbook('{self.username}', '{self.bookname}')"


login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@app.route("/python",methods=['GET','POST'])
def python():
    db.execute(
                  text('UPDATE bookcn SET bookcount=bookcount+1 WHERE bookname="python"'))
    #print(current_user)
    t=current_user.retuser()
    print(t)
    user1=db.execute("SELECT bookname FROM usersbook WHERE username=:username AND bookname=:bookname",{'username':t,'bookname':'python'}).fetchone()
    print(user1)
    if user1 is None:
        db.execute("INSERT INTO usersbook(username,bookname) VALUES(:username,:bookname)",{'username':t,'bookname':'python'})
    db.commit()
    return render_template('python.html')




@app.route("/cpp",methods=['GET','POST'])
def cpp():
    db.execute(
                  text('UPDATE bookcn SET bookcount=bookcount+1 WHERE bookname="cpp"'))
    t=current_user.retuser()
    print(t)
    user1=db.execute("SELECT bookname FROM usersbook WHERE username=:username AND bookname=:bookname",{'username':t,'bookname':'cpp'}).fetchone()
    print(user1)
    if user1 is None:
        db.execute("INSERT INTO usersbook(username,bookname) VALUES(:username,:bookname)",{'username':t,'bookname':'cpp'})

    db.commit()
    return render_template('cpp.html')


@app.route("/javascript",methods=['GET','POST'])
def javascript():
    db.execute(
                  text('UPDATE bookcn SET bookcount=bookcount+1 WHERE bookname="javascript"'))
    t=current_user.retuser()
    print(t)
    user1=db.execute("SELECT bookname FROM usersbook WHERE username=:username AND bookname=:bookname",{'username':t,'bookname':'javascript'}).fetchone()
    print(user1)
    if user1 is None:
        db.execute("INSERT INTO usersbook(username,bookname) VALUES(:username,:bookname)",{'username':t,'bookname':'javascript'})
    db.commit()
    return render_template('javascript.html')

@app.route("/java",methods=['GET','POST'])
def java():
    db.execute(
                  text('UPDATE bookcn SET bookcount=bookcount+1 WHERE bookname="java"'))
    t=current_user.retuser()
    print(t)
    user1=db.execute("SELECT bookname FROM usersbook WHERE username=:username AND bookname=:bookname",{'username':t,'bookname':'javascript'}).fetchone()
    print(user1)
    if user1 is None:
        db.execute("INSERT INTO usersbook(username,bookname) VALUES(:username,:bookname)",{'username':t,'bookname':'javascript'})
    db.commit()
    return render_template('java.html')


@app.route("/alchemyst",methods=['GET','POST'])
def alchemyst():
    #db.execute("UPDATE bookcount SET bookcount=bookcount+1 WHERE bookname==:ab",ab=b)
    #db.execute("UPDATE book_cout1 SET alchemyst = alchemyst+1 ")
    db.execute(
                  text('UPDATE bookcn SET bookcount=bookcount+1 WHERE bookname="alchemyst"'))
    t=current_user.retuser()
    print(t)
    #user1 = Usersbook.query.filter_by(username==t & bookname=='alchemyst').first()
    user1=db.execute("SELECT bookname FROM usersbook WHERE username=:username AND bookname=:bookname",{'username':t,'bookname':'alchemyst'}).fetchone()
    print(user1)
    if user1 is None:
        db.execute("INSERT INTO usersbook(username,bookname) VALUES(:username,:bookname)",{'username':t,'bookname':'alchemyst'})
    db.commit()
    return render_template('alchemyst.html')


@app.route("/issue",methods=['GET','POST'])
def issue():
    if(request.method=='POST'):
        search=request.form.get('search')
        db.execute("UPDATE book SET quantity = quantity-1 WHERE bookname=:search",{'search':search})
        db.commit()
    return render_template('issue.html')


@app.route("/admin_book_search",methods=['GET','POST'])
def admin_book_search():
    l={'bookname':'','author':'','quantity':'','section':'','serial_no':''}
    if(request.method=='POST'):
        search=request.form.get('search')
        username_data=db.execute("SELECT * FROM book WHERE bookname=:search",{'search':search}).fetchone()
        if username_data is None:
            flash('no book of this name is available here we will try to add it','danger')
            db.execute("INSERT INTO book_req(name) VALUES(:username_data)",{'username_data':username_data})
            db.commit()
            return render_template('admin_book_search.html',l1=l)
        else:
            l['bookname']=username_data[0]
            l['author']=username_data[1]
            l['quantity']=username_data[2]
            l['section']=username_data[3]
            l['serial_no']=username_data[4]
            return render_template('admin_book_search.html',l1=l)
    return render_template('admin_book_search.html',l1=l)

@app.route("/")
def home():

    return render_template('home.html')






@app.route("/admin_insert_book",methods=['GET','POST'])

def admin_insert_book():
    if(request.method=='POST'):

        bookname=request.form.get('bookname')
        author=request.form.get('author')
        quantity=request.form.get('quantity')
        section=request.form.get('section')
        serial_no=request.form.get('serial_no')
        #db.execute("INSERT INTO Ibook(bookname) VALUES(:bookname)",{'bookname':bookname})

        db.execute("INSERT INTO bookcn(bookname) VALUES(:bookname)",{'bookname':bookname})
        db.execute("INSERT INTO book(bookname,author,quantity,section,serial_no) VALUES(:bookname,:author,:quantity,:section,:serial_no)",
            {'bookname':bookname,'author':author,'quantity':quantity,'section':section,'serial_no':serial_no})

        connection.commit()
        db.commit()
        flash('book inserted successfully','success')
    return render_template('admin_insert_book.html')




@app.route("/admin_after_login",methods=['GET','POST'])
def admin_after_login():

    return render_template('admin_after_login.html')

@app.route("/user_after_login",methods=['POST','GET'])
def user_after_login():
    if(request.method=='POST'):
        try:
            search=request.form.get('search')
            db.execute("UPDATE book SET quantity = quantity+1 WHERE bookname=:search",{'search':search})
            db.commit()
        except:
            search=request.form.get('search1')
            db.execute("UPDATE book SET quantity = quantity+1 WHERE bookname=:search",{'search':search})
            db.commit()

    return render_template('user_after_login.html',post1=post)


@app.route("/admin",methods=['GET','POST'])
def admin():
    if(request.method=='POST'):
        username=request.form.get('name')
        password=request.form.get('password')
        username_data=db.execute("SELECT username FROM usersadmin WHERE username=:username",{'username':username}).fetchone()
        password_data=db.execute("SELECT password FROM usersadmin WHERE username=:username",{'username':username}).fetchone()
        if username_data is None:
            flash('no username','danger')
            return render_template('admin.html')
        else:
            if(password==password_data[0]):
                flash('you are now login','success')
                return redirect(url_for('admin_after_login'))
            else:
                flash('incorrect password','danger')
                return render_template('admin.html')
    return render_template('admin.html')

@app.route("/registers",methods=['GET','POST'])
def registers():
    if(request.method=='POST'):
        name=request.form.get('name')
        username=request.form.get('username')
        password=request.form.get('password')
        confirm=request.form.get('confirm')
        #secure_password=sha256_crypt.encrypt(str(password))
        if password==confirm:
            db.execute("INSERT INTO users(name,username,password) VALUES(:name,:username,:password)",
                {'name':name,'username':username,'password':password})
            #db.execute()
            db.commit()
            flash('you can login now','success')
            return redirect(url_for('login'))
        else:
            flash('password does not match','danger')
            return render_template('registers.html')
    return render_template('registers.html')

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('name')
        password=request.form.get('password')
        username_data=db.execute("SELECT username FROM users WHERE username=:username",{'username':username}).fetchone()
        password_data=db.execute("SELECT password FROM users WHERE username=:username",{'username':username}).fetchone()
        user = Users.query.filter_by(username=username).first()
        if username_data is None:
            flash('no username','danger')
            return render_template('login.html')
        else:
            if(password==password_data[0]):
                login_user(user)
                return redirect(url_for('before_issue'))
                '''
                flash('you are now loged in as '+username,'success')
                l=db.execute("SELECT * FROM bookcn").fetchall()
                l.sort(key=lambda x: x[1],reverse=True)
                next=request.args.get('next')
                #return redirect(next or url_for('before_issue'))
                return render_template('before_issue.html', l1=l)
                #return render_template('before_issue.html',username1=username,l1=l)
                '''
            else:
                flash('incorrect password','danger')
                return render_template('login.html')
    return render_template('login.html')




@app.route('/before_issue')
def before_issue():
    if current_user.is_authenticated:
        rmdata=db.execute("SELECT * FROM usersbook").fetchall()
        g=defaultdict(list)
        for it in rmdata:
            g['{}'.format(it[1])].append(it[2])
        #g will be use in future to make a dataset for apriori algorithm for recomendation
        l=db.execute("SELECT * FROM bookcn").fetchall()
        l.sort(key=lambda x: x[1],reverse=True)
        return render_template('before_issue.html', l1=l)
    return redirect(url_for('login'))




@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('login')


if(__name__=='__main__'):
    app.secret_key="123456daily"
    app.run(debug=True)
