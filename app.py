from flask import Flask,render_template,request,redirect,flash

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)
#Setting Secret Key so that we can work with forms in our app it protects against modifying cookies,cross-site 
# attacks and forgery attacks
app.config['SECRET_KEY'] = "a0e07a5d0eb818d1453f16bac1bf967d"
#initializing database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TODO.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db=SQLAlchemy(app)

#defining the structure of table of database using class 
class TODO(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    #ye method ye kaam karta hai jab bhi ham todo class ke kisi object ko print karenge to
    #kya print hona chahiye
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

class submit_form(FlaskForm):
    todo_title=StringField('Todo',validators=[DataRequired(), Length(min=3,max=100)])
    desc=StringField('Description',validators=[DataRequired(), Length(min=5,max=200)])
    submit= SubmitField('Submit')
    update= SubmitField('Update')

@app.route("/",methods=['GET'])
def index():
    form=submit_form()
    alltodo=TODO.query.all()
    return render_template("index.html",alltodo = alltodo,form=form) 

@app.route("/submit",methods=['GET','POST'])
def submit():
    form=submit_form()
    alltodo=TODO.query.all()
    if request.method=="POST":
        #jab bhi koi user submit par click karega tabhi ham ek instance(object) bana lenge ek todo class ka
        #jisko phir ham databse meon add kar denge
        if form.validate_on_submit():
            title=form.todo_title.data
            desc=form.desc.data
            todo = TODO(title=title,desc=desc)
            db.session.add(todo)
            db.session.commit()
            flash(f"TODO {title} added successfully","success")
            form.todo_title.data=""
            form.desc.data=""
            return redirect("/")
        return render_template("index.html",alltodo = alltodo,form=form) 

@app.route("/delete/<int:sno>")           
def delete(sno):
    todo=TODO.query.filter_by(sno=sno).first()
    title=todo.title
    db.session.delete(todo)
    db.session.commit()
    flash(f"TODO {title} deleted successfully","danger")
    return redirect("/")

@app.route("/update/<int:sno>",methods=['GET','POST'])           
def update(sno):
    form=submit_form()
    if request.method=="POST":
        if form.validate_on_submit():
            title=form.todo_title.data
            desc=form.desc.data
            todo = TODO.query.filter_by(sno=sno).first()
            todo.title=title
            todo.desc=desc
            db.session.add(todo)
            db.session.commit()
            flash(f"TODO {title} updated successfully","warning")
            return redirect("/")

    todo1=TODO.query.filter_by(sno=sno).first()
    return render_template("update.html",todo1=todo1,form=form)



if __name__=="__main__":
    app.run(debug=False,port=8000)
