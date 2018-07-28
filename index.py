from flask import Flask,render_template,request,session
import os
#from dbconnect import connection
import MySQLdb

db= MySQLdb.connect("localhost","root","San@1234","YogaDB")

app = Flask(__name__)

'''@app.route("/")
def visitor():
	return render_template ("home.html")'''

#@app.route("/")
#def visitor():
#	return render_template ("visitorindex.html")

@app.route("/")
def services():
	return render_template ("sarvice.html")

'''@app.route("/s")
def services1():
	return render_template ("sarvice1.html")'''


@app.route("/contact")
def contact():
	return render_template ("contact.html")

@app.route("/contact1")
def contact1():
	return render_template ("contact1.html")

@app.route("/about")
def about():
	return render_template ("aboutus.html")

@app.route("/about1")
def about1():
	return render_template ("aboutus1.html")

@app.route("/member")
def member():
	return render_template ("sarvice1.html")

@app.route("/admin")
def admin():
	return render_template ("homeadm.html")

@app.route("/memreg")
def memreg():
	return render_template ("regist.html")

@app.route("/treg")
def treg():
	return render_template ("treg.html")

@app.route("/result", methods =['POST','GET'])
def result():
	if request.method == 'POST':
		FirstName = request.form['first']
		MiddleName = request.form['middle']
		LastName = request.form['last']
		Address = request.form['addr']
		dob = request.form['bir']
		Mob = request.form['mob']
		Mob1 = request.form['mob1']
		Email = request.form['email']
		College = request.form['school']
		gender = request.form['gen']
		married = request.form['marstat']
		weight = request.form['weight']
		Blood = request.form['bg']
		Veg = request.form['veg']
		occ = request.form['occ']
		medical = request.form['medical']
		reason = request.form['reason']
		Cert = request.form['cer']
		info = request.form['info']
		Pass = request.form['password']
		confirm = request.form['cpassword']
		Place = request.form['place']
        cursor=db.cursor()
        cursor.execute("""insert into memberreg(First_Name,Middle_Name,Last_Name,Local_Address,DOB,Mob_No,Alternative_Mob_No,Email_ID,College,Gender,Marital_Status,Weight,Blood_Group,Veg_NonVeg,Occupation,Medical,Reason,Dr_Certificate,Info,Password,Confirm_Password,Place)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(FirstName,MiddleName,LastName,Address,dob,Mob,Mob1,Email,College,gender,married,weight,Blood,Veg,occ,medical,reason,Cert,info,Pass,confirm,Place))
        cursor.fetchall()
        db.commit()
        msg="register"
        return render_template("msg.html", msg = msg)
        db.close()



@app.route("/login")
def login():
	return render_template ("login1.html")

@app.route("/admin",methods=["GET","POST"])
def login1():
    if request.form['psw'] == 'admin' and request.form['email'] == 'admin':
        session['logged_in'] = True
        result = request.form
        return render_template("homeadm.html",result = result)
    else:
        username = request.form['username']
        password = request.form['password']
        session['logged_in'] = True

        cursor = db.cursor()
        cursor.execute("select * from member_reg where username ='"+username+"' and password ='"+password+"'")
        user = cursor.fetchall()

        if len(user) is 1:
            return render_template('memberindex.html')
        else:
            msg=('invalid username or password')
            msg1=('please login with correct username/password!')
            return render_template ("login1.html", msg=msg, msg1=msg1)


@app.route("/result1", methods =['POST','GET'])
def result1():
	if request.method == 'POST':
		FirstName = request.form['firstname']
		LastName = request.form['lastname']
		Mob = request.form['contact']
		Payment = request.form['payment']
		Email = request.form['email']
		Address = request.form['add']
		
        cursor=db.cursor()
        cursor.execute("""insert into Teacher_reg(First_Name,Last_Name,Contact,Payment,Email_ID,Address)
        	values (%s,%s,%s,%s,%s,%s)""",
        	(FirstName,LastName,Mob,Payment,Email,Address))
        cursor.fetchall()
        db.commit()
        msg="Successfully registered!"
        return render_template("treg.html", msg = msg)
        db.close()

@app.route("/meal")
def meal():
	return render_template ("meal.html")

@app.route("/displaytrain")
def displaytrain():
	cursor = db.cursor()
	cursor.execute("select * from Teacher_reg")
	data=cursor.fetchall()
	return render_template("trainregist.html",data = data)
	
	db.close()

@app.route("/displaymem")
def displaymem():
	cursor = db.cursor()
	cursor.execute("select * from memberreg")
	data=cursor.fetchall()
	return render_template("memrregist.html",data = data)
	
	db.close()



if (__name__ == "__main__"):
	app.secret_key = os.urandom(12)
	app.run(debug = True)

