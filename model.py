from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)


def setup():
    global app
    app.config['MYSQL_HOST'] = '104.197.184.194'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'Excellence@321'
    app.config['MYSQL_DB'] = 'new_project'
    return MySQL(app)


mysql = setup()
