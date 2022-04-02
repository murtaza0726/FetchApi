from connections import mysql
import json
from flask import jsonify
class getDatas(object):
    def __init__(self):
        self.cursor = mysql.connect().cursor()

    def getAllData(self):
        self.cursor.execute("SELECT * FROM weather_table")
        aData = self.cursor.fetchall()
        return jsonify(aData)