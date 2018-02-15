from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
heroku = Heroku(app)
db = SQLAlchemy(app)

#from counter import Counter

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Save e-mail to database and send to success page
#@app.route('/add', methods=['POST'])
#def add():
#    email = None

#    if request.method == 'POST':
#        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
#        if not db.session.query(Counter).filter(User.email == email).count():
#            reg = Counter(email)
#            db.session.add(reg)
#            db.session.commit()
#            return
#    return render_template('index.html')

if __name__ == '__main__':
    #app.debug = True
    app.run()
