from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Filters : upper, lower, capitalize, trim, title, striptags, safe |
    username = "Sanjay Pandian"
    avengers = ["Ironman","Spiderman","Thor","Captain America"]
    return render_template("index.html", name=username, avengers=avengers)

@app.route('/profile/<name>')
def user(name):
    return render_template('profile.html', username=name)

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html"),400



