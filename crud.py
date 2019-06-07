from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Lamps(db.Model):

    id = db.Column(db.Integer,  nullable=False,  primary_key=True, autoincrement=True)
    price = db.Column(db.Integer, nullable=False, unique=False)
    height = db.Column(db.Integer, nullable=False, unique=False)
    currency = db.Column(db.String(50), nullable=False, unique=False)
    lightSourceType = db.Column(db.String(50), nullable=False, unique=False)
    rating = db.Column(db.String(50), nullable=False, unique=False)

    def __init__(self,
                 price=0.0,
                 height=0.0,
                 currency="USD",
                 lightSourceType="LED",
                 rating="GOOD"):

        self.price = price
        self.height = height
        self.currency = currency
        self.lightSourceType = lightSourceType
        self.rating = rating


class LampsSchema(ma.Schema):

    class Meta:

        fields = ('price', 'height', 'currency', 'lightSourceType', 'rating')


lamps_schema = LampsSchema()

lampss_schema = LampsSchema(many=True)

db.create_all()


@app.route("/lamps", methods=["POST"])
def add_lamps():

    price = request.json['price']

    height = request.json['height']

    currency = request.json['currency']

    lightSourceType = request.json['lightSourceType']

    rating = request.json['rating']

    new_lamps = Lamps(price, height, currency, lightSourceType, rating)

    db.session.add(new_lamps)

    db.session.commit()

    return lamps_schema.jsonify(new_lamps)


@app.route("/lamps", methods=["GET"])
def get_lamps():
    all_lampss = Lamps.query.all()
    result = lamps_schema.dump(all_lampss)
    return jsonify(result.data)


@app.route("/lamps/<id>", methods=["GET"])
def lamps_detail(id):

    lamps = Lamps.query.get(id)

    return lamps_schema.jsonify(lamps)


@app.route("/lamps/<id>", methods=["PUT"])
def lamps_update(id):

    lamps = Lamps.query.get(id)

    price = request.json['price']

    height = request.json['height']

    currency = request.json['currency']

    lightSourceType = request.json['lightSourceType']

    rating = request.json['rating']

    lamps.price = price

    lamps.height = height

    lamps.currency = currency

    lamps.lightSourceType = lightSourceType

    lamps.rating = rating

    db.session.commit()

    return lamps_schema.jsonify(lamps)


@app.route("/lamps/<id>", methods=["DELETE"])
def lamps_delete(id):
    lamps = Lamps.query.get(id)
    db.session.delete(lamps)
    db.session.commit()

    return lamps_schema.jsonify(lamps)


if __name__ == '__main__':
    app.debug = True
    app.run()