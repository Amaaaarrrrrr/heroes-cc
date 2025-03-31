from flask import Flask,jsonify, request
from flask_migrate import Migrate
from models import db, Hero,  HeroPower, Power

app= Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app)
migrate= Migrate(app, db)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to House Management APi"})


#get all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200


#get hero by id
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'error': 'Hero not found'}), 404
    return jsonify(hero.to_dict()), 200


#get all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200

#get power by id
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    return jsonify(power.to_dict()), 200

#update power description
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404

    data = request.get_json()
    try:
        power.description = data.get('description', power.description)
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

#create new power
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        hero_id = data['hero_id']
        power_id = data['power_id']
        strength = data['strength']

        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)

        if not hero or not power:
            return jsonify({'error': 'Hero or Power not found'}), 404

        hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
        db.session.add(hero_power)
        db.session.commit()

        return jsonify(hero_power.to_dict()), 201
    except KeyError:
        return jsonify({'error': 'Missing required fields'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Resource not found'}), 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)