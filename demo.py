import flask
from flask_restful import Resource
from flask.json import JSONEncoder
from flask import jsonify, request
from connections import mysql
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)


class status (Resource):
    def get(self):
        try:
            return {'data': 'Api is Running'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}
 
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://murtaza@az900-mysql:Welcome1@az900-mysql.mysql.database.azure.com/demodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)


class user(db.Model):
    __tablename__ = 'ProjectDP'
    ID = db.Column(db.Integer, primary_key=True)
    City = db.Column(db.String(50), unique=True)
    Rank = db.Column(db.Integer)
    Sunshine_hours = db.Column(db.Integer)
    Cost_water = db.Column(db.Float)
    ObesityLevels_percent = db.Column(db.Float)
    Life_expectancy = db.Column(db.Float)
    Pollution_Index = db.Column(db.Float)
    Hours_worked = db.Column(db.Integer)
    Happiness_levels = db.Column(db.Float)
    Outdoor_activities = db.Column(db.Integer)
    Takeout_places = db.Column(db.Integer)
    Gym_membership = db.Column(db.Float)

    def __init__(self, ID, City, Rank, Sunshine_hours, Cost_water, ObesityLevels_percent, Life_expectancy, Pollution_Index, Hours_worked, Happiness_levels, Outdoor_activities, Takeout_places, Gym_membership):
        self.ID = ID
        self.City = City
        self.Rank = Rank
        self.Sunshine_hours = Sunshine_hours
        self.Cost_water = Cost_water
        self.ObesityLevels_percent = ObesityLevels_percent
        self.Life_expectancy = Life_expectancy
        self.Pollution_Index = Pollution_Index
        self.Hours_worked = Hours_worked
        self.Happiness_levels = Happiness_levels
        self.Outdoor_activities = Outdoor_activities
        self.Takeout_places = Takeout_places
        self.Gym_membership = Gym_membership

@app.route('/user', methods=['GET'])
def getuser():
    aData = user.query.all() 
    output=[]
    for data in aData:
        pData = {}
        pData['ID']=data.ID
        pData['City']=data.City
        pData['Rank']=data.Rank
        pData['Sunshine_hours']=data.Sunshine_hours
        pData['Cost_water']=data.Cost_water
        pData['ObesityLevels_percent']=data.ObesityLevels_percent
        pData['Life_expectancy']=data.Life_expectancy
        pData['Pollution_Index']=data.Pollution_Index
        pData['Hours_worked']=data.Hours_worked
        pData['Happiness_levels']=data.Happiness_levels
        pData['Outdoor_activities']=data.Outdoor_activities
        pData['Takeout_places']=data.Takeout_places
        pData['Gym_membership']=data.Gym_membership
        output.append(pData)
    return jsonify(output)

if(__name__ == "__main__"):
    app.run()