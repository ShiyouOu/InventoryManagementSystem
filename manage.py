from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
import sqlite3 as sql
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
	return	render_template("index.html")


@app.route('/summary/')
def summary():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM products")

    rows = cur.fetchall()
    return render_template("summary.html", rows = rows)

@app.route('/add/')
def add():
	return	render_template("add_inventory.html")

@app.route('/addproduct/', methods = ["POST", "GET"])
def add_product():
    if request.method == "POST":
        data = request.form
        nm = data['nm']
        desc = data['desc']
        quantity = data['quantity']
        checkin = data['checkin']

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO products (name, description, quantity, checkin) VALUES ('{0}', '{1}', '{2}', '{3}')".format(nm, desc, quantity, checkin))
            con.commit()
        return redirect(url_for('summary'))
    return "Error"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
