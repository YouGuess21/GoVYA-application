from flask import Flask,render_template,request,redirect,url_for,flash
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField

mydb=mysql.connector.connect(host="localhost",user="root",passwd="password",database="sql_college")
cursor=mydb.cursor()
app=Flask( __name__)
app.config['SECRET_KEY']='nokey'

class DataForm(FlaskForm): #We can create an object of this form
    text=StringField('', render_kw={"placeholder": "User ID", "id": "text"})
    password=StringField('', render_kw={"placeholder": "Password", "id": "password"})
    #Convert in end above is for ease of access while debugging
    #password=PasswordField('Enter Password:', render_kw={"id": "password"})
    submit=SubmitField('Login', render_kw={"id": "sub"})

@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/login',methods=['GET','POST'])
def login():
    #cursor.execute("select * from user")
    #value=cursor.fetchall()
    form=DataForm()
    return render_template('Login.html',form=form)

@app.route('/cust_funct',methods=['GET', 'POST'])
def CustomerFunction():
    if request.method == 'POST':
        user_id= request.form.get("user_id", default=0, type=int)
        todo=request.form.get('todo', default=0,type=int)
        if (user_id == 0):
            return redirect(url_for('unauth'))

        if(todo==1):
            cursor.execute("select c_ID,name,email,c_homeaddr,c_phoneNo from user join customer on user_ID=c_id where user_id=%s",(user_id,))
            userdata=cursor.fetchone() 
            #used fetchone because only one output would be there
            #didn't check wether it occured or not as it will definitely exist as we are inside it's login page
            return render_template('Cust_funct.html',userid=user_id,user_data=userdata,funct=1)
        if(todo==2):#create request options become visible
            return render_template('Cust_funct.html',userid=user_id,funct=2)
        if(todo==3):
            cursor.execute("select quote_ID ,name,quote_amt,quote_speed from (quotes natural join requests) join user on p_id=user_id where c_id=%s",(user_id,))
            userdata=cursor.fetchall()
            if bool(userdata):
                return render_template('Cust_funct.html',userid=user_id,cur=userdata,funct=3,quotepresent=True)
            else:
                return render_template('Cust_funct.html',userid=user_id,funct=3,noquotes=True)
                
        if(todo==5):#delete acc
            cursor.execute("select c_ID,name,email,c_homeaddr,c_phoneNo from user join customer on user_ID=c_id where user_id=%s",(user_id,))
            userdata=cursor.fetchone() 
            return render_template('Cust_funct.html',userid=user_id,user_data=userdata,funct=1,delacc=True)
        
        if(todo==7):#deleteing acc after confirmation
            cursor.execute("select * from orders where c_id=%s and status not like 'Complete%'",(user_id,))
            value=cursor.fetchall()
            if not value:
               cursor.execute("delete from user where user_id=%s",(user_id,))
               mydb.commit() 
               return render_template('User_deleted.html',userid=user_id)
            else:
                cursor.execute("select c_ID,name,email,c_homeaddr,c_phoneNo from user join customer on user_ID=c_id where user_id=%s",(user_id,))
                userdata=cursor.fetchone() 
                return render_template('Cust_funct.html',userid=user_id,user_data=userdata,funct=1,deletefail=True)
        if(todo==8):
            weight=request.form.get('weight',default=0,type=float)
            size=request.form.get('size',default=0,type=float)
            speed=request.form.get('speed',default=0,type=float)
            dist=request.form.get('dist',default=0,type=float)
            startpt = request.form.get('startpt', default='', type=str)
            endpt = request.form.get('endpt', default='', type=str)
            cursor.callproc('addrequest', (user_id, weight, size, speed, dist, startpt, endpt))
            cursor.execute("select max(req_id) from requests")
            rid=cursor.fetchone()[0]
            z=cursor.fetchall()
            return render_template('Cust_funct.html',userid=user_id,r_id=rid,funct=2,success=True)
        
        if(todo == 9):
            
            cursor.execute("select * from employee where isAssisting=0")  
            results = cursor.fetchall()
            empid=0
            if bool(results):
                for row in results:
                    if bool(row):
                        empid = int(row[0])
                        break
            
            if empid != 0 :
                
                cursor.execute("select * from employee natural join EMP_PHONENO where emp_id =%s",(int(empid),) )
                val2=cursor.fetchall()
                for row in val2:
                    if row:
                        val=row
                        break
                cursor.execute("update employee set isAssisting=%s where emp_id =%s",(user_id,empid))
                mydb.commit()
                return render_template('Cust_funct.html',row=val,cur2=val2,assigned=True,funct=2)

            else:
                return render_template('Cust_funct.html',unassigned=True,funct=2)
        if(todo==10):
            qid=request.form.get('qid',default=0,type=int)
            
            #remove request
            cursor.execute("select p_ID,quote_amt,quote_speed,req_id from quotes where quote_id = %s",(qid,))
            val=cursor.fetchone()
            if bool(val):
                p_id=val[0]
                q_amt=val[1]
                q_speed=val[2]
                req_id=val[3]
                cursor.execute("select c_ID,req_weight,req_size,req_dist,req_type,start,end from requests where req_id = %s",(req_id,))
                val2=cursor.fetchone()
                c_id=val2[0]
                req_weight=val2[1]
                req_size=val2[2]
                req_dist=val2[3]
                req_type=val2[4]
                start=val2[5]
                end=val2[6]
                print(c_id,p_id,req_weight,req_size,req_type,q_speed,'Processing',req_dist,q_amt,start,end)
                cursor.execute("delete from requests where req_id = %s",(req_id,))
                print("Deleted")
                mydb.commit()
                cursor.execute("select max( order_id) from orders")
                val=cursor.fetchone()
                if not bool(val):
                    order_id=0
                else:
                    order_id=val[0]
                order_id=order_id+1
                cursor.execute("insert into orders (c_ID, p_ID, order_ID, weight, size, type, speed, status, dist, bill, start, end) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (c_id, p_id, order_id, req_weight, req_size, req_type, q_speed, 'Processing', req_dist, q_amt, start, end))
                print("created order")
                mydb.commit()
                cursor.execute("select name from user where user_id=%s",(c_id,))
                name=cursor.fetchone()[0]
                return render_template('Customer.html',username=name,userid=user_id,order_id=order_id,ordercreated=True)
            else:
                cursor.execute("select quote_ID ,name,quote_amt,quote_speed from (quotes natural join requests) join user on p_id=user_id where c_id=%s",(user_id,))
                userdata=cursor.fetchall()
                if bool(userdata):
                    return render_template('Cust_funct.html',userid=user_id,cur=userdata,funct=3,quotepresent=True,wrongquote=True)
                else:
                    return render_template('Cust_funct.html',userid=user_id,funct=3,noquotes=True)
        if(todo==4):
            #  order_ID,name,weight,size,type,speed,status,dist,bill,start,end
            cursor.execute("select order_ID,name,weight,size,type,speed,status,dist,bill,start,end from orders join user on orders.p_id=user.user_id where c_id=%s and status not like 'Complete%'",(user_id,))
            cur=cursor.fetchall()
            if bool(cur):
                return render_template('Cust_funct.html',userid=user_id,cur=cur,funct=4,ordinprog=True)
            else:
                return render_template('Cust_funct.html',userid=user_id,funct=4,noordinprog=True)
        if(todo==11):
            cursor.execute("select order_ID,name,weight,size,type,speed,status,dist,bill,start,end from orders join user on orders.p_id=user.user_id where c_id=%s and status  like 'Complete%'",(user_id,))
            cur=cursor.fetchall()
            if bool(cur):
                return render_template('Cust_funct.html',userid=user_id,cur=cur,funct=5,ordercomp=True)
            else:
                return render_template('Cust_funct.html',userid=user_id,funct=5,noordercomp=True)
    return redirect(url_for('unauth'))

@app.route('/Customer',methods=['GET', 'POST'])
def customer():
    uname = request.args.get('Username', default='', type=str)
    userid = request.args.get('userID', default=0, type=int)
    if uname:
        return render_template('Customer.html', username=uname,userid=userid)
    else:
        return redirect(url_for('unauth'))

@app.route('/Provider', methods=['GET', 'POST'])
def provider():
    uname = request.args.get('Username', default='', type=str)
    userid = request.args.get('userID', default=0, type=int)
    
    if userid:
        return render_template('Provider.html', username=uname,userid=userid)
    else:
        return redirect(url_for('unauth'))

        
@app.route('/prov_funct', methods=['GET', 'POST'])
def ProviderFunction():
    if request.method == 'POST':
        user_id= request.form.get("user_id", default=0, type=int)
        todo=request.form.get('todo', default=0,type=int)
        if (user_id == 0):
            return redirect(url_for('unauth'))
        
        if(todo==1):#profile view
            cursor.execute("select user_ID,name,email,p_scale,p_officeaddr,p_phoneNo,p_multiplier,p_PAN,p_GST from user join provider on user_id=p_id where p_id=%s",(user_id,))
            userdata=cursor.fetchone()   
            return render_template('prov_funct.html',userid=user_id,user_data=userdata,funct=1)

        if(todo==5):#delete acc
            cursor.execute("select user_ID,name,email,p_scale,p_officeaddr,p_phoneNo,p_multiplier,p_PAN,p_GST from user join provider on user_id=p_id where p_id=%s",(user_id,))
            userdata=cursor.fetchone() 
            return render_template('prov_funct.html',userid=user_id,user_data=userdata,funct=1,delacc=True)
        if(todo==6):#update acc
            cursor.execute("select user_ID,name,email,p_scale,p_officeaddr,p_phoneNo,p_multiplier,p_PAN,p_GST from user join provider on user_id=p_id where p_id=%s",(user_id,))
            userdata=cursor.fetchone() 
            return render_template('prov_funct.html',userid=user_id,user_data=userdata,funct=1,updateacc=True)
        
        if(todo==7):#deleteing acc after confirmation
            cursor.execute("select * from orders where p_id=%s and status not like 'Complete%'",(user_id,))
            value=cursor.fetchall()
            if not value:
               cursor.execute("delete from user where user_id=%s",(user_id,))
               mydb.commit() 

               return render_template('User_deleted.html',userid=user_id)
            else:
                cursor.execute("select user_ID,name,email,p_scale,p_officeaddr,p_phoneNo,p_multiplier,p_PAN,p_GST from user join provider on user_id=p_id where p_id=%s",(user_id,))
                userdata=cursor.fetchone() 
                return render_template('prov_funct.html',userid=user_id,user_data=userdata,funct=1,deletefail=True)
        if(todo==2):
            cursor.execute("select p_scale from provider where p_id=%s",(user_id,))
            scale=cursor.fetchone()[0]
            if(scale=="Small"):
                cursor.execute("select * from requests where req_type like 'Small'")
                val=cursor.fetchall()
            if(scale=="Medium"):
                cursor.execute("select * from requests where req_type like 'Small' or req_type like 'Medium'")
                val=cursor.fetchall()
            if(scale=="Large"):
                cursor.execute("select * from requests where req_type like 'Small' or req_type like 'Medium' or req_type like 'Large'")
                val=cursor.fetchall()
            if bool(val):
                return render_template('prov_funct.html',userid=user_id,cur=val,funct=2,req_exist=True)
            else:
                return render_template('prov_funct.html',userid=user_id,funct=2,req_not=True)
        
        if todo==8 :
            
            rid= request.form.get("rid", default=0, type=int)
            amount= request.form.get("amt", default=0, type=int)
            days= request.form.get("days", default=0,type=int)
            
            cursor.execute("select max( distinct quote_id) from quotes")
            val=cursor.fetchone()
            if not bool(val):
                quoteid=0
                
            else:
                quoteid=val[0]
            
            quoteid=quoteid+1
            cursor.execute("insert into quotes(quote_id,p_id,quote_amt,quote_speed,req_id) values(%s,%s,%s,%s,%s)",(quoteid,user_id,amount,days,rid))
            mydb.commit()
            cursor.execute("select p_scale from provider where p_id=%s",(user_id,))
            scale=cursor.fetchone()[0]
            if(scale=="Small"):
                cursor.execute("select * from requests where req_type like 'Small'")
                val=cursor.fetchall()
            if(scale=="Medium"):
                cursor.execute("select * from requests where req_type like 'Small' or req_type like 'Medium'")
                val=cursor.fetchall()
            if(scale=="Large"):
                cursor.execute("select * from requests where req_type like 'Small' or req_type like 'Medium' or req_type like 'Large'")
                val=cursor.fetchall()
            return render_template('prov_funct.html',userid=user_id,funct=2,qid=quoteid,qcreate=True,req_exist=True,cur=val)
        if (todo==3):
            cursor.execute("select order_ID,c_id,c_phoneNo,weight,size,type,speed,status,dist,bill,start,end from orders natural join customer where p_id=%s and status not like 'Complete%'",(user_id,))
            cur=cursor.fetchall()
            if bool(cur):
                return render_template('prov_funct.html',userid=user_id,cur=cur,funct=3,ordinprog=True)
            else:
                return render_template('prov_funct.html',userid=user_id,funct=3,noordinprog=True)
        if (todo==9):
            ord_id= request.form.get("ordid", default=0, type=int)
            stat= request.form.get("status", default='',type=str)
            cursor.execute("select order_ID from orders where p_id=%s and status not like 'Complete%'",(user_id,))
            val=cursor.fetchall()
            cursor.execute("select order_ID,c_id,c_phoneNo,weight,size,type,speed,status,dist,bill,start,end from orders natural join customer where p_id=%s and status not like 'Complete%'",(user_id,))
            cur=cursor.fetchall()
            for row in val:
                if row[0]==ord_id:
                    cursor.execute("update orders set status=%s where order_ID=%s",(stat,ord_id))
                    mydb.commit()
                    cursor.execute("select order_ID,c_id,c_phoneNo,weight,size,type,speed,status,dist,bill,start,end from orders natural join customer where p_id=%s and status not like 'Complete%'",(user_id,))
                    cur=cursor.fetchall()
                    if stat=="Completed" or stat=="Complete":
                        if bool(cur):
                            return render_template('prov_funct.html',cur=cur,userid=user_id,funct=3,ordupdate=True,ordinprog=True)
                        else:
                            return render_template('prov_funct.html',userid=user_id,funct=3,ordupdate=True,noordinprog=True)
                    
                    return render_template('prov_funct.html',cur=cur,userid=user_id,funct=3,ordupdate=True,ordinprog=True)
            return render_template('prov_funct.html',cur=cur,userid=user_id,funct=3,wrongid=True,ordinprog=True)
        if (todo==4):
            cursor.execute("select order_ID,c_id,c_phoneNo,weight,size,type,speed,status,dist,bill,start,end from orders natural join customer where p_id=%s and status like 'Complete%'",(user_id,))
            cur=cursor.fetchall()
            if bool(cur):
                return render_template('prov_funct.html',userid=user_id,cur=cur,funct=4,ordercomp=True)
            else:
                return render_template('prov_funct.html',userid=user_id,funct=4,noordercomp=True)
                

            

    return redirect(url_for('unauth'))

@app.route('/deleted')
def udeleted():
    if(request.method == 'POST'):
        return render_template('User_deleted.html')
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
                    cursor.execute("select verified from provider where p_id=%s",(entered_userid,))
                    stat=cursor.fetchone()[0]
                    if stat == 1:
                        return redirect(url_for('provider',Username=name,userID=entered_userid))
                    else:
                        return render_template('User_selector.html', Welcome='Account is not yet Verified')
                
                        
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
                return redirect(url_for('cust_register',Success="Account with same Email-Id Already Exists,Retry?"))

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
