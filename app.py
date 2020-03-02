from flask import Flask, render_template, request, redirect
from config import app, db, migrate
from models import Ninja, Dojo
from sqlalchemy.sql import func #pylint: disable=import-error

@app.route("/")
def main():
	# grabs all dojos
	dojo_results = Dojo.query.all()
	return render_template("main.html", dojos=dojo_results)

@app.route("/add_dojo", methods=["POST"])
def add_dojo():
	new_dojo = Dojo(name=request.form['name'], city=request.form['city'], state=request.form['state'])
	print("Adding new dojo...")
	print(new_dojo)
	db.session.add(new_dojo)
	db.session.commit()

	return redirect("/")

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
	new_ninja = Ninja(first_name=request.form['first_name'], last_name=request.form['last_name'], dojo=Dojo.query.get(request.form['id']))

	print("Adding new ninja...")
	print(new_ninja)
	db.session.add(new_ninja)
	db.session.commit()
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)