from flask import Flask
from flask import render_template,request,redirect,url_for,flash
from flaskext.mysql import MySQL
from flask import send_from_directory
from datetime import datetime
import os 
app= Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='123456789'
app.config['MYSQL_DATABASE_DB']='repositorio'
mysql.init_app(app)

@app.route('/')
def index():
    sql = "SELECT * FROM libros";
    conn = mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql)
    repositorios=cursor.fetchall()
    print(repositorios)
    conn.commit()
    return render_template('sitio/index.html', repositorios=repositorios)

if __name__ == '__main__':
    app.run(debug=True)