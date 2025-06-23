from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
import os 
from werkzeug.utils import secure_filename
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'i_love_pizza'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images','logos')
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
db = SQLAlchemy(app)
migrate = Migrate(app, db)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50))  # trending, highlight, recent
    highlight_type = db.Column(db.String(10), nullable=True) #main or small
    image = db.Column(db.String(200), nullable=True, default='default_post.jpeg')
# Path to image in /static/images

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    image_url = db.Column(db.String(255))  # Main banner
    logo_url = db.Column(db.String(255))   # Company logo (new)
    location = db.Column(db.String(150)) 

@app.route('/')
def index():
    today = datetime.today()
    events = Event.query.filter(Event.date >= today).order_by(Event.date.asc()).limit(10).all()
    posts = Post.query.order_by(Post.date.desc()).all()
    
    trending_posts = [p for p in posts if p.category == 'trending']
    recent_posts = [p for p in posts if p.category == 'recent']
    highlight_main = next((p for p in posts if p.category == 'highlight' and p.highlight_type == 'main'), None)
    highlight_smalls = [p for p in posts if p.category == 'highlight' and p.highlight_type == 'small']
   
    products = [p for p in posts if p.category == 'products']
    

    # Dummy placeholders for optional sections
    ad_exists = True  # You can implement logic to toggle this
    topics = ['AI', 'Cybersecurity','DevOps']
    
    return render_template('base.html', 
                           trending_posts=trending_posts, 
                           highlight_main=highlight_main,
                           highlight_smalls=highlight_smalls,
                           recent_posts=recent_posts,
                           ad_exists=ad_exists,
                           topics=topics,
                           events=events,
                           products=products)

@app.route('/dashboard')
def dashboard():
    posts = Post.query.order_by(Post.date.desc()).all()
    events = Event.query.order_by(Event.date.asc()).all()
    return render_template('dashboard.html', posts=posts, events=events)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        image_file = request.files['image']
        filename = None

        if image_file and image_file.filename != '' :
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)

        category = request.form.get('category')
        highlight_type = request.form.get('highlight_type') if category == 'highlight' else None

        if category == 'highlight' and not highlight_type:
            flash('Please select a highlight type.', 'error')
            return redirect(request.url)

        new_post = Post(
            title=request.form['title'],
            author=request.form['author'],
            content=request.form['content'],
            category=category,
            highlight_type=highlight_type,
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

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)

    

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date_str = request.form['date']
        event_date = datetime.strptime(date_str, '%Y-%m-%d')
        logo = request.files['logo']

        if logo and allowed_file(logo.filename):
            filename = secure_filename(logo.filename)
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            logo.save(filepath)
            logo_url = f"/{filepath.replace('\\', '/')}"  # Web-safe path
        else:
            logo_url = "/static/default_logo.png"  # fallback


        new_event = Event(title=title, description=description, date=event_date, logo_url=logo_url)
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('create_event.html')

@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == 'POST':
        event.title = request.form['title']
        event.description = request.form['description']
        event.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
       
        logo = request.files.get('logo')
        if logo and logo.filename != '' and allowed_file(logo.filename):
            filename = secure_filename(logo.filename)
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            logo.save(filepath)
            event.logo_url = f"/{filepath.replace('\\', '/')}"

        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('edit_event.html', event=event)

@app.route('/delete_event/<int:event_id>')
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/events/<int:event_id>')
def view_event(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('view_event.html', event=event)



if __name__ == '__main__':
    #with app.app_context():
      #  db.create_all()
    app.run(debug=True)
