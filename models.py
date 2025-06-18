from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Article(db.model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  author = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text(200), nullable=False)
  image = db.Column(db.String(100), nullabe=False)
  date_posted = db.Column(db.DateTime, default=datetime.utcnow)
