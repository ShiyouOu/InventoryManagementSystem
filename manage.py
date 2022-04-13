from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
import sqlite3 as sql
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
	return	render_template("index.html")


@app.route('/summary')
def summary():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM products")

    rows = cur.fetchall()
    return render_template("summary.html", rows = rows)

@app.route('/add')
def add():
	return	render_template("add_inventory.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
