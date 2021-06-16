from datetime import datetime

from flask import Flask, render_template
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_username']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)


@app.route("/")
def welcome():
    return render_template("welcome.html", message="variables passing")


@app.route("/date")
def date():
    return "This page was served at: " + str(datetime.now())


counter = 0


@app.route("/count_view")
def count():
    global counter
    counter = counter + 1
    return "count : " + str(counter)


def get_all_records(db):
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM {db}")
    result = cursor.fetchall()
    cursor.close()
    return str(result)


def get_single_record(db, id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM {db} WHERE id={id}")
    result = cursor.fetchall()
    cursor.close()
    return str(result)


@app.route("/all/<db>")
def get_all(db):
    return get_all_records(db)


''' output /all/state: ((1, 'Alabama', 'AL'), (2, 'Alaska', 'AK'), (3, 'Arizona', 'AZ'), (4, 'Arkansas', 'AR'),
 (5, 'California', 'CA'), (6, 'Colorado', 'CO'), (7, 'Connecticut', 'CT'), (8, 'Delaware', 'DE'), 
 (9, 'District of Columbia', 'DC'), (10, 'Florida', 'FL'), (11, 'Georgia', 'GA'), (12, 'Hawaii', 'HI'), 
 (13, 'Idaho', 'ID'), (14, 'Illinois', 'IL'), (15, 'Indiana', 'IN'), (16, 'Iowa', 'IA'), (17, 'Kansas', 'KS'), 
 (18, 'Kentucky', 'KY'), (19, 'Louisiana', 'LA'), (20, 'Maine', 'ME'), (21, 'Maryland', 'MD'), (22, 'Massachusetts', 'MA'), 
 (23, 'Michigan', 'MI'), (24, 'Minnesota', 'MN'), (25, 'Mississippi', 'MS'), (26, 'Missouri', 'MO'), (27, 'Montana', 'MT'), 
 (28, 'Nebraska', 'NE'), (29, 'Nevada', 'NV'), (30, 'New Hampshire', 'NH'), (31, 'New Jersey', 'NJ'), (32, 'New Mexico', 'NM'), 
 (33, 'New York', 'NY'), (34, 'North Carolina', 'NC'), (35, 'North Dakota', 'ND'), (36, 'Ohio', 'OH'), (37, 'Oklahoma', 'OK'), 
 (38, 'Oregon', 'OR'), (39, 'Pennsylvania', 'PA'), (40, 'Rhode Island', 'RI'), (41, 'South Carolina', 'SC'), 
 (42, 'South Dakota', 'SD'), (43, 'Tennessee', 'TN'), (44, 'Texas', 'TX'), (45, 'Utah', 'UT'), (46, 'Vermont', 'VT'), 
 (47, 'Virginia', 'VA'), (48, 'Washington', 'WA'), (49, 'West Virginia', 'WV'), (50, 'Wisconsin', 'WI'), (51, 'Wyoming', 'WY'))
'''


# return render_template('Datatable.html', data=data)
@app.route("/single/<db>/<id>")
def get_single(db, id):
    return get_single_record(db, id)

# output /single/country/5: ((5, 'AS', 'American Samoa', 'American Samoa', 'ASM', '016', 'no', '1+684', '.as'),)
