# About Application
Flask is a micro web framework written in Python. It is classified as a microframework because it does not 
require particular tools or libraries.
<br>

### Create Flask Application
Create a flask app using app = Flask(__name__) 

We create multiple pages for our application.
When a client makes a request to a valid particular route defined in app.py the defined below that route gets executed and the content is rendered by the browser as defined by the functionality of that function.
<br>
HOME ROUTE
```bash
 @app.route("/")
```
 
### Render_Template 
It is used with return so that we can render the html page or template present inside the static folder of app on the browser.

### To Run
For running the app we write this code 

```bash
	if __name__=="__main__":
		app.run(debug=False,port=8000)
```

## For Database

1. Sabse pehle hame agar database banana hai flask mein to hame use karna padega flask ke flask_SQL Alchemy package ko. So first we have to install flask-sqlalchemy in our environment.

2. SQL Alchemy ek ORM mapper hai jo ki python ke through database mein changes karne ke liye facilities provide karta hai. Similar to JPA Repository in Spring Boot.

3. Phir ham pehle database ko initialize karenge, uske baad ham specify karte hain ki kaun sa database ham use karna chahte hain.Jis tarah ka ham DATABASE_URI specify karte hain usi type ka database banta hai 
hamara(sql_lite,mysql) mein. 

4. Database banane ke liye hame flask ko batana padta hai ki ham database mein kya kya cheezein store karenge jiske liye hame class banani padti hai jisme ham specify karte hain ki hamare database mein kaun-kaun si fields hongi phir un fields ka datatype  kya hoga. Phir uske baad ham database ko banane ke liye ek python ka command use karte hain jisse ki flask apne aap hamare required database ko bana deta hai (which containe the fields present in the class which we created...that is the work of ORM. It is also helpful in making connections to already existing databases so that we do not have to explicilty write bunch pf code for connecting to databses and it also provides functionality so that we can avoid writing queries in order to fetch the record from that table of databases unless until it is a very much complicated query.)

To create the initial database, just import the db object from an interactive Python shell and run 
the SQLAlchemy.create_all() method to create the tables and database:
```bash
from app import db
db.create_all()
```

## Host The Application On HEROKU

1. Iske liye sabse pehle ham "gunicorn" library ko install karna padta hai taki multiple threads mein ham apni application ko run kara skein.
Ye ek proc file use karega jo ki ham heroku specific banayenge.

	```bash
	pip install gunicorn
	```

2. Proc file is used by heroku app in order to deploy the appilication .proc file mein ham heroku ko ye batayenge ki kaun si app ko heroku exexute karega. 

3. App ko heroku par depoly karne ke liye hame requirements ko bhi store karna padta hai jo ki ham store karte hain requirements.txt file mein by exceuting 

	```bash
	pip freeze > requirements.txt
	```
4. After installing heroku cli ,type "heroku login" in terminal to log in to heroku account.

5. Then write
	* git init 
	* git add .
	* git commit -m "mssg"
<br>

6. Then write in terminal "heroku create todo-rm".This will create a project on heroku and it will return the url on which our heroku app get published.
	```bash
	heroku create todo-rm
	````

7. Ham yahan par github nhi use kar rahe hain ham heroku ko use kar rahe hain as remote repository system. Par git same hi rahega jo ki local repository system ko maintain karne ke liye use kiya jaata hai.
	
	```bash
	git remote -v
	```
	Ye command hame bata dega ki kis url se
	ham fetch kar rahe hain aur kis url par push perform kar rahe  hain.

8. To push/deploy our app on heroku now write the command as 
	```bash
	git push heroku master
	```
9. #### NOTE 
	If due to some reason , at the time of  deployment this is shown:
	Procfile declares types -> web
	Instead of this
	Procfile declares types -> (none)

	Then accidently you might have created the file ProcFile instead of Procfile .Simply 
	renaming that file will not get picked up by git. You had to do a 
	```bash
	git rm ProcFile -f
	``` 
	what it does it will remove the file from your local repository because it is already present in tracked area and then you again add the file with the modified new name to the tracked area using command
	```bash
	git add Procfile
	```
	After that, when you push the changes after committing them on local repository to remote repository it will get picked up correctly by Heroku.


 


