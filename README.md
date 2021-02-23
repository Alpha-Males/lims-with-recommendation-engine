# lims-with-recommendation-engine(SDL mini project)
      
   A LIMS(library information management system) which recommends book using apriori algorithm.
      
      
The mini project was completed in the third year in SDL Lab by our team

**Prerequisites**
------------------
Install dependencies using ``pip3 install -r requirements.txt``

start mysql using ``service mysql start`` and create database by the name of ``'lims'`` and import database using

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

** Our Approach of recommender engine **
----------------------------------------
The algorithm used in the recommendation has taken its inspiration from market basket analysis.
further explaination of this market basket analysis:
- if a user buy milk in a grocery store then he/she also buy bread and some other products,so this is a transation
- if several users in the grocery store buy milk and bread,
- now the algorithm will check all the transactions and will found out that several users who buy milk also buy bread
- if a new user come to store the Apriori Algorithm will recommend the user to buy bread if he/she buy mil as it has been preferred the a huge set of community.

Inspiration goes like this:

-  firstly a window of time was kept to watch the transaction(books read by the user in the given window) happened
-  then consider that if there were 'n' transaction happened i.e 'n' no of users issued the books in the given window and each issue on books on a particular day was ammended into the transactions.
- Consider there the 100 transactions happened in the given window and 4 books are common in the transactions which are('Joy of computing with python','DSA','ML','ADS')
- then if a new user comes and issue a DSA book then he/she will also be recommended the other three books('Joy of computing with python','ML','ADS')


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


