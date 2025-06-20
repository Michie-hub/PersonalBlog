from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os 
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/images'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50))  # trending, highlight, recent
    image = db.Column(db.String(200))    # Path to image in /static/images

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
        {'image': 'product1.jpg', 'description': 'Top Tech Gadgets 2025'},
        {'image': 'product2.jpg', 'description': 'Software Essentials'}
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
        image_file = request.files['image']
        if image_file and image_file.filename!= '' :
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)

        new_post = Post(
            title=request.form['title'],
            author=request.form['author'],
            content=request.form['content'],
            category=request.form['category'],
            image=filename
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

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        post.category = request.form['category']

        if 'remove_image' in request.form:
            post.image = None
        else:
            post.image = request.form['image']    
        
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('edit_post.html', post=post)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
