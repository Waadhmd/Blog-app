# Flask Blog

A simple Flask blog application using JSON file storage for posts.  

This project is built in phases: the current phase implements **basic CRUD functionality** for blog posts. Future phases will add user authentication, categories, likes, and comments.

---

## Features (Current Phase)

- Display all blog posts on the homepage
- Add new posts via a form
- Update existing posts via a pre-filled form
- Delete posts with a delete button
- JSON-based storage (`posts.json`)
- Server-side caching disabled for consistent updates

---

## Upcoming Features

- **User authentication**  
  - Sign up, log in, and log out functionality  
  - Posts linked to specific users  

- **Categories for posts**  
  - Assign posts to categories  
  - Filter posts by category  

- **Likes for posts and comments**  
  - Users can like posts  
  - Optional comments system with likes  

- **Improved styling**  
  - Responsive design  
  - Better layout for posts and forms
   
##install dependencies:
  - pip install flask

## Usage:

- Add a post: Click "➕ Add New Post", fill the form, and submit. 
- Update a post: Click "Update" on any post, edit the fields, and submit.
- Delete a post: Click "Delete" on any post to remove it.