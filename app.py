import json
from flask import Flask, render_template

POSTS_FILE_NAME = 'posts.json'
app = Flask(__name__)

def load_posts():
    try:
        with open(POSTS_FILE_NAME, "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html',posts=blog_posts )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
