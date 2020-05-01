from collections import defaultdict
import operator
from collections import defaultdict
from datetime import date
import csv
import sys

from flask import Flask,render_template,request,session,logging,url_for,redirect,flash

from sqlalchemy import create_engine,and_
from sqlalchemy.orm import sessionmaker,scoped_session

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_login import login_user, current_user, logout_user, login_required,LoginManager,UserMixin

from app.model import Users,Usersbook
from app import db,db1,app




login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


def process(bookname,number,t):
    csv_file = csv.reader(open('pair.csv', "r"), delimiter="|")

    l1=set()
    #loop through csv list
    for row in csv_file:
        #if current rows 2nd value is equal to input, print that row
        for s1 in row:
            if(s1==number[0]):
                for i in row:
                    l1.add(i)
    l=list(l1)
    info=[]
    for i in range(len(l)):
        g=db.execute('SELECT * FROM book WHERE serial_no=:serial_no',{'serial_no':l[i]}).fetchone()
        info.append(g)
    db.execute(
                  text('UPDATE bookcn SET bookcount=bookcount+1 WHERE bookname="{}"'.format(bookname)))


    db.execute(
                  text('UPDATE usersbook SET bookcount=bookcount+1 WHERE bookname="CN" AND username=:username'),{'username':t})
    user1=db.execute("SELECT bookname FROM usersbook WHERE username=:username AND bookname=:bookname",{'username':t,'bookname':bookname}).fetchone()
    print(user1)
    if user1 is None:
        db.execute("INSERT INTO usersbook(username,bookname) VALUES(:username,:bookname)",{'username':t,'bookname':bookname})
    db.commit()
    return info
 

@app.route("/python",methods=['GET','POST'])
def python():
    t=current_user.retuser()
    l=request.args.get('my_var')
    print(l)
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()
    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'python'}).fetchone()
    info=process('python',number,t)



    #input number you want to search
    #number = input('Enter number to find\n')

    #read csv, and split on "," the line
    return render_template('python.html',info=info)



@app.route("/cpp",methods=['GET','POST'])
def cpp():
    t=current_user.retuser()
    l=request.args.get('my_var')
    print(l)
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()

    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'cpp'}).fetchone()
    info=process('cpp',number,t)
    return render_template('cpp.html',info=info)


@app.route("/javascript",methods=['GET','POST'])
def javascript():
    t=current_user.retuser()
    l=request.args.get('my_var')
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()
    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'javascript'}).fetchone()



    info=process('javascript',number,t)

    return render_template('javascript.html',info=info)

@app.route("/java",methods=['GET','POST'])
def java():
    t=current_user.retuser()
    l=request.args.get('my_var')
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()
    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'java'}).fetchone()
    info=process('java',number,t)
    return render_template('java.html',info=info)


@app.route("/alchemyst",methods=['GET','POST'])
def alchemy():
    t=current_user.retuser()
    l=request.args.get('my_var') # var l deals only with cart and issue
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()
    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'alchemyst'}).fetchone()
    #db.execute("UPDATE bookcount SET bookcount=bookcount+1 WHERE bookname==:ab",ab=b)
    #db.execute("UPDATE book_cout1 SET alchemyst = alchemyst+1 ")
    info=process('alchemyst',t)
    return render_template('alchemyst.html',info=info)

@app.route("/CN",methods=['GET','POST'])
def CN():
    t=current_user.retuser()
    l=request.args.get('my_var')
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()
    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'CN'}).fetchone()
    info=process('CN',number,t)
    return render_template('CN.html',info=info)

@app.route("/DBMS",methods=['GET','POST'])
def DBMS():
    t=current_user.retuser()
    l=request.args.get('my_var')
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()
    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'DBMS'}).fetchone()

    info=process('DBMS',number,t)
    return render_template('DBMS.html',info=info)

@app.route("/CG",methods=['GET','POST'])
def CG():
    t=current_user.retuser()
    l=request.args.get('my_var')
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()
    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'CG'}).fetchone()

    info=process('CG',number,t)
    return render_template('CG.html',info=info)

@app.route("/ADS",methods=['GET','POST'])
def ADS():
    t=current_user.retuser()
    l=request.args.get('my_var')
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()

    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'ADS'}).fetchone()

    info=process('ADS',number,t)
    return render_template('ADS.html',info=info)

@app.route("/DS",methods=['GET','POST'])
def DS():
    t=current_user.retuser()
    l=request.args.get('my_var')
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()

    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'DS'}).fetchone()
    info=process('DS',number,t)

    return render_template('DS.html',info=info)

