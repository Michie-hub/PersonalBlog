from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50))  # trending, highlight, recent
    image_filename = db.Column(db.String(200))    # Path to image in /static/images

@app.route('/')
def index():
    posts = Post.query.order_by(Post.date.desc()).all()

    trending_posts = [p for p in posts if p.category == 'trending']
    highlight_posts = [p for p in posts if p.category == 'highlight']
    recent_posts = [p for p in posts if p.category == 'recent']

    highlight_main = highlight_posts[0] if highlight_posts else None
    highlight_smalls = highlight_posts[1:] if len(highlight_posts) > 1 else []

    # Dummy placeholders for optional sections
    ad_exists = True  # You can implement logic to toggle this
    event = {'date': datetime.utcnow().strftime('%Y-%m-%d'), 'description': 'Tech Conference 2025'}
    topics = ['AI', 'Cybersecurity', 'Web Dev']
    products = [
        {'image_filename': 'product1.jpg', 'description': 'Top Tech Gadgets 2025'},
        {'image_filename': 'product2.jpg', 'description': 'Software Essentials'}
    ]

    return render_template('base.html', 
                           trending_posts=trending_posts, 
                           highlight_main=highlight_main,
                           highlight_smalls=highlight_smalls,
                           recent_posts=recent_posts,
                           ad_exists=ad_exists,
                           event=event,
                           topics=topics,
                           products=products)

@app.route('/dashboard')
def dashboard():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template('dashboard.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        new_post = Post(
            title=request.form['title'],
            author=request.form['author'],
            content=request.form['content'],
            category=request.form['category'],
            image_filename=request.form['image_filename']
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('create_post.html')

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
