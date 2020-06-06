# flask_web_App
==============
      
      
      A LIMS(library information management system) which recommends book using apriori algorithm.
      
      


      
      
**Prerequisites**
------------------
Install dependencies using pip3 install -r requirements.txt

start mysql using service mysql start and import database using

``mysql -u root -p lims < dbexport.sql``


grant privilage to user root to access database lims using following :
----------------------------------------------------------------------------
```
$ sudo mysql -u root # for new installation

mysql> USE mysql;
mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
mysql> FLUSH PRIVILEGES;
mysql> exit;

$ service mysql restart
```
If your MySql is set with your password
----------------------------------------------------------------------------
```
$ sudo mysql -u root -p

- Then grant privilage using the above statements.<br>
- Provide your MySql root password into __init__.py file ; # mysql+pymysql://root:your_password@localhost/lims<br>
- $ service mysql restart
```
-----------------------------------------------------------------------------
<br>
if problem persists refer
<br>
https://stackoverflow.com/questions/39281594/error-1698-28000-access-denied-for-user-rootlocalhost


**using** 
--------  

    git clone https://github.com/lims-with-autorecommendation/flask_web_App
    cd flask_web_App
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    open the teminal and fire ``python3 run.py``    
    
    
**TODO**
---------
- [ ] Redirect issue when issuing  and returning book but can be sloved easily by refactoring account route. 
- [ ] variable names must be changed for readabiliy, maintainability and Understandability. 
- [ ] Code should be refactored to reduce number of html page in template folder.
- [ ] Make a single route for all the book and which works on addition of any book in future.
- [ ] Design better schema for database.
- [ ] Remove dependency from sqlalchemy ORM and therefore dependent code should be proted to flask-sqlalchmey.
- [ ] Better UI for account page .
- [ ] Improve Reccommendation by merging collaboration filtering,decision tree and content based methods.


**Contributing**
----------------
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


