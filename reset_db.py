from app import db, app
import os

if os.path.exists('posts.db'):
    os.remove('posts.db')

with app.app_context():
    db.create_all()

print("Database reset and tables created.")
