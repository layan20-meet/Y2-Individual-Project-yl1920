from databases import *
from model import *
from flask import *
from flask import session as login_session
import flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/index')
def home():
	return render_template('index.html')

@app.route('/')
def NewHome():
	return home()


@app.route('/SignUp', methods=["POST","GET"])
def SignUp():
	if request.method=="GET":
		return render_template('SignUp.html')
	else:
		Fname=request.form["Fname"]
		Lname=request.form["Lname"]
		username=request.form["username"]
		Email=request.form["Email"]
		password=request.form["password"]
		add_User(Fname,Lname,username,Email,password)
		return redirect(url_for('Travels'))



@app.route('/LogIn',methods=['GET','POST'])
def LogIn():
	if request.method=='POST':
		username=request.form['username']
		password=request.form['password']
		all_users=query_all_users()
		for u in all_users:
			print("u = "+u.username)
			print("p = "+u.password)
		for user in all_users:
			print user.username
			print user.password
			if user.username==username and user.password==password:
				print ("Logged in successfully")
				return redirect(url_for('Travels'))
		return redirect('LogIn')
	else:
		return render_template("LogIn.html")


@app.route('/Travels')
def Travels():
	travels=query_all_travels()
	return render_template("Travels.html" , travels=travels)

@app.route('/Add_Travel',methods=['GET','POST'])
def Add_Travel():
	if request.method=="POST":
		Travel_name=request.form["Travel_name"]
		Destinaion=request.form["Destintaion"]
		Dates=request.form["Dates"]
		Ques1=request.form["Ques1"]
		Ques2=request.form["Ques2"]
		Ques3=request.form["Ques3"]
		Ques4=request.form["Ques4"]
		Ques5=request.form["Ques5"]
		picture=request.form["picture"]
		add_Travel(Travel_name,Destinaion,Dates,Ques1,Ques2,Ques3,Ques4,Ques5,picture)
		return redirect(url_for('Travels'))
	return render_template('Add_Travel.html')

@app.route('/delete/<int:travel_id>')
def delete(travel_id):
	delete_travel(travel_id)
	return redirect(url_for('Travels'))

@app.route('/LogOut')
def LogOut():
	return render_template('LogOut.html')


if __name__ == '__main__':
	app.run(debug=True)