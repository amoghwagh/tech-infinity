from flask import Flask, render_template,url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Amogh Wagh',
        'title' : 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted' : 'April 20 , 2019'
    },
     {
        'author': 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second Post content',
        'date_posted' : 'July 20 , 2019'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
