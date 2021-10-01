import datetime
import logging

from flask import Flask
from flask import redirect
from flask import render_template
from flask import session

app = Flask(__name__)
app.config.from_object('config')

logging.basicConfig(
    level='DEBUG'
)


@app.context_processor
def inject_now():
    return {'now': datetime.datetime.now()}


@app.route("/")
def root():
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    return render_template('pages/dashboard.html')


@app.route('/other')
def other():
    return render_template('pages/other.html')


@app.route('/callback')
def callback():
    print('callback called')
    print(session)
    return "OK"


@app.route('/setup')
def setup():
    print('setup called')
    print(session)
    return "OK"


# Default port:
if __name__ == '__main__':
    app.run()
