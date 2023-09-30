from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL connection
app.config['MYSQL_HOST'] = '172.19.0.2'
# app.config['MYSQL_HOST'] = 'mysql-db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Emmanuel'
app.config['MYSQL_DB'] = 'flaskcontacts'
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template("index.html", contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == "POST":
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname)
        print(phone)
        print(email)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact added succesfully!')
        return redirect(url_for('Index'))



@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', [id])
    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == "POST":
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts 
            SET fullname = %s, phone = %s, email = %s
            WHERE id = %s
        """, (fullname, phone, email, id))
        mysql.connection.commit()
        flash('Contact updated successfully')
        return redirect(url_for('Index'))
                

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact removed succesfully')
    return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 4000, debug = True)