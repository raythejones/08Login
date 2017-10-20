from flask import Flask, render_template, request, session, redirect, url_for, flash
import os 

app = Flask(__name__)
app.secret_key = os.urandom(32)


#test account info
username = 'ray'
password = 'jones'

@app.route('/')
def root():
	if session.has_key('myUser'):
		return redirect( url_for('greeting') )
	else: 
		return render_template('home.html')
'''
@app.route('/route', methods = ['POST'])
def route():
    if request.form['myUser'] == username:
        session['name'] = request.form['myUser']
        return render_template('greeting.html', myUser = request.form['myUser'])
    else:
        return render_template('home.html', message = "username or password incorrect")
'''


@app.route('/verify', methods = ['POST','GET'])
def verify():
	inputUser = request.form['myUser']
	inputPass = request.form['myPass']
	if inputUser == username:
		if inputPass == password:
			session['myUser'] = request.form['myUser']
			flash('Your Login Was Successful')
			return redirect( url_for('greeting') )
		else:
			flash('The Password Was Incorrect. Try again!')
			return redirect( url_for('root') )
	else:
		flash('The Username Was Incorrect. Try again!')
		return redirect( url_for('root') )
    
    
    
    
@app.route('/greeting', methods = ['POST', 'GET'])
def greeting():
	return render_template('greeting.html', myUser = session['myUser'])




@app.route('/logout', methods = ['POST', 'GET'])
def logout():
	session.pop('myUser')
	flash('You Have Been Logged Out')
	return redirect( url_for('root') )
    
    
if __name__ == '__main__':
	app.debug = True
	app.run()