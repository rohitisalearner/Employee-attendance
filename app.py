from flask import Flask,request,jsonify
import os
from flask_restful import Api, Resource, reqparse
from userDb import db
from myResource import ItemListResource,createItem
from flask_cors import CORS 
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

file_path = os.path.join(os.path.dirname(__file__), 'config.json')
f = open(file_path)
ConfigData = json.load(f)

# 'mysql+pymysql://username:password@localhost/db_name'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://'+ConfigData['Techpath']['Database']['User']+':'+ConfigData['Techpath']['Database']['Password']+'@'+ConfigData['Techpath']['Database']['Host']+'/'+ConfigData['Techpath']['Database']['Database']

app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api.add_resource(ItemListResource, '/items')
api.add_resource(createItem, '/create')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=5001, host="0.0.0.0")
