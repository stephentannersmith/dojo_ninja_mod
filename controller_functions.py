from flask import render_template, redirect, request
# we now need fewer imports because we're not doing everything in this file!

# if we need to work with the database, we'll need those imports:
from config import db
from models import Ninja, Dojo

def main():
	# grabs all dojos
	dojo_results = Dojo.query.all()
	return render_template("main.html", dojos=dojo_results)

def add_dojo():
	new_dojo = Dojo(name=request.form['name'], city=request.form['city'], state=request.form['state'])
	print("Adding new dojo...")
	print(new_dojo)
	db.session.add(new_dojo)
	db.session.commit()

	return redirect("/")

def add_ninja():
	new_ninja = Ninja(first_name=request.form['first_name'], last_name=request.form['last_name'], dojo=Dojo.query.get(request.form['id']))

	print("Adding new ninja...")
	print(new_ninja)
	db.session.add(new_ninja)
	db.session.commit()
	return redirect("/")