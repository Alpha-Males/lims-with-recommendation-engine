# flask_web_App
==============
      
      
      A LIMS(library information management system) which recommends book using apriori algorithm.
      
      


      
      
**Prerequisites**
------------------
Install flask and 2 of its extensions flask-sqlalchemy and flask-login 
Install An ORM sqlalchemy




**using** 
--------  

    git clone https://github.com/lims-with-autorecommendation/flask_web_App
    cd flask_web_App
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    open the teminal and fire ``python3 run.py``    
    
    
**TODO**
---------
- [ ] Redirect issue when issuing book from cart. 
- [ ] Code should be refactored to reduce number of html page in template folder.
- [ ] Make a single route for all the book and which works on addition of any book in future.
- [ ] Design better schema for database.
- [ ] Remove dependency from ORM sqlalchemy dependent code should be proted to flask-sqlalchmey.


**Contributing**
----------------
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


