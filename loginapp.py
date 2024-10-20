from flask import Flask,render_template,request
import os
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('loginindex.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method =='POST':
        if request.form['name']== 'user' and request.form['password']== 'deepak':
            return render_template('dashboard.html')
        else:
            error= "wrong user / password"
            return render_template('login.html',error=error)

    else:
        return render_template('login.html')
    
    


app.add_url_rule('/home','home',home)
if __name__=='__main__':
    app.run(debug=True)