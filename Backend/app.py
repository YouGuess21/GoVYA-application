from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ashwin@319",database="sql_college")
cursor=mydb.cursor()
app=Flask( __name__)
app.config['SECRET_KEY']='nokey'

class DataForm(FlaskForm): #We can create an object of this form
    text=StringField('Enter User ID:', render_kw={"id": "text"})
    password=StringField('Enter Password:', render_kw={"id": "password"})
    #Convert in end above is for ease of access while debugging
    #password=PasswordField('Enter Password:', render_kw={"id": "password"})
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

@app.route('/cust_funct',methods=['GET', 'POST'])
def CustomerFunction():
    if request.method == 'POST':
        user_id= request.form.get("user_id", default=0, type=int)
        todo=request.form.get('todo', default=0,type=int)
        if(todo==1):
            cursor.execute("select c_ID,name,email,c_homeaddr,c_phoneNo from user join customer on user_ID=c_id where user_id=%s",(user_id,))
            userdata=cursor.fetchone() 
            #used fetchone because only one output would be there
            #didn't check wether it occured or not as it will definitely exist as we are inside it's login page
            return render_template('Cust_funct.html',userid=user_id,user_data=userdata,funct=1)
    return redirect(url_for('unauth'))

@app.route('/Customer',methods=['GET', 'POST'])
def customer():
    uname = request.args.get('Username', default='', type=str)
    userid = request.args.get('userID', default=0, type=int)
    if uname:
        return render_template('Customer.html', username=uname,userid=userid)
    else:
        return redirect(url_for('unauth'))


@app.route('/admin',methods=['GET','POST'])
def Admin():
    uname = request.args.get('Username', default='', type=str)
    userid = request.args.get('userID', default=0, type=int)
    if uname:
        return render_template('Admin.html', username=uname, userid=userid)
    else:
        return redirect(url_for('unauth'))



@app.route('/admin_funct',methods=['GET','POST'])
def Admin_fun():
    if request.method == 'POST':
        username = request.form.get('user_name', default='', type=str)
        userid = request.form.get('user_id', default=0, type=int)
        todo=request.form.get('todo', default=0,type=int)
        provid = request.form.get('p_id', default=0, type=int)
        if username:
            if todo==1:
                cursor.execute('SELECT  * from provider where not verified')
                val=cursor.fetchall()
                return render_template('admin_funct.html', username=username, userid=userid,cur=val,flag=True)

            elif todo==2:
                cursor.execute('SELECT  * from orders')
                val=cursor.fetchall()
                return render_template('admin_funct.html', username=username, userid=userid,cur=val,cur2=val,funct=2)

            elif todo==3:
                cursor.execute('select * from employee')
                val=cursor.fetchall()
                cursor.execute('select * from emp_Phoneno')
                val2=cursor.fetchall()
                return render_template('admin_funct.html', username=username, userid=userid,cur=val,cur2=val2,funct=3)
                
            elif todo==4:
                cursor.execute('SELECT  * from provider where not verified')
                val=cursor.fetchall()
                for i in val:
                    if(provid==i[0]):
                        cursor.execute('update provider set verified=true where p_id=%s',(int(provid),))
                        mydb.commit()
                        cursor.execute('SELECT  * from provider where not verified')
                        val2=cursor.fetchall()
                        return render_template('admin_funct.html', username=username, userid=userid,success="Provider with Id:"+str(provid)+" is verified",cur=val2)
                    
                cursor.execute('SELECT  * from provider where not verified')
                val2=cursor.fetchall()
                return render_template('admin_funct.html', username=username, userid=userid,success="Provider with Id:"+str(provid)+" is already verified or it doesn't Exist",cur=val2) 
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
                    name=row[2]
                    return redirect(url_for('customer',Username=name,userID=entered_userid))
                    #url_for(fn name,   )
                if(int(int(row[0])/1000)==2):
                    name=row[2]
                    return redirect(url_for('Admin',Username=name,userID=entered_userid))
                if(int(int(row[0])/1000)==3):
                    name=row[2]
                    return redirect(url_for('provider',Welcome="Welcome Provider "+name,userID=entered_userid))
        return render_template('User_selector.html', Welcome='User Id or Password is Wrong')
    return redirect(url_for('unauth'))


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/cust_reg', methods=['GET', 'POST'])
def cust_register():
    if request.method=="POST":
        name = request.form.get("name")
        num = request.form.get("pno") #name is the value in name attribute
        email=request.form.get("email")
        home=request.form.get("home")
        passwd=request.form.get("pass")
        conf=request.form.get("conf")
        cursor.execute("Select max(user_ID) from user where user_id between 1000 and 1999")
        id=cursor.fetchone()[0]
        c_id=int(id)+1
        cursor.execute("Select email from user")
        cur=cursor.fetchall()
        for i in cur:
            if(i and email==i[0]):
                return redirect(url_for('cust_register',Success="Email Already Exists,Retry?"))

        if(passwd==conf):
            cursor.execute("insert into user(user_ID,password,name,email) values(%s,%s,%s,%s)",(c_id,passwd,name,email))
            mydb.commit()
            cursor.execute("insert into customer(c_id,c_homeaddr,c_phoneNo) values(%s,%s,%s)",(c_id,home,num))
            mydb.commit()
            return redirect(url_for('cust_register',Success="Success Account Created:"+str(name) +" User Id:" +str(c_id)))
        else:
            return redirect(url_for('cust_register',Success="Passwords Do not match?"))

    success_message = request.args.get('Success', default='', type=str) #when redirected from above(not a post request)
    return render_template('Customer_register.html',Success=success_message)

@app.route('/prov_reg',methods=['GET', 'POST'])
def prov_register():
    if request.method=="POST":
        name = request.form.get("name")
        num = request.form.get("pno") #name is the value in name attribute
        email=request.form.get("email")
        office=request.form.get("office")
        scale=request.form.get("scale")
        pan = request.form.get("pan")
        gst = request.form.get("gst")
        mult = request.form.get("mult")
        passwd=request.form.get("pass")
        conf=request.form.get("conf")
        cursor.execute("Select max(user_ID) from user where user_id between 3000 and 3999")
        id=cursor.fetchone()[0]
        p_id=int(id)+1
        cursor.execute("Select email from user")
        cur=cursor.fetchall()
        for i in cur:
            if(i and email==i[0]):
                return redirect(url_for('prov_register',Success="Email Already Exists,Retry?"))
            
        if(passwd==conf):
            cursor.execute("insert into user(user_ID,password,name,email) values(%s,%s,%s,%s)",(p_id,passwd,name,email))
            mydb.commit()
            cursor.execute("insert into provider(p_id,p_scale,p_officeaddr,p_phoneNo,p_multiplier,p_PAN,p_GST,verified) values(%s,%s,%s,%s,%s,%s,%s,%s)",(p_id,scale,office,num,float(mult),pan,gst,False))
            #Had to use float() as number we get is a string so have to change it to a float
            mydb.commit()
            return redirect(url_for('prov_register',Success="Success Account Created:"+str(name) +" User Id:" +str(p_id)))
        else:
            return redirect(url_for('prov_register',Success="Passwords Do not match?"))
        


    success_message = request.args.get('Success', default='', type=str)
    return render_template('Provider_register.html',Success=success_message)


if __name__=="__main__":
    app.run(debug=True)