@app.route("/SEPM",methods=['GET','POST'])
def SEPM():
    t=current_user.retuser()
    l=request.args.get('my_var')
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()

    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'SEPM'}).fetchone()

    info=process('SEPM',number,t)
    return render_template('SEPM.html',info=info)

@app.route("/ISEE",methods=['GET','POST'])
def ISEE():
    t=current_user.retuser()
    l=request.args.get('my_var')
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()
    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'ISEE'}).fetchone()

    info=process('ISEE',number,t)
    return render_template('ISEE.html',info=info)

@app.route("/ml",methods=['GET','POST'])
def ml():
    t=current_user.retuser()
    l=request.args.get('my_var')
    if(l!=None):
        rec=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l}).fetchone()
        if(rec==None):
            db.execute("INSERT INTO userscart(bookname,username) VALUES(:bookname,:username)",{'bookname':l,'username':t})
            db.commit()
    number=db.execute("SELECT serial_no FROM book WHERE bookname=:bookname",{'bookname':'ml'}).fetchone()
    #db.execute("UPDATE bookcount SET bookcount=bookcount+1 WHERE bookname==:ab",ab=b)
    #db.execute("UPDATE book_cout1 SET ml = ml+1 ")
    info=process('ml',number,t)
    return render_template('ml.html',info=info)




@app.route("/admin_book_search",methods=['GET','POST'])
def admin_book_search():
    l={'bookname':'','author':'','quantity':'','section':'','serial_no':'','issuedby':''}
    if(request.method=='POST'):
        search=request.form.get('search')
        username_data=db.execute("SELECT * FROM book WHERE bookname=:search",{'search':search}).fetchone()
        issuedby_data=db.execute("SELECT username FROM issue WHERE bookname=:bookname",{'bookname':search}).fetchall()
        size=int(len(issuedby_data))
        if username_data is None:
            flash('no book of this name is available here we will try to add it','danger')
            #db.execute("INSERT INTO book_req(name) VALUES(:username_data)",{'username_data':username_data})
            #db.commit()
            return render_template('admin_book_search.html',l1=l)
        else:
            l['bookname']=username_data[1]
            l['author']=username_data[2]
            l['quantity']=username_data[3]
            l['section']=username_data[4]
            l['serial_no']=username_data[5]
            l['issuedby']=issuedby_data
            return render_template('admin_book_search.html',l1=l,size=size)

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

        #connection.commit()
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
        user_data=db.execute("SELECT username FROM users WHERE username=:username",{'username':username}).fetchone()
        if user_data is not  None:
            flash('username already available please use some other','danger')
        else:
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
        #g will be use in future to make a dataset for apriori algorithm for recomendation


        l=db.execute("SELECT * FROM bookcn").fetchall()
        l.sort(key=lambda x: x[1],reverse=True)
        l2=l[0:6]
        print(l2)
        return render_template('before_issue.html', l1=l2)
    return redirect(url_for('login'))

@app.route("/account")
def account():
    t=current_user.retuser()
    data=db.execute("SELECT bookname FROM userscart WHERE username=:username",{'username':t}).fetchall()
    #print(data)
    today = date.today()
    print(today)
    l2=request.args.get('my_var1')
    rec=db.execute("SELECT bookname FROM issue WHERE bookname=:bookname AND username=:username",{'bookname':l2,'username':t}).fetchone()
    count=db.execute("SELECT count(bookname) FROM issue WHERE username=:username",{'username':t}).fetchone()
    if(count[0]>3):
        flash('you are not allowed to issue more than four book','danger')
    elif(rec==None and l2!=None):
        db.execute("INSERT INTO issue(username,issuedate,bookname) VALUES(:username,:issuedate,:bookname)",
                        {'username':t,'issuedate':today,'bookname':l2})
        db.execute("UPDATE book SET quantity = quantity-1 WHERE bookname=:search",{'search':l2})
                #db.execute()
        db.commit()
    data1=db.execute("SELECT bookname FROM userscart WHERE bookname=:bookname",{'bookname':l2}).fetchone()
    if(data!=None and rec!=None):
        db.execute("DELETE FROM userscart WHERE bookname=:bookname",{'bookname':l2})
        db.commit()
    data1=db.execute("SELECT bookname FROM issue WHERE username=:username",{'username':t}).fetchall()
    ret_book=request.args.get('my_var2')

    if(ret_book!=None):
        db.execute("DELETE FROM issue WHERE username=:username AND bookname=:bookname",{'username':t,'bookname':ret_book})
        db.execute("UPDATE book SET quantity = quantity+1 WHERE bookname=:search",{'search':ret_book})
        db.commit()
    return render_template('account.html',data=data,data1=data1)



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')



