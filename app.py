from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy #ORM

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'
db = SQLAlchemy(app)

class Destination(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	destination = db.Column(db.String(50), nullable=False)
	country = db.Column(db.String(50), nullable=False)
	rating = db.Column(db.Float, nullable=False)

	def to_dict(self):
		return {
			'id': self.id,
			'destination': self.destination,
			'country': self.country,
			'rating': self.rating
		}

with app.app_context():
	db.create_all()


@app.route("/", methods=['GET'])
def home():
	return jsonify({"message": "Welcome to the Travel API"})

@app.route("/destinations", methods=['GET'])
def get_destinations():
	destinations = Destination.query.all()
	return jsonify([dest.to_dict() for dest in destinations])

@app.route("/destinations/<int:id>", methods=['GET'])
def get_destination(id):
	destination = Destination.query.get(id)
	if destination:
		return jsonify(destination.to_dict())
	else:
		return jsonify({"error": "Destination not found"}), 404

@app.route("/destinations", methods=['POST'])
def add_destination():
	data = request.get_json()
	new_destination = Destination(destination=data['destination'],
	                              country=data['country'],
		                          rating=data['rating'])
	db.session.add(new_destination)
	db.session.commit()
	return jsonify(new_destination.to_dict()), 201

@app.route("/destinations/<int:id>", methods=['PUT'])
def update_destination(id):
	data = request.get_json()
	destination = Destination.query.get(id)
	if destination:
		destination.destination = data.get('destination', destination.destination)
		destination.country = data.get('country', destination.country)
		destination.rating = data.get('rating', destination.rating)
		db.session.commit()
		return jsonify(destination.to_dict())
	else:
		return jsonify({"error": "Destination not found"}), 404

@app.route("/destinations/<int:id>", methods=['DELETE'])
def delete_destination(id):
	destination = Destination.query.get(id)
	if destination:
		db.session.delete(destination)
		db.session.commit()
		return jsonify({"message": "Destination deleted"}), 204
	else:
		return jsonify({"error": "Destination not found"}), 404
if __name__ == '__main__':
	app.run(debug=True)
