from flask import Flask,render_template,request,session,logging,url_for,redirect,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy
#from flask_whooshalchemy import wa



engine=create_engine("mysql+pymysql://root:@localhost/register")
                    #(mysql)


db=scoped_session(sessionmaker(bind=engine))



app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/register'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['WHOOSH_BASE']='whoosh'

#db1=SQLAlchemy(app)

post='now you can use the library'

@app.route("/count",methods=['GET','POST'])
def count():
    db.execute("UPDATE cc SET c = c+1 ")
    db.commit()
    return render_template('count.html')

@app.route("/cpp",methods=['GET','POST'])
def cpp():
    db.execute("UPDATE book_cout1 SET cpp = cpp+1 ")
    db.commit()
    return render_template('cpp.html')


@app.route("/javascript",methods=['GET','POST'])
def javascript():
    db.execute("UPDATE book_cout1 SET javascript = javascript+1 ")
    db.commit()
    return render_template('javascript.html')

@app.route("/java",methods=['GET','POST'])
def java():
    db.execute("UPDATE book_cout1 SET java = java+1 ")
    db.commit()
    return render_template('java.html')


@app.route("/alchemyst",methods=['GET','POST'])
def alchemyst():

    db.execute("UPDATE book_cout1 SET alchemyst = alchemyst+1 ")
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
            db.execute("INSERT INTO book_reuired(book_name) VALUES(:username_data)",{'username_data':username_data})
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





@app.route("/admin_after_login",methods=['GET','POST'])
def admin_after_login():

    if(request.method=='POST'):

        bookname=request.form.get('bookname')
        author=request.form.get('author')
        quantity=request.form.get('quantity')
        section=request.form.get('section')
        serial_no=request.form.get('serial_no')

        db.execute("INSERT INTO book(bookname,author,quantity,section,serial_no) VALUES(:bookname,:author,:quantity,:section,:serial_no)",
            {'bookname':bookname,'author':author,'quantity':quantity,'section':section,'serial_no':serial_no})
        db.commit()
        flash('book inserted successfully','success')
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
        if username_data is None:
            flash('no username','danger')
            return render_template('login.html')
        else:
            if(password==password_data[0]):
                flash('you are now loged in as '+username,'success')
                l=db.execute("SELECT * FROM book_cout1").fetchone()
                dict1={"cpp":l[0],
                        "java":l[1],
                        "javascript":l[2],
                        "alchemyst":l[3]
                }
                dict2=sorted(dict1.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
                return render_template('before_issue.html',username1=username,l1=dict2)
                #return redirect(url_for('issue'))
            else:
                flash('incorrect password','danger')
                return render_template('login.html')

    return render_template('login.html')


if(__name__=='__main__'):
    app.secret_key="123456daily"
    app.run(debug=True)
