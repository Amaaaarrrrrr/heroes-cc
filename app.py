from flask import Flask,jsonify
from flask_migrate import Migrate
from models import db

app= Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app)
migrate= Migrate(app, db)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to House Management APi"})





if __name__ == '__main__':
    app.run(port=5555, debug=True)