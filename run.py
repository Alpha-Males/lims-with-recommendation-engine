from app import app



if(__name__=='__main__'):
    app.secret_key="123456daily"
    app.run(debug=True,port=8082)
