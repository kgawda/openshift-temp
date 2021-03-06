import os
from flask import Flask, session, redirect, url_for, escape, request, abort, send_file

app = Flask(__name__)
application = app

import actions

CSS = """
<link href="https://unpkg.com/basscss@8.0.2/css/basscss.min.css" rel="stylesheet">
<div class="clearfix"></div>
<div class="max-width-4 mx-auto"><br>
"""

@app.route("/")
def index():
    return CSS + "Hello"

@app.route("/test")
def testpage():
    return CSS +  "Test for %s, logged-%s." % (
        escape(os.environ.get('APP_MAIN_USER','user')),
        'in' if 'password' in session else 'out'
        )

@app.route("/post", methods=['GET', 'POST'])
def post():
    if not 'password' in session:
        abort(401)
    if request.method == 'POST':
        message = request.form.get('message', '')
        user = os.environ['APP_MAIN_USER']
        password = session['password']
        blogURL = os.environ['APP_BLOG_URL']

        print actions.action1(user, password, blogURL, message)

        return redirect(url_for('post'))

    return send_file('templates/home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'].strip() == os.environ['APP_MAIN_USER']:
            session['password'] = request.form['password']
            return redirect(url_for('index'))
        else:
            abort(401)
    return CSS + '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('password', None)
    return redirect(url_for('index'))

app.secret_key = os.environ['APP_SECRET_KEY']

if __name__ == "__main__":
    app.run()
