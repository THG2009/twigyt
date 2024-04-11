from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/')
def home_redirect():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects/projects.html')


@app.route('/projects/alpha-apis')
def alpha_apis():
    return render_template('projects/alpha-apis.html')


if __name__ == '__main__':
    app.run()
