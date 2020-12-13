from app import app
from flask_mysqldb import MySQL
import os

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Arka.1992'
app.config['MYSQL_DB'] = 'ecommerce'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.config['SECRET_KEY'] = 'secret'

mysql = MySQL(app)

