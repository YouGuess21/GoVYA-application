from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ashwin@319",database="sql_college")
cursor=mydb.cursor()
app=Flask( __name__)
app.config['SECRET_KEY']='nokey'

class DataForm(FlaskForm): #We can create an object of this form
    text=StringField('Enter User ID:', render_kw={"id": "text"})
    password=StringField('Enter Password:', render_kw={"id": "password"})
    submit=SubmitField('Submit', render_kw={"id": "sub"})

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    cursor.execute("select * from user")
    value=cursor.fetchall()
    form=DataForm()
    return render_template('Login.html',data=value,form=form)

@app.route('/Customer')
def customer():
    welcome = request.args.get('Welcome', default='', type=str)
    userid = request.args.get('userID', default=0, type=int)
    if welcome:
        return render_template('Customer.html', Welcome=welcome,userid=userid)
    else:
        return redirect(url_for('unauth'))


@app.route('/admin')
def Admin():
    welcome = request.args.get('Welcome', default='', type=str)
    userid = request.args.get('userID', default=0, type=int)
    if welcome:
        return render_template('Admin.html', welcome=welcome, userid=userid)
    else:
        return redirect(url_for('unauth'))
    

@app.route('/Provider')
def provider():
    welcome = request.args.get('Welcome', default='', type=str)
    userid = request.args.get('userID', default=0, type=int)
    if welcome:
        return render_template('Provider.html', Welcome=welcome,userid=userid)
    else:
        return redirect(url_for('unauth'))

@app.route('/unauthorized_Access')
def unauth():
    return render_template('unauthacc.html')

@app.route('/User_selector', methods=['GET', 'POST'])
def user_selector():
    form = DataForm()
    if request.method == 'POST' and form.validate_on_submit():
        entered_userid = form.text.data
        form.text.data=""
        entered_pass=form.password.data
        form.password.data=""
        cursor.execute("select * from user")
        value=cursor.fetchall()
        for row in value:
            if (str(row[0])==entered_userid and str(row[1])==entered_pass):
                if(int(int(entered_userid)/1000)== 1):
                    return redirect(url_for('customer',Welcome="Welcome Customer "+entered_userid,userID=entered_userid))
                    #url_for(fn name,   )
                if(int(int(row[0])/1000)==2):
                    return redirect(url_for('Admin',Welcome="Welcome Admin "+entered_userid,userID=entered_userid))
                if(int(int(row[0])/1000)==3):
                    return redirect(url_for('provider',Welcome="Welcome Provider "+entered_userid,userID=entered_userid))
        return render_template('User_selector.html', Welcome='User Id or Password is Wrong')
    return render_template('user_selector',form=form)


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/cust_reg')
def cust_register():
    return render_template('Customer_register.html')

@app.route('/prov_reg')
def prov_register():
    return render_template('Provider_register.html')




if __name__=="__main__":
    app.run(debug=True)
