import json
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

POSTS_FILE_NAME = 'posts.json'
app = Flask(__name__)

def load_posts():
    """
    Load blog posts from the JSON file.
    Returns:
        list[dict]: A list of posts, each represented as a dictionary.
    """
    try:
        with open(POSTS_FILE_NAME, "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def fetch_post_by_id(posts,post_id):
    """
    Find and return a blog post by its ID.
    """
    post = next((post for post in posts if post['id'] == post_id),None)
    return post

def save_posts(post):
    """
     Save the list of blog posts to the JSON file
    """
    with open(POSTS_FILE_NAME,'w',encoding='UTF-8') as file:
        json.dump(post,file,ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """
     Render the homepage with a list of all blog posts.
     Returns:
         Response: Rendered HTML page with blog posts.
     """
    blog_posts = load_posts()
    return render_template('index.html',posts=blog_posts )

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
     Handle adding a new blog post.
     GET:
         Render the 'add_post.html' template with the form.
     POST:
         Create a new post, save it, and redirect to the homepage.
"""
    if request.method == 'POST':
        posts = load_posts()
        new_post = {
            "id": max((post['id'] for post in posts),default=0) + 1,
            "title": request.form.get('title'),
            "content": request.form.get('content'),
            "author": request.form.get('author')
        }
        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))

    return render_template('add_post.html')

@app.route('/delete-post/<int:post_id>',methods=['POST'])
def delete(post_id):
    """
       Handle deleting a blog post by its ID.
    Args:
        post_id (int): ID of the post to delete
    """
    posts = load_posts()
    posts = [post for post in posts if post['id'] != post_id]
    save_posts(posts)
    return redirect(url_for('index'))

@app.route('/update/<int:post_id>',methods=['GET','POST'])
def update(post_id):
    """
     Handle updating an existing blog post.
     GET:
         Render the 'update_post.html' template with current post data.
     POST:
         Update the post's fields, save changes, and redirect to homepage.
    """
    posts = load_posts()
    post = fetch_post_by_id(posts,post_id)

    if post is None:
        return 'Post not found',404
    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        post['author'] = request.form['author']
        save_posts(posts)
        return redirect(url_for('index'))
    else:
         return render_template('update_post.html',post = post)


@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    return response



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
