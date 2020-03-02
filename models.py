from sqlalchemy.sql import func #pylint: disable=import-error
from config import db

class Dojo(db.Model):
	__tablename__ = "dojos"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	city = db.Column(db.String(255))
	state = db.Column(db.String(255))
	created_at = db.Column(db.DateTime, server_default=func.now())
	updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Ninja(db.Model):
	__tablename__ = "ninjas"
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(255))
	last_name = db.Column(db.String(255))
	dojos_id = db.Column(db.Integer, db.ForeignKey("dojos.id", ondelete="cascade"), nullable=False)
	dojo = db.relationship("Dojo", foreign_keys=[dojos_id], backref="ninjas")
	created_at = db.Column(db.DateTime, server_default=func.now())
	updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
	
	def full_name(self):
		return f"{self.first_name} {self.last_name}"