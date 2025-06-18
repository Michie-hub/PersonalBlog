from flask import Flask, render_template, request, redirect, url_for
from models import db, Article


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.creat_all()

@app.route('/')
def home():
    articles = Article.query.order_by(Article.date_posted.desc()).all()
    return render_template('base.html')  # Make sure this file exists in templates/
@app.route('/add', methods=['POST'])
def add_article():
    title = request.form['title']
    author = request.form['author']
    description = request.form['description']
    image = request.form['image']  # path like 'images/img7.jpeg'

    new_article = Article(title=title, author=author, description=description, image=image)
    db.session.add(new_article)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
