from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'app.sqlite')
    # make possible to set up sql lite db
db = SQLAlchemy(app)
ma = Marshmallow(app)

# inherit from model ... only ref primary key for look up #
class Guide(db.Model)
    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class GuideSchema(ma.Schema):
    class Meta:# use tuple to expose fields we want access to
        fields = ('title', 'content')
# instantiate guide schema
# single guide
guide_schema = GuideSchema()
        guides_schema = GuideSchema(many=True)

''' dont need since making our own API endpt
@app.route('/')
def hello():
    return "Hey Flask"
'''

if __name__ == '__main__':
    app.run(debug=True)
    