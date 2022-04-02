from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()

mysql.init_app(app)