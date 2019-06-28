
import firebase_admin
from firebase_admin import credentials, firestore
import google.cloud

cred = credentials.Certificate("path/to/file.json")

Config = {

  "apiKey": " ",
  "authDomain": " ",
  "databaseURL": " ",
  "projectId": " ",
  "storageBucket": " ",
  "messagingSenderId": " ",
  "appId": " "
  "cred"}
firebase = firebase_admin.initialize_app(config)
db = firestore.client()

@bpp()

def storage():
docs = db.collection(u'users').get()

	if request.method == 'POST':
		if request.form['submit'] == 'add':
		
			name = request.form['name']
			db.collection(u'users').document(u'alovelace').set(name)
			return ('item added')
		
		elif request.form['submit'] == 'delete':
			db.collection(u'users').document(u'alovelace').delete()
			return ('item removed')
	return ('item added')

	else:

		db.collection(u'users').get()

		for doc in docs:
    		print(u'{} => {}'.format(doc.id, doc.to_dict()))


if __init__ == '__main__':
	bpp.run()