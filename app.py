import json
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

POSTS_FILE_NAME = 'posts.json'
app = Flask(__name__)

def load_posts():
    try:
        with open(POSTS_FILE_NAME, "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_posts(post):
    with open(POSTS_FILE_NAME,'w',encoding='UTF-8') as file:
        json.dump(post,file,ensure_ascii=False, indent=2)

@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html',posts=blog_posts )

@app.route('/add', methods=['GET', 'POST'])
def add():
    blog_posts = load_posts()
    if request.method == 'POST':
        posts = load_posts()
        new_post = {
            "id": len(posts) + 1,
            "title": request.form.get('title'),
            "content": request.form.get('content'),
            "author": request.form.get('author')
        }
        blog_posts.append(new_post)
        save_posts(blog_posts)
        return redirect(url_for('index'))

    return render_template('add_post.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
