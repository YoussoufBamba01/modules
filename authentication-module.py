
import pyrebase



Config = {

  "apiKey": " ",
  "authDomain": " ",
  "databaseURL": " ",
  "projectId": " ",
  "storageBucket": " ",
  "messagingSenderId": " ",
  "appId": " "
  }
firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()

@app()

def authentication():
	
	email = request.form['name']
	password = request.form['pass']

	if request.method == 'POST':
		
		try:
			auth.sign_in_with_email_and_password(email, password)
			return'login successfully completed'
		
		except :
				try:

					auth.send_password_reset_email(email)
					return 'email sended'

				except:
					auth.create_user_with_email_and_password(email,password)
					return 'email created'
			
		return 'Login successful'

	return render_template 'login successfully completed'	

	else:
	
		auth.sign_in_with_email_and_password(email, password)
		print(auth.get_account_info(user['idToken']))
	return'here are your info'
	


if __init__ =='__main__':
	
	app.run()