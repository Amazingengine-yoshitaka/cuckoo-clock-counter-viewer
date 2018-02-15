from manage import db,app

# Create our database model
class Counter(db.Model):
    __tablename__ = 'counter'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    num = db.Column(db.Integer, unique=False)

    def __init__(self, name, num):
        self.name = name
        self.num = num

    def __repr__(self, name):
        user = db.session.query(User).filter_by(name=name).first()
        user.name = "user_a"
        db.session.flush()
